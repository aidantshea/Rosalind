import os

# read in nucleotide sequence
content: str = ""
with open(os.path.join("SUBS", "rosalind_subs.txt"), 'r') as file:
    content = file.read().strip()

# split input string into sequence and substring of interest
sequence: str; substring: str
sequence, substring = content.split('\n')

# search string for subsequence, save indices to memory
indices: list[int] = []
for i in range(len(sequence) - len(substring) + 1):
    if (sequence[i:i+len(substring)] == substring):
        indices.append(i + 1)   # adjusting to 1-indexing

# output to terminal
for index in indices:
    print(str(index) + " ", end="")