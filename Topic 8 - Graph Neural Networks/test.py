import torch

from GAT import GraphAttentionLayer


if __name__ == "__main__":
    # Configurations
    # Model input
    in_features = 2
    out_features = 2
    n_heads = 2
    is_concat = False
    dropout = 0.6
    leaky_relu_negative_slope= 0.2

    # Feature input
    n_nodes = 64

    gat_layer = GraphAttentionLayer(
        in_features=in_features,
        out_features=out_features,
        n_heads=n_heads,
        is_concat=is_concat,
        dropout=dropout,
        leaky_relu_negative_slope=leaky_relu_negative_slope
    )

    # Test the layer
    h = torch.rand(n_nodes, in_features)
    A = torch.rand(n_nodes, n_nodes, 1) > 0.5
    print("Input size: ", h.size())
    print("Adjacency matrix size: ", A.size())

    o = gat_layer.forward(h, A)
    print("Output size: ", o.size())