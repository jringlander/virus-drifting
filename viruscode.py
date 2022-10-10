# Input is fasta files with sequence metadata in the sequence name and align.
# import packages
from Bio import SeqIO
import subprocess
import matplotlib.pyplot as plt


# Align sequences
subprocess.run('cat sequence.fasta gisaid_hcov-19_2022_10_04_14.fasta > ref_query.fasta | mafft ref_query.fasta > aligned.fasta', shell=True)

# List and dictionary of alignment
multifasta = list(SeqIO.parse("aligned.fasta", format = 'fasta'))

queries = {}
for entry in multifasta:
    queries[entry.id] = entry

# Define gaps
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

# Print mutations compared to reference
for item in queries:
    print (item + ' '+str(len(get_mutations(queries['NC_045512.2'], queries[item]))))

# Count all substitutions (AT, AC, AG, GC, GA, GT, TA, TC, TC, CA, CG, CT) compared to ref
for item in queries:


# The sum of each different substitutions divided with the number of unique sequences from the respective dates

# Substitution frequency of each type of substitutions on each date into csv file

# Make graph of substitution frequency of all possible substitutions for all dates
# matplotlib
#for y, item in enumerate(queries):
    #plt.plot((0, len(queries['NC_045512.2'])), (y,y), color = 'lightgrey')





