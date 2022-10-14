# Input is fasta files with sequence metadata in the sequence name. The script aligns sequences and calls all variants compared to reference.
# import packages
from Bio import SeqIO
import subprocess
import matplotlib.pyplot as plt

# Align query sequences with reference
subprocess.run('cat sequence.fasta gisaid_hcov-19_2022_10_04_14.fasta > ref_query.fasta | mafft ref_query.fasta > aligned.fasta', shell=True)

# List and dictionary of alignment
multifasta = list(SeqIO.parse("aligned.fasta", format = 'fasta'))

queries = {}
for entry in multifasta:
    queries[entry.id] = entry.seq


# Call mutations compared to reference
def get_mutations(initial, variant):
    out = []
    queries = list(zip(initial, variant))
    for pos, nt in enumerate(queries):
        if nt[0] != nt[1]:
            out.append(nt[0].upper() + str(pos) + nt[1].upper())
    return out

# New dictionary of mutations
mutations = {}
for item in queries:
    mutations[item] = get_mutations(queries['NC_045512.2'], queries[item])

# Print number of mutations compared to reference and all separate mutations
f = open('mutations_results.txt', 'w')
for item in queries:
    print((item + str(mutations[item])), file = f)
    print(item + ' '+str(len(mutations[item])), file = f)
f.close()

# Make graph of substitution frequency of all possible substitutions for all dates
plt.figure(figsize = (50,15))
for y, item in enumerate(queries):
    plt.plot((0, len(queries['NC_045512.2'])), (y,y), color = 'lightgrey')
    plt.text(-160, y, item, va = 'top', ha ='right')

    for mutation in mutations[item]:
        pos = int(mutation[1:-1])
        nt_change = mutation[-1]
        plt.text(pos, y, nt_change, va = 'bottom', ha = 'center')

    plt.xlim(-300, len(queries['NC_045512.2']) + 100)
    plt.ylim(0, 4)
    plt.savefig('drift.pdf')

# Count all substitutions (AT, AC, AG, GC, GA, GT, TA, TC, TC, CA, CG, CT) compared to ref
#subf = open('substitutions_results.txt', 'w')
#substitution = ('[A-Z](\d+)[A-Z]')
#for substitution in mutations:
#    print(item + ' '+str(substitution), file = subf)
#f.close()

# The sum of each different substitutions divided with the number of unique sequences from the respective dates

# Substitution frequency of each type of substitutions on each date into csv file
