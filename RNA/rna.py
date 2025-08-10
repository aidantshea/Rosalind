import os

# read in nucleotide sequence
content: str = ""
with open(os.path.join("RNA", "rosalind_rna.txt"), 'r') as file:
    content = file.read().strip()

# convert input dna sequence into corresponding rna sequence
rna_sequence: str = content.replace("T", "U")

# output to terminal
print(rna_sequence)