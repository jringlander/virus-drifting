# Input is minimap2 aligned data with sequence metadata in the fasta files. Metadata is formatted and
#followed by the actual sequence

import samtools
import pandas
import mappy as mp

a = mp.Aligner("SARS-CoV-2.fa")



# Count all substitutions (AT, AC, AG, GC, GA, GT, TA, TC, TC, CA, CG, CT) compared to ref for all seqs and put name and
# number of certain substitutions in new csv file
 = int(input())

def subsitution_count()
    if refpos = "A"
        and seqpos ["G""T""C"]
            "A"=1



# The sum of each different substitutions divided with the number of unique sequences from the respective dates

# Substitution frequency of each type of substitutions on each date into csv file

# Make graph of substitution frequency of all possible substitutions for all dates
matplotlib




