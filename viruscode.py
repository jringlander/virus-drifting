# Input is fasta files with sequence metadata in the sequence name and align.
# import packages
from Bio import SeqIO
import subprocess
import re
import matplotlib.pyplot as plt
import numpy


# Align query sequences with reference
subprocess.run('cat sequence.fasta gisaid_hcov-19_2022_10_04_14.fasta > ref_query.fasta | mafft ref_query.fasta > aligned.fasta', shell=True)

# List and dictionary of alignment
multifasta = list(SeqIO.parse("aligned.fasta", format = 'fasta'))

queries = {}
for entry in multifasta:
    queries[entry.id] = entry.seq

# Define gaps from alignment
def gapped_pos(seq, pos):
    no_gap = 0
    gaps = 0
    for nt in seq:
        if nt !='-':
            no_gap += 1
        else:
            gaps += 1
            if no_gap == pos:
                return pos + gaps

# Call mutations compared to reference
def get_mutations(initial, variant):
    out = []
    queries = list(zip(initial, variant))
    for pos, nt in enumerate(queries):
        if nt[0] != nt[1]:
            out.append(nt[0].upper() + str(pos) + nt[1].upper())
    return out

# Print number of mutations compared to reference and all separate mutations
for item in queries:
    print(get_mutations(queries['NC_045512.2'], queries[item]))
    print(item + ' '+str(len(get_mutations(queries['NC_045512.2'], queries[item]))))

# New dictionary of mutations
mutations = {}
for item in queries:
    mutations[item] = get_mutations(queries['NC_045512.2'], queries[item])

# Make graph of substitution frequency of all possible substitutions for all dates
plt.figure(figsize = (35,10))
for y, item in enumerate(queries):
    plt.plot((0, len(queries['NC_045512.2'])), (y,y), color = 'lightgrey')
    plt.text(-160, y+1, item, va = 'center', ha='right')

    for mutation in mutations[item]:
        pos = int(mutation[1:-1])
        nt_change = mutation[-1]
        plt.text(pos, y, nt_change, va = 'center', ha = 'center')

    plt.xlim(-300, len(queries['NC_045512.2']) + 100)
    plt.ylim(0, 4)
    plt.savefig('drift.pdf')

# Count all substitutions (AT, AC, AG, GC, GA, GT, TA, TC, TC, CA, CG, CT) compared to ref

# The sum of each different substitutions divided with the number of unique sequences from the respective dates

# Substitution frequency of each type of substitutions on each date into csv file

