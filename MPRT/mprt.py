import os
import requests, requests_cache
from Bio import SeqIO
from io import StringIO

# enable caching with SQLite
requests_cache.install_cache("mprt_cache")

# read in uniprot_id list
content: str = ""
with open(os.path.join("MPRT", "rosalind_mprt.txt"), 'r') as file:
    content = file.read().strip()

# load uniprot_id list as list of strings
uniprot_ids: list[str] = list(map(str, content.split()))

# initialize dictionary containing uniprot IDs and their respective sequences
sequences: dict[str, str]= {}
for id in uniprot_ids:
    url: str = r"http://www.uniprot.org/uniprot/" + id.split('_')[0] + ".fasta"

    response = requests.get(url)
    fasta = StringIO(response.text)
    seq: str = str(next(SeqIO.parse(fasta, "fasta")).seq)
    sequences[id] = seq

    print(f"loaded sequence {id}")

# create a dictionary associating each uniprot ID with a list of locations of the N-glycosylation motif
motif_locations: dict[str, list[int]] = {}
for id in uniprot_ids:
    seq: str = sequences[id]
    motif_locations[id] = []
    for i in range(len(seq) - 3):
        if (seq[i] == 'N' and seq[i+1] != 'P' and seq[i+2] in 'ST' and seq[i+3] != 'P'):
            motif_locations[id].append(i + 1)   # adjust for 1-indexing

# output to terminal
print()
for key in motif_locations.keys():
    if (motif_locations[key] == []):
        continue
    print(key)
    for loc in motif_locations[key]:
        print(str(loc) + " ", end="")
    print()