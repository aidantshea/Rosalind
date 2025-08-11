import os
from Bio import SeqIO
from suffix_trees import STree

# generate infile path
path: str = os.path.join("LCSM", "rosalind_lcsm.txt")

# generate list of sequences
sequences: list[str] = []
for record in SeqIO.parse(path, "fasta"):
    sequences.append(str(record.seq))

# construct tree and output longest common substring to terminal
st = STree.STree(sequences)
print(st.lcs())