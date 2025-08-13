import os
from Bio import SeqIO
from revp_helpers import get_reverse_complement

# generate infile path
path: str = os.path.join("REVP", "rosalind_revp.txt")

# scrape sequence and determine its reverse complement
seq: str = str(next(SeqIO.parse(path, "fasta")).seq).strip()
revc: str = get_reverse_complement(seq)

print(seq)
print(revc)

# sliding window, see if seq is same as revc
for i in range(4, 14, 2):                                   # for each length of sliding window
    for j in range(0, len(seq) - i + 1, 1):                 # and for the length of the total sequence
        subseq: str = seq[j:j+i]                            # get each subsequence
        if (subseq == get_reverse_complement(subseq)):      # list subsequences that match their reverse complement
            print(str(j + 1) + " " + str(i))                # adjust for 1-indexing