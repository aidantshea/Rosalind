import os

# read in nucleotide sequence
content: str = ""
with open(os.path.join("REVC", "rosalind_revc.txt"), 'r') as file:
    content = file.read().strip()

# get the reverse sequence
reverse_sequence: str = ''.join(reversed(content))

# initialize dictionary storing nucleotides and their complements
complements: dict[str, str] = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

# generate translation table from the complement key-value pairs
translation_table = str.maketrans(complements)

# get the reverse complement
reverse_complement: str = reverse_sequence.translate(translation_table)

# output to terminal
print(reverse_complement)