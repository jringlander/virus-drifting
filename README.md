virus-drifting 

Align multiple sequences in a fasta files with reference sequence and tracks nucleotide subsitutions in viruses over time. 
Adapted for fasta files downloaded from GISAID with limited metadata (LID, date, country, region) within the name of 
the sequence in the fasta file. 

The reference genome 'sequence.fasta' may be changed to other non-segemented virus genome and run with fasta files
containing other query genomes. The program alings reference and queries and makes an alignment file called
aligned.fasta. This files is processed and a graph containing all differences is the second output. 

Requirments: 
MAFFT aligner. 
Biopython.  

Git clone the repository to run with testdata.
Run: python viruscode.py 

Change reference and query genome: The files used in the current script, 'sequence.fasta' and 'gisaid_hcov-19_2022_10_04_14.fasta', are variable and may be changed to your own reference and query. 
The input files are found in line 11: subprocess(cat sequence.fasta gisaid.fasta> ref_query.fasta 
