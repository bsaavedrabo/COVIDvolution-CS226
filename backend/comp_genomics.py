# Author(s): Daize Njounkeng and Maria Belen Saavedra Rios
# Username(s): njounkengdaizem and saavedrariosm
#
# Purpose: A class that prepares sequences of DNA to be analyzed.
######################################################################
# Acknowledgements:
# Dr. Rosen, Professor of Biology. Dr. Anderson, Professor of Biology and Liberty Mupotsa
####################################################################################

from backend.percent_diff import *
from backend.dna_class import *


def comparative_genome(file):
    # OPENING WUHAN
    opening_file = open("../sequences/sequence.china.wuhan1.txt", "r")
    line = opening_file.read()
    wuhan_list = []
    for each in line:
        if each != "\n":
            wuhan_list = wuhan_list + [each]  # getting rid of the /n character
    opening_file.close()

    # OPENING THE SEQUENCE TO COMPARE
    opening_file = open(file, "r")
    sequence_choice = opening_file.read()
    opening_file.close()
    # Translating and transcribing sequence
    strand_A = DNA(sequence_choice)
    sequence_to_compare = strand_A.aminoacid_chunks()

    # Using the percentage difference class
    comparison = percent_difference(wuhan_list, sequence_to_compare)
    print("{}%".format(comparison.sequ_differ()))
    return comparison
