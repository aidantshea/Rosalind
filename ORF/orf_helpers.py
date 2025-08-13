# this function returns the reverse complement of a given DNA sequence
def get_reverse_complement(seq: str) -> str:
    
    # get the reverse sequence
    reverse_sequence: str = ''.join(reversed(seq))

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

    return reverse_complement