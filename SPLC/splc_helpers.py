from dna_codon_table import dna_codon_table

# this function returns a protein sequence given an exon sequence
def translate(seq: str) -> str:
    protein: str = ""
    for i in range(0, len(seq), 3):
        codon: str = seq[i:i+3]
        if (dna_codon_table[codon] == "Stop"):
            break
        protein += dna_codon_table[codon]
    
    return protein