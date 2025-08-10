import os
from Bio import SeqIO

# generate infile path
path: str = os.path.join("GC", "rosalind_gc.txt")

# helper function to calculate GC content in a string
def calculate_gc(seq: str) -> float:
    return (seq.count('G') + seq.count('C')) * 100 / len(seq)

# generate dictionary of IDs and GC content
records: dict[str, float] = {}
for record in SeqIO.parse(path, "fasta"):
    records[record.id] = calculate_gc(str(record.seq))

# retrieve record with highest gc content
record_with_highest_gc = max(records, key=records.get)

# output to terminal
print(f"{record_with_highest_gc}\n{records.get(record_with_highest_gc)}")