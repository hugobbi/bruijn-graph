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

        if kmer in kmers.keys():
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1

    print(kmers)

    return 1

seq = "ATGGAAGTCGCGGAATC"
k = 3

seq1 = "ATC"
seq2 = "ATCGCCATCCGCATCGCCGCC"
seq3 = "ATCGCCTAA"

bruijn_graph(seq, k)