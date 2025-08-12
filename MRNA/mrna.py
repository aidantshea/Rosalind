import os
from codon_table import codon_table

# read in protein sequence
protein_sequence: str = ""
with open(os.path.join("MRNA", "rosalind_mrna.txt"), 'r') as file:
    protein_sequence = file.read().strip()

# create python dict that lists number of possible codons that translate to each protein
num_codons_per_protein: dict[str, int] = {}
for protein in codon_table.values():
    num_codons_per_protein[protein] = sum(1 for codon in codon_table.keys() if codon_table[codon] == protein)

# count possible mrnas
mrnas: int = 3  # starting with 3 for stop codon
for char in protein_sequence:
    mrnas = mrnas * num_codons_per_protein[char] % 1000000

# output to terminal 
print(mrnas)