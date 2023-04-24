import torch

from torch import nn


class GraphAttentionLayer(nn.Module):
    """
    Graph Attention Network implementation.
    
    GATs work on graph data. A graph consists of nodes and edges
    connecting nodes. It uses masked self-attention, similar to transformers.
    GAT consists of graph attention layers stacked on top of each other.
    Each graph attention layers gets node embeddings as inputs and outputs
    transformed embeddings. The node embeddings pay attention to the embeddings
    of other nodes it's connected to.

    Args:
    -------
        in_features: int
            $F$, the number of input features per node
        out_features: int
            $F'$, the number of output features per node
        n_heads: int
            $K$, the number of attention heads
        is_concat: bool
            If True, the multi-head result will be concatenated.
            Otherwise they will be averaged.
        dropout: float (0 to 1)
            Dropout probability.
        leaky_relu_negative_slope: float
            Negative slope for leaky relu activation.
    """

    def __init__(
        self,
        in_features: int,
        out_features: int,
        n_heads: int,
        is_concat: bool = True,
        dropout: float = 0.6,
        leaky_relu_negative_slope: float = 0.2
    ):
        super().__init__()

        self.is_concat      = is_concat
        self.n_heads        = n_heads

        # Calculate the number of dimensions per head (n_hidden)
        if is_concat:
            assert out_features % n_heads == 0
            self.n_hidden = out_features // n_heads
        else:
            self.n_hidden = out_features

        self.linear         = nn.Linear(in_features, self.n_hidden * n_heads, bias=False)
        self.attn           = nn.Linear(self.n_hidden * 2, 1, bias=False)
        self.activation     = nn.LeakyReLU(negative_slope=leaky_relu_negative_slope)
        self.softmax        = nn.Softmax(dim=1)
        self.dropout        = nn.Dropout(dropout)

    def forward(self, h: torch.Tensor, A: torch.Tensor) -> torch.Tensor:
        """
        Forward call of GAT.
        Where h is the input node embeddings of shape [n_nodes, in_features].
        A is the adjacency matrix of shape [n_nodes, n_nodes, 1] or
        [n_nodes, n_nodes, n_heads] if adjacency matrices are different for each node.
        """
        n_nodes = h.shape[0]
        
        # Initial transformation
        g = self.linear(h)
        g = g.view(n_nodes, self.n_heads, self.n_hidden)

        # Calculate attention score
        
        # g_repeat gets {g1, g2, ..., gN, g1, g2, ..., gN, ...}
        g_repeat = g.repeat(n_nodes, 1, 1)
        # g_repeat_interleave gets {g1, g1, ..., g1, g2, g2, ..., g2, ...}
        g_repeat_interleave = g.repeat_interleave(n_nodes, dim=0)
        # g_concat get {g1 || g1, g1 || g2, ..., g1 || gN, g2 || g1, ..., gN || gN}
        g_concat = torch.cat([g_repeat_interleave, g_repeat], dim=-1)
        # Reshape so that g_concat[i, j] is gi || gj
        g_concat = g_concat.view(n_nodes, n_nodes, self.n_heads, 2 * self.n_hidden)

        # Calculate e_ij (shep: [n_nodes, n_nodes, n_heads, 1])
        e = self.activation(self.attn(g_concat))
        # Reshape to (shape: [n_nodes, n_nodes, n_heads])
        e = e.squeeze(-1)

        # Adjacency shape checking
        assert A.shape[0] == 1 or A.shape[0] == n_nodes
        assert A.shape[1] == 1 or A.shape[1] == n_nodes
        assert A.shape[2] == 1 or A.shape[2] == self.n_heads

        # Mask e_ij based on A, e_ij = -inf if there is no edge from i to j
        e = e.masked_fill(A == 0, float('-inf'))

        # Normalize attention score
        a = self.softmax(e)
        # Apply dropout
        a = self.dropout(a)

        # Calcuate final output for each head
        # h_i^k = sum a_ij^k g_j^k
        attn_res = torch.einsum('ijh, jhf->ihf', a, g)

        # Concatenate or average the heads
        if self.is_concat:
            return attn_res.reshape(n_nodes, self.n_heads * self.n_hidden)
        else:
            return attn_res.mean(dim=1)