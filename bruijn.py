# Generates De Bruijn Graph from a string
# Henrique Uhlmann Gobbi | hugobbi@inf.ufrgs.br
# 29/03/2023

'''
Source:
https://eaton-lab.org/slides/genomics/answers/nb-10.2-de-Bruijn.html
https://towardsdatascience.com/genome-assembly-using-de-bruijn-graphs-69570efcc270
'''

import igraph as ig

def bruijn_graph(sequence: str, k: int) -> ig.Graph:
    n = len(sequence)
    print(n)
    kmers = dict()
    for i in range(n):
        kmer = sequence[i:i+k]
        if len(kmer) != k:
            continue

        # counts frequency of kmers and add them to dictionary
        if kmer in kmers.keys():
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1

    kmers_list = kmers.keys()
    # using a set so there's no duplicate values
    vertices = set()
    edges = set()

    for kmer1 in kmers_list:
        for kmer2 in kmers_list:
            if kmer1 != kmer2:
                # checks if kmers overlap each other using k-1-mers
                if kmer1[1:] == kmer2[:-1]:
                    edges.add((kmer1[:-1], kmer2[:-1]))
                    vertices.add(kmer1[:-1])
                    vertices.add(kmer2[:-1])
                if kmer1[:-1] == kmer2[1:]:
                    edges.add((kmer2[:-1], kmer1[:-1]))
                    vertices.add(kmer1[:-1])
                    vertices.add(kmer2[:-1])

    print(edges)

    burjin_graph = ig.Graph()
    burjin_graph.add_vertices(len(vertices))
    burjin_graph.add_edges(edges)
    burjin_graph.vs['label'] = vertices

    return burjin_graph    

seq  = "ATGGAAGTCGCGGAATC"
k = 3

seq1 = "ATC"
seq2 = "ATCGCCATCCGCATCGCCGCC"
seq3 = "ATCGCCTAA"

bruijn_graph(seq, k)
