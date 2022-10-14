# virus-drifting 

Aligns multiple query sequences in one fasta file with a reference sequence in anouther fasta file and calls variants in the query sequences.  
Adapted for fasta files downloaded from GISAID's EpiCov database with limited metadata (country, isolate name, LID, date) within the name of 
the sequence. The reference genome 'sequence.fasta' may however be changed to other non-segemented virus genomes and run with fasta files
containing other query genomes. The reference and queries are preferably the same or related viruses with similiar genomes. The program alings reference and queries and makes an alignment file called aligned.fasta. Aligned.fasta is one of the output files. This file is processed, a text file and a graph containing all differences compared to the reference are also output. 

## Requirements 
Biopython:  conda install -c anaconda biopython
MAFFT aligner: conda install -c bioconda mafft

### How to run 
Git clone the repository to run with testdata.
Run: python viruscode.py 

Change reference and query genome: The files used in the current script are provided as testa data, 'sequence.fasta' and 'gisaid_hcov-19_2022_10_04_14.fasta', may be changed to your own reference and query. The input files are found in line 11: subprocess(cat sequence.fasta gisaid.fasta> ref_query.fasta 

Future versions will include analysis of substitutions over time.  
