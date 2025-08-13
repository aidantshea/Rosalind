from Bio import SeqIO
import os, itertools
from splc_helpers import translate

# generate infile path
path: str = os.path.join("SPLC", "rosalind_splc.txt")

# set up iterator for fasta files
fasta_iter, peek = itertools.tee(SeqIO.parse(path, "fasta"))

# scrape main sequence
seq: str = str(next(fasta_iter).seq)

# scrape intron sequences
introns: list[str] = []; has_next: bool = True
while (has_next):
    try:
        introns.append(str(next(fasta_iter).seq))
    except StopIteration:
        has_next = False

# generate exon sequence
exon_seq: str = seq
for intron in introns:
    exon_seq = exon_seq.replace(intron, "")

# translate to protein and output to terminal
print(translate(exon_seq))