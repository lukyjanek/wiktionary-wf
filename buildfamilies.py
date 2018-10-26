#!usr/bin/env python3
# coding: utf-8

"""Convert directed graph of lexemes to the complete graph of lexemes."""

import argparse
import networkx as nx


# Arguments parsing
parser = argparse.ArgumentParser()

parser.add_argument('-i', action='store', dest='i', required=True,
                    help='path to the extracted wikti release')
parser.add_argument('-o', action='store', dest='o', required=True,
                    help='path to the output file')

par = parser.parse_args()


# Load data
all_relations = list()
print('Info: Loading data...')

with open(par.i, mode='r', encoding='utf-8') as f:
    for line in f:
        rel = line.strip().split('\t')
        all_relations.append(tuple(rel))

print('Info: Data loaded.')


# Build families from pairs
print('Info: Building families from pairs...')

G = nx.Graph()
G.add_edges_from(all_relations)

print('Info: Families builded.')


# Save data to file
print('Info: Saving data...')

with open(par.o, mode='w', encoding='utf-8') as f:
    for family in sorted(nx.connected_components(G)):
        f.write('\t'.join(family) + '\n')

print('Info: Data saved.')
print('Info: Complete.')
