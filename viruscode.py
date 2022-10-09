# Input is fasta files with sequence metadata in the sequence name and align.
# import packages
from Bio import SeqIO
import subprocess

# Align sequences
subprocess.run('cat sequence.fasta gisaid_hcov-19_2022_10_04_14.fasta > ref_query.fasta| mafft ref_query.fasta > aligned.fasta', shell=True)

# List and dictionary of alignment
multifasta = list(SeqIO.parse("aligned.fasta", format = 'fasta'))

for entry in multifasta:
    print(entry.id)

queries = {}
for entry in multifasta:
    queries[entry.id] = entry

print(queries['hCoV-19/Poland/WSSEGorzow-22S3280/2022|EPI_ISL_15234788|2022-09-16'].seq)

for entry in multifasta:
    print(len(entry.seq))

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

# Count all substitutions (AT, AC, AG, GC, GA, GT, TA, TC, TC, CA, CG, CT) compared to ref
def get_mutations(initial, variant):
    queries = list(zip(initial, variant))
    for pos, nt in enumerate(queries):
        if nt[0] != nt[1]:
            print(nt[0].upper() + str(pos) + nt[1].upper())

get_mutations(queries['NC_045512.2'], queries['hCoV-19/Poland/WSSEGorzow-22S3285/2022|EPI_ISL_15234790|2022-09-20'])

# The sum of each different substitutions divided with the number of unique sequences from the respective dates

# Substitution frequency of each type of substitutions on each date into csv file

# Make graph of substitution frequency of all possible substitutions for all dates
# matplotlib




