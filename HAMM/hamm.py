import os

# read in nucleotide sequence
content: str = ""
with open(os.path.join("HAMM", "rosalind_hamm.txt"), 'r') as file:
    content = file.read().strip()

seq1: str; seq2: str
seq1, seq2 = content.split('\n')

hamming_distance: int = 0
for i in range(len(seq1)):
    if (seq1[i] != seq2[i]):
        hamming_distance += 1

print(hamming_distance)