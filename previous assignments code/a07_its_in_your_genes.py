######################################################################
# Author(s): Daize Njounkeng, Maria Belen Saavedra
# Username(s): njounkengdaizem, saavedrariosm
#
# Assignment: A07: It's in Your Genes
#
# Purpose: Determine an amino acid sequence given an input DNA sequence
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence:
    :return:True or false depending if the sequence is valid. Consiting of only A, C, G and T
    """
    nucleo = "ACGT"                    #initialised a valid string

    for i in sequence:                #checks the sequence and ensures it is made up of valid nucleotides
        if i in nucleo:
            pass
        else:
            return False
    return True                                        #returns true if no wrong nucleotide is found

def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence:
    :return: The complementary sequence with the T's complementing A and C complementing G and vice verse
    :return: Returns sequencial error is the sequence is not complementary
    """

    complement = ""      # This can be used to "build" the complement

    for i in sequence:
        if i == "G":
            i = "C"
            complement += i
        elif i == "C":
            i = "G"
            complement += i
        elif i == "A":
            i = "T"
            complement += i
        elif i == "T":
            i = "A"
            complement += i
        else:
            return "Sequencing Error"
    return complement



def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence:
    :return: a new mrna strand with the T replaced to nucleotide U
    """
    mrna = ""
    for i in sequence:
        if i == "T":
            i = "U"
            mrna += i
        else:
            mrna += i
    return mrna


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence:
    :return: a list containing pairs of 3 while discarding strings that make it not a multiple of 3
    """

    list_of_chunks = []
    length = len(sequence) % 3
    if length == 0:
        for i in range (0, len(sequence), 3):
           list_of_chunks.append(sequence[i: i + 3])
    elif length != 0:
        for i in range(0, len(sequence) - length, 3):
            list_of_chunks.append(sequence[i: i + 3])

    return list_of_chunks

def amino_acid_chunks(three_char_seq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character AminoAcid

    :param three_char_seq: a sequence of three characters
    :return: A string representing the amino acid chunk for that sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    # We haven't learned about dictionaries yet, but here is one for the extra curious.
    # You aren't expected to know what this is yet.
    translator = {"GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
                  "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
                  "GAC": "D", "GAU": "D",
                  "AAC": "N", "AAU": "N",
                  "UGC": "C", "UGU": "C",
                  "GAA": "E", "GAG": "E",
                  "CAA": "Q", "CAG": "Q",
                  "GGA": "G", "GGC": "G", "GGU": "G", "GGG": "G",
                  "CAC": "H", "CAU": "H",
                  "AUA": "I", "AUC": "I", "AUU": "I",
                  "UUA": "L", "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
                  "AAA": "K", "AAG": "K",
                  "AUG": "M",
                  "UUC": "F", "UUU": "F",
                  "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
                  "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
                  "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
                  "UGG": "W",
                  "UAC": "Y", "UAU": "Y",
                  "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
                  "UAA": "*", "UAG": "*", "UGA": "*"
                 }

    if three_char_seq in translator.keys():
        return translator[three_char_seq]  # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a a sequence of nucleotides:
    A, C, G, and T and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    aaseq=""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = chunk_amino_acid(mrna)            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + amino_acid_chunks(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code

    :return: None
    """
    print("The original sequence {0} returns {1}".format("CACGT", sequence_gene("CACGT")))


if __name__ == "__main__":
    main()          # call to main() function
