# Input is fasta files with sequence metadata in the sequence name and align.
from Bio import SeqIO
from Bio.Align import PairwiseAligner

target = SeqIO.parse("/Users/johanringlander/Desktop/Sv__Sekvensering_tidiga_stammar/14_SE300_DE-20-007850.consensus.fasta", "fasta")

queries = {}
for seq_record in SeqIO.parse("/Users/johanringlander/Downloads/gisaid_hcov-19_2022_10_04_14.fasta", "fasta"):
    #print (seq_record.id)
    queries[seq_record.id] = seq_record.seq

for k,v in queries.items():
    # align v to target
({k})
aligner = PairwiseAligner()
aligner.gap_score = -10
alignments = aligner.align(target, query)
len(alignments)
alignment = alignments[0]
print(alignment)

# Count all substitutions (AT, AC, AG, GC, GA, GT, TA, TC, TC, CA, CG, CT) compared to ref
m = alignment.substitutions
print(m)

# The sum of each different substitutions divided with the number of unique sequences from the respective dates

# Substitution frequency of each type of substitutions on each date into csv file

# Make graph of substitution frequency of all possible substitutions for all dates
# matplotlib




