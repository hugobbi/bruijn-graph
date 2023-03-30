# Generates De Bruijn Graph from a string
# Henrique Uhlmann Gobbi | hugobbi@inf.ufrgs.br
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
    burjin_graph = ig.Graph(directed=True)
    burjin_graph.add_vertices(vertices)
    burjin_graph.add_edges(edges)
    burjin_graph.vs['label'] = vertices

    # Plots and saves the graph
    visual_style = {}
    #visual_style['bbox'] = (2000, 2000)
    visual_style['margin'] = 60
    visual_style['layout'] = burjin_graph.layout('auto')
    visual_style['vertex_color'] = 'orange'
    visual_style['vertex_size'] = 30
    visual_style['edge_curved'] = False
    ig.plot(burjin_graph, target='burijn_graph.pdf', **visual_style)  

    print(burjin_graph.summary())

    return burjin_graph    

seq  = 'ATGGAAGTCGCGGAATC'
k = 3
teste = 'AAGATTCTCTAAGA'

bruijn_graph(seq, k)
