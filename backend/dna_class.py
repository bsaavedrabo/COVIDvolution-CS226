# Author(s): Daize Njounkeng and Maria Belen Saavedra Rios
# Username(s): njounkengdaizem and saavedrariosm
# Purpose: The DNA class transcribes and translates genomic sequences
######################################################################
# Acknowledgements:
# Dr. Rosen, Professor of Biology. Dr. Anderson, Professor of Biology and Liberty Mupotsa, Senior CSC major
####################################################################################
class DNA:

    def __init__(self, sequence):
        """
        Initializer method a.k.a. Constructor:
        Holds the classes' attributes
        :param sequence:
        """
        self.sequence = sequence

    def clean_data(self):
        """
              Cleans the DNA sequence, Gets rid of unnecessary letters and spaces
              :return: an mRNA sequence
              :return: Clean DNA sequence ready to be transcribed
              """
        nucleotides = ["A", "T", "C", "G"]             #Valid nucleotides, any other charater is discarded
        clean_seq = ""
        for letter in self.sequence:
            if letter in nucleotides:
                clean_seq = clean_seq + letter
        self.sequence = clean_seq

    def transcription(self):
        """
        Transcribes the DNA sequence into mRNA
        This method is a mix between complement and mRNA in the previous a07 It's on your genes
        :return: an mRNA sequence
        :return: The complementary sequence with the U's complementing A and C complementing G and vice verse
        :return: Returns sequencial error is the sequence is not complementary
        """
        # changes C for G and viceversa and T for A BUT A for U

        complement = ""                     # This can be used to "build" the complement
        self.clean_data()
        for i in self.sequence:
            if i == "G":
                i = "C"
                complement += i
            elif i == "C":
                i = "G"
                complement += i
            elif i == "A":
                i = "U"
                complement += i
            elif i == "T":
                i = "A"
                complement += i
            else:
                print("The letter is", i)
                return "Sequencing Error"
        return complement

    def triplets_aminoacid(self):
        """
        Divides the mRNA into codons which are triplets of mRNA nucleotides
        :return: A list of strings containing triplets of nucleotides ["ACU", "UGC"]
        """
        seq_transcribed = self.transcription()
        list_of_codons = []
        length = len(seq_transcribed) % 3                #Splits the strands in pairs of three
        if length == 0:
            for i in range(0, len(seq_transcribed), 3):
                list_of_codons.append(seq_transcribed[i: i + 3])
        elif length != 0:
            for i in range(0, len(seq_transcribed) - length, 3):
                list_of_codons.append(seq_transcribed[i: i + 3])

        return list_of_codons

    def aminoacid_chunks(self):
        """
        Translates the sequence of mRNA to amino acid
        :return: Chunks of amino acids
        """
        # Use a dictionary to map the key (triplets) and value(amino acid)
        # returns the sequence of aminoacids as a list ["A","V","L","B"]
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
        list_of_aminoacids = []
        for i in self.triplets_aminoacid():

            if i in translator.keys():
                list_of_aminoacids.append(
                    translator[i])  # Given any 3 letter sequence, this returns the amino acid for that sequence
            else:
                return "Oops Something went wrong. Check that you didn't delete a nucleotide"  # Returns a question mark if the input is invalid
        return list_of_aminoacids