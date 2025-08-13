import os
from Bio import SeqIO
from orf_helpers import get_reverse_complement
from dna_codon_table import dna_codon_table

# generate infile path
path: str = os.path.join("ORF", "rosalind_orf.txt")

# scrape sequence and determine its reverse complement
seq: str = str(next(SeqIO.parse(path, "fasta")).seq).strip()
revc: str = get_reverse_complement(seq)

# generate reading frames
reading_frames: list[str] = []                                          # generate each of three reading frames from the seq and reverse complement
for i in range(3):
    reading_frames.append(seq[i:])
    reading_frames.append(revc[i:])

reading_frames = [s[:len(s) - (len(s) % 3)] for s in reading_frames]    # cut down each frame such that the length is a multiple of three

# find candidate sequences for translation, i.e. open reading frames
candidate_sequences: set[str] = set()
for frame in reading_frames:
    for i in range(0, len(frame), 3):                           # loop through the codons
        if (frame[i:i+3] == "ATG"):                             # and for each start codon,
            candidate_seq: str = frame[i:i+3]                   # start a new candidate DNA sequence for translation
            
            for j in range(i+3, len(frame), 3):                 # then loop through the rest of the codons
                codon: str = frame[j:j+3]
                if (codon in ["TAA", "TAG", "TGA"]):            # if a stop codon is found, 
                    candidate_seq += codon
                    candidate_sequences.add(candidate_seq)      # add the sequence to the candidates 
                    break
                else:
                    candidate_seq += codon                      # otherwise keep looping, and eventually discard in the case of no stop codon

#print(candidate_sequences)

# now translate to protein strings with the DNA codon table
candidate_proteins: set[str] = set()
for seq in candidate_sequences:
    prot: str = ""
    for i in range(0, len(seq) - 3, 3):
        codon: str = seq[i:i+3]
        prot += dna_codon_table[codon]
    candidate_proteins.add(prot)

for candidate in candidate_proteins:
    print(candidate)