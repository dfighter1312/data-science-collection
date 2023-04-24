# Graph Attention Networks

## What this repository do?

Hands-on implementation of Graph Neural Networks. Following the instruction of https://nn.labml.ai/graphs/gat/index.html.

## How to run this repository?

**Step 1:** Go to the directory
```bash
cd "Topic 8 - Graph Neural Networks"
```

**Step 2:** Install `torch`. Search on Google for more details

**Step 3:** Run the test by the following script
```bash
python test.py
```
*You will see the console print out 3 lines corresponding to the sizes of input features h, adjacency matrix A and output o.*

## Struggle and Derived Tips during implementation

**1. Torch Einsum**

It may be overwhelming for beginner to first learn this function. But people said that it is really useful for implementing a new layer/model if we know about einsum. I may suggest this video [here](https://www.youtube.com/watch?v=pkVwUVEHmfI) to know about einsum.