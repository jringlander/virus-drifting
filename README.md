# virus-drifting 

Aligns multiple query sequences in one fasta file with a reference sequence in another fasta file and calls variants in the query sequences.  
Adapted for fasta files containing SARS-CoV-2 sequences downloaded from GISAID's EpiCov database with limited metadata (country, isolate name, LID, date) within the name of the sequence. The reference genome 'sequence.fasta' may however be changed to other non-segemented virus genomes and run with fasta files containing other query genomes. The reference and queries are preferably the same or related viruses with similiar genomes. The program alings reference and queries and makes an alignment file called aligned.fasta. Aligned.fasta is one of the output files. This file is processed, a text file and a graph containing all differences compared to the reference are made and put in the current repository. 

## Requirements 
The script is written in python 3 and require some programs to be installed. All may be installed with conda in the terminal.  

Biopython:   

    conda install -c anaconda biopython  
    
MAFFT aligner:  

    conda install -c bioconda mafft
Matplotlib:

    conda install matplotlib


## How to run 
Git clone the repository to run with testdata.

Run the script in the terminal:  

    python viruscode.py

Change reference and query genome: The files used in the current script are provided as testa data, "sequence.fasta" and "gisaid_hcov-19_2022_10_04_14.fasta", and may be changed to your own reference and query, only fasta files are allowed. The input files are found in line 11:  

    subprocess(cat sequence.fasta gisaid.fasta > ref_query.fasta

## Work in progress 
Future versions will include analysis of substitutions over time.  
