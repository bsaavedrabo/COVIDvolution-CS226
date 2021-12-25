# Author(s): Daize Njounkeng and Maria Belen Saavedra Rios
# Username(s): njounkengdaizem and saavedrariosm
######################################################################
# Purpose: A test suite to test the two classes in our program
######################################################################
# Acknowledgements:
# Youtube, Google and Liberty
######################################################################

import sys
from dna_class import *
from percent_diff import *


def testit(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def DNA_test_suite():
    """
    The DNA_test_suite() is designed to test the following:
      transciption()
      chunk_aminoacid()
      aminoacid_chunks()

    :return: None
    """
    # Instances of the class
    strand1 = DNA("GATCTGTTCTCTAAACGAACTTTAAAATCTGT")
    strand2 = DNA("AATAAAGGAGCTGGT")
    strand3 = DNA("CGAACTGCAC")
    strand4 = DNA("AGTTGAAAAAGGCGTTTTGCCT")
    strand5 = DNA("TAGGCGACGAGCTTGGCACT")

    # The following tests test the origin() method
    print("\nTesting transcription()")
    testit(strand1.transcription() == "CUAGACAAGAGAUUUGCUUGAAAUUUUAGACA")
    testit(strand2.transcription() == "UUAUUUCCUCGACCA")
    testit(strand3.transcription() != "CGAACTGCAC")
    testit(strand4.transcription() != "UCAACUUUUUCCGCAAAACGGA")  # test for a failed case
    testit(strand5.transcription() == "AUCCGCUGCUCGA5CCGUGA")  # test for a failed case

    # The following tests test the triplets_aminoacid() method
    print("\nTesting triplets_aminoacid()")
    testit(strand1.triplets_aminoacid() == ['CUA', 'GAC', 'AAG', 'AGA', 'UUU', 'GCU', 'UGA', 'AAU', 'UUU', 'AGA'])
    testit(strand2.triplets_aminoacid() == ['UUA', 'UUU', 'CCU', 'CGA', 'CCA'])
    testit(strand3.triplets_aminoacid() == ['UUA', 'UUU', 'CCU', 'CGA'])  # test for a failed case
    testit(strand4.triplets_aminoacid() != '')
    testit(strand5.triplets_aminoacid() != ['AUC', 'CGC', 'UGC', 'UCG', 'AAC', 'CGU'])  # test for a failed case)

    # The following tests test the aminoacid_chunks() method
    print("\nTesting aminoacid_chunks()")
    testit(strand1.aminoacid_chunks() == ['L', 'D', 'K', 'R', 'F', 'A', '*', 'N', 'F', 'R'])
    testit(strand2.aminoacid_chunks() == ['L', 'F', 'P', 'R', 'P'])
    testit(strand3.aminoacid_chunks() == ['A', '*', 'R'])
    testit(strand4.aminoacid_chunks() != ['S', 'T', 'F', 'S', 'A', 'K', 'R'])  # test for a failed case
    testit(strand5.aminoacid_chunks() == '')  # test for a failed case


def percent_diff_test_suite():
    """
     The DNA_test_suite() is designed to test the following:
       count_amino()
       compare()
       display()

     :return: None
     """
    strain1 = ['L', 'S', 'Q', 'L', 'F', 'P', 'Q', 'N', 'G', 'Q']
    strain2 = ['L', 'S', 'Q', 'L', '#', 'P', 'Q', 'N', 'G', '']
    strain3 = ['S', 'T', 'F', 'S', 'A', 'K', 'R']
    strain4 = ['L', 'F', 'P', 'R', 'P']
    strand1 = percent_difference(strain1, strain2)
    strand2 = percent_difference(strain3, strain4)
    strand3 = percent_difference(strain1, strain3)
    strand4 = percent_difference(strain2, strain4)

    print("\nTesting sequ_similar()")
    testit(strand1.sequ_differ() == "10.00")
    testit(strand2.sequ_differ() == "71.43")
    testit(strand4.sequ_differ() == "40.00")
    testit(strand4.sequ_differ() != "40.0")
    testit(strand3.sequ_differ() != 70.00)
    testit(strand4.sequ_differ() != "10.00")  # test for a failed case
    testit(strand1.sequ_differ() == 10.00)  # test for a failed case
    testit(strand3.sequ_differ() == "0.00")  # test for a failed case


def main():
    DNA_test_suite()  # Calling the DNA test suite
    percent_diff_test_suite()  # Calling the Percentage Difference test suite


main()
