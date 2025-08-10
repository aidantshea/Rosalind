import os
from Bio import SeqIO

# generate infile path
path: str = os.path.join("GRPH", "rosalind_grph.txt")

# generate dictionary of IDs and sequences
records: dict[str, str] = {}
for record in SeqIO.parse(path, "fasta"):
    records[str(record.id)] = str(record.seq)

# generate edges
edges: list[list[str]] = []
for id_for_s in records.keys():
    for id_for_t in records.keys():
        s: str = records[id_for_s]
        t: str = records[id_for_t]
        if (s[len(s)-3:len(s)] == t[0:3] and s != t):
            edges.append([id_for_s,id_for_t])

# output to terminal
for edge in edges:
    print(edge[0] + " " + edge[1])