import os
from amino_acid_mass_table import aa_masses

# read in amino acid sequence
protein_seq: str = ""
with open(os.path.join("PRTM", "rosalind_prtm.txt"), 'r') as file:
    protein_seq = file.read().strip()

# calculate protein mass
protein_mass: float = 0
for aa in protein_seq:
    protein_mass += aa_masses[aa]

print(protein_mass)