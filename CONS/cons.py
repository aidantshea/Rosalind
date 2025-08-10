import os
from Bio import SeqIO

# generate infile path
path: str = os.path.join("CONS", "rosalind_cons.txt")

# generate dictionary of IDs and GC content
sequences: list[str] = []
for record in SeqIO.parse(path, "fasta"):
    sequences.append(str(record.seq))

# initialize profile matrix
length: int = len(sequences[0])
profile: dict[str, list[int]] = {
    'A':[0] * length,
    'C':[0] * length,
    'G':[0] * length,
    'T':[0] * length
}

# populate profile matrix
for seq in sequences:
    for i, nucleotide in enumerate(seq):
        profile[nucleotide][i] += 1

# generate consensus sequence
consensus: str = ""
for i in range(length):
    consensus += max(profile, key=lambda key: profile[key][i])

# output to terminal
print(consensus)
for key in profile.keys():
    print(key, end=": ")
    for num in profile[key]:
        print(str(num) + " ", end="")
    print()