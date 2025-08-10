import os
from codon_table import codon_table

# read in nucleotide sequence
content: str = ""
with open(os.path.join("PROT", "rosalind_prot.txt"), 'r') as file:
    content = file.read().strip()

# generate protein sequence, breaking at stop codon
protein: str = ""
for i in range(0, len(content), 3):
    codon: str = content[i:i+3]
    if (codon_table[codon] == "Stop"):
        break
    protein += codon_table[codon]

# output to terminal
print(protein)