# Generates De Bruijn Graph from a string
# Henrique Uhlmann Gobbi - hugobbi@inf.ufrgs.br
# Biologia Computacional - INF05018 - 2022/2
# 29/03/2023

import igraph as ig

def bruijn_graph(sequence: str, k: int) -> ig.Graph:
    n = len(sequence)
    vertices = set()
    edges = list()
    for i in range(n - k + 1):
        kmer = sequence[i:i+k]
        kmer_l = kmer[:-1]
        kmer_r = kmer[1:]
        vertices.add(kmer_l)
        vertices.add(kmer_r)
        edges.append((kmer_l, kmer_r))

    # Creates the graph using igraph
    vertices = list(vertices)
    bruijn_graph = ig.Graph(directed=True)
    bruijn_graph.add_vertices(vertices)
    bruijn_graph.add_edges(edges)
    bruijn_graph.vs['label'] = vertices

    # Plots and saves the graph
    visual_style = {}
    visual_style['margin'] = 60
    visual_style['vertex_color'] = 'orange'
    visual_style['vertex_size'] = 30
    ig.plot(bruijn_graph, target='bruijn_graph.pdf', **visual_style)  

    print(bruijn_graph)
    print(bruijn_graph.summary())

    return bruijn_graph
    