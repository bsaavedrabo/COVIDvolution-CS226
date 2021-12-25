# Author(s): Daize Njounkeng and Maria Belen Saavedra Rios
# Username(s): njounkengdaizem and saavedrariosm
# Purpose: A class that performs an statistical test that calculates the percent difference between two nucleotide sequences
######################################################################
# Acknowledgements:
# Youtube, Google and Liberty, Senior CSC major
####################################################################################
def compare(a, b, c):  # Helper Function used in sequ_differ method in the class percent_similar
    accu = 0
    for i in range(len(a) - 1):
        if a[i] != b[i]:
            accu += 1
        else:
            pass
    diff = (accu / c) * 100  # calculate the percentage
    difference = "{:.2f}".format(diff)
    return difference  # returns the number of similar bases


class percent_difference:

    def __init__(self, sequence1, sequence2, differ=0):
        """
         Initialize an amino acid sequence
        :param A,A,R,D,N,C,E,Q,G,H,I,L,K,M,F,P,S,T,W,Y,V,Z: Sequence of amino acid
        """
        self.wuhan_seq = sequence1  # this is our constant strain
        self.sequence2 = sequence2
        self.differ = differ

    def sequ_differ(self):
        """
        Cuts sequence 2 to the length of sequence1(Wuhan1) OR
        cut Wuhan1 sequence to the length of sequence2 depending on which is longer
        Calls the helper function "compare" to find the difference between the two sequences
        :return: sequence 2 clean, ready for analysis
        """
        sequence1_len = len(self.wuhan_seq)  # this sequence will always be Wuhan1
        sequence2_len = len(self.sequence2)
        if sequence1_len > sequence2_len:
            denum = sequence1_len
        elif sequence2_len > sequence1_len:
            denum = sequence2_len
        else:
            denum = sequence1_len
        sequence1_clean = self.wuhan_seq[:]
        sequence2_clean = self.sequence2[:]
        if sequence2_len < sequence1_len:  # compare the lengths of both strands and returns the shortest
            sequence1_clean = self.wuhan_seq[:sequence2_len + 1]
            # return sequence1_clean
        elif sequence2_len > sequence1_len:
            sequence2_clean = self.sequence2[:sequence1_len + 1]  #
            # return sequence2_clean
        else:
            pass
        self.differ = compare(sequence1_clean, sequence2_clean, denum)
        return self.differ

    def __str__(self):
        return str(self.differ)
