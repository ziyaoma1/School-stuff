def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> (bool)

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    num = dna1.count(dna2)
    return num > 0
def is_valid_sequence(dna):
    """ (str) -> bool
    Return whether the DNA sequence is valid or not.

    >>> is_valid_sequence("ANFASD")
    False
    >>> is_valid_sequence("ATCG")
    True
    """
    num = 0

    for char in dna:
        if not char in 'ATCG':
            num = num + 1
    return num == 0
def insert_sequence(dna1,dna2,loc):
    """(str,str,int) -> (str)
    Return combined sequence by inserting dna2 within dna1 with the specified
    location of loc

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    """
    return (dna1[:loc] + dna2 + dna1[loc:])

def get_complement(nuc):
    """ str -> str
    Returns the complementary nucleotide of nuc
    get_complement('A')
    'T'
    get_complement ('C')
    'G'
    """
    complement = ''
    if nuc == 'A':
        complement = 'T'
    elif nuc == 'T':
        complement = 'A'
    elif nuc == 'C':
        complement = 'G'
    elif nuc == 'G':
        complement = 'C'
    return complement
def get_complementary_sequence(dna):
    """ (str) -> str
    Returns the complementary DNA sequence of dna
    >>>get_complementary_sequence ('AT')
    'TA'
    >>>get_complementary_sequence ('ATCG')
    'TAGC'
    """
    complementary = ''
    for c in dna:
        complementary = complementary + get_complement(c)
    return complementary
