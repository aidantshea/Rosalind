import os

# read in nucleotide sequence
content: str = ""
with open(os.path.join("DNA", "rosalind_dna.txt"), 'r') as file:
    content = file.read().strip()

# define key-value pairs of nucleotide bases and frequency
counts: dict[str, int] = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0
}

# count nucleotide frequency in input sequence
for char in content:
    counts[char] += 1

# output to terminal
for value in counts.values():
    print(str(value) + " ", end="")