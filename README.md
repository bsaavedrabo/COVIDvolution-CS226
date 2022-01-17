# CSC226 Final Project

**Term**: Fall 2021

**Author(s)**: Daize Njounkeng and Maria Belen Saavedra Rios

**References**: 
We were inspired by two assignments (A07 and T09) from the class CSC 226: Software Implementation and Design at Berea College.
---

**SARS-COVID-19 Genome Analyzer**

**Purpose**: It transcribes and translates viral genome. It compares COVID-19 strands sequenced in 12 countries with the first COVID-19 Sequence from December 2019.
The objective is to observe SARS-CoV-2 mutations from Dec 2019.

**CRC Cards**:

![alt text](images/DNA_class.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one")
![alt text](images/percent_diff_class.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one")

### User Instructions
Once the user clicks the "Start Analyzing" botton, a world map will pop out. The user should select the COVID sequence they would like to analyze from the 12 available countries. After that, the percentage similarity will pop out in a new window.

### Errors and Constraints

Biological limitations:
- Data, the samples have been collected at different times. It would be more accurate to observe the mutation having the same collection date.
- Quality of DNA sequence, we rely on the quality of the DNA sequences
- Comparing the mutations as DNA nucleotides would be better to identify what type of mutations happened in the strands of interest.

Technical limitations:
- We end up having three pages at the end of the execution of the program: the main page, the map and the result page. Our program would be perhaps more user-friendly if we closed the 
main page once the result page is executed.

### Reflection

It is fascinating that we can replicate biological 
processes to understand more intriguing questions such as: how much 
coronavirus has changed since December 2019? 
Understanding this virus' rapid mutations could help scientists to
develop vaccines more rapidly. Our current design is specifically targeted at 
COVID-19 analysis. 

We started, however, with the idea of creating a program that 
compares two organisms from different species. Due to time constraints and 
bioinformatics experience, we made a program that identifies the differences 
of different COVID DNA sequences.

We learned more about the application of OOP: using tkinter and classes effectively and 
also we were able to practice pair programming effectively.

Some major challenges we faced while doing this task 
was implementing the tkinter because we did not have previous experience implementing GUI
on our programs.
Another big challenge we faced was trying to simulate with precision biological processes 
like transcription and translation. We have realized that molecular processes are way more 
difficult (but exciting) to simulate computationally. Dr. Rosen and Dr. Anderson from the 
Biology Department guided us to improve our project.

Some future steps for our program is to identify the type of mutation between the two strands 
in the DNA level, also in a future opportunity, we can use genomic databases from other organisms.

We have learned through this program where to get the right resources and we plan
to use them in the future. 

Thank you!

Belen and Daize
#####
