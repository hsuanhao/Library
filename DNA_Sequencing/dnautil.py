#!/usr/bin/python
"""

dnautil module contains useful functions to process DNA sequence.

"""



def gc(dna):
    """
    
    This function compute the GC percentage of a DNA sequence
    
    Parameters
    ---------
    dna: str A DNA sequence
    
    Returns
    -------
    gcpercent: float GC percentage of a DNA sequence
    
    
    """
    
    # nbases is number of non-defined bases n or N
    nbases = dna.count('n') + dna.count('N')
    
    # gcpercent is GC percentage of a DNA sequence
    gcpercent = (dna.count('c') + dna.count('C') + dna.count('g') + dna.count('G'))*1.0/(len(dna)-nbases)
    
    return gcpercent

def dna_has_stop(dna, frame=0):
    """
    
    This function check if a given DNA sequence
    contains an in-frame stop codon.
    
    Parameters
    ---------
    dna: str A DNA sequence
    
    frame: int frame argument equal to 0, 1, or 2.
               Default is 0.
    
    Returns
    -------
    stop_codon_found: boolean Whether the DNA sequence contains stop codon
    
    """
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    
  
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()
        
        # Check whether codon is a stop codon
        if codon in stop_codons:
            stop_codon_found = True
            break
    
    if stop_codon_found:
        print("Input sequence has an in-frame stop codon.")
    else:
        print("Input sequence has no in-frame stop codon.")
        
    return stop_codon_found

def reverse_complement(dna):
    """
    
    A function to reverse complement of the dna sequence.
    
    Parameters
    ----------
    dna: str A DNA sequence
    
    
    Returns
    -------
    seq: str A reverse complement of the input DNA sequence
    
    """
    seq = reverse_string(dna)
    seq = complement(seq)
    return seq
    
    
    
def reverse_string(string):
    """
    A function to reverse a string
    
    Parameters
    ----------
    string: str string to be reversed
    
    Retruns
    -------
    reversed string
    """
    
    return string[::-1]


def complement(dna):
    """
    
    Return the complementary sequence of a DNA sequence
    
    Parameters
    ----------
    dna: str A DNA sequence
    
    Returns
    -------
    complement: str complementary sequence of a DNA sequence
    
    """
    base_complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', \
                      'N':'N', 'a':'t', 'c':'g', 'g':'c', \
                      't':'a', 'n':'n'}
    
    letters = list(dna)
    letters = [base_complement[base] for base in letters]
    
    complement = ''.join(letters)
    
    return complement
    