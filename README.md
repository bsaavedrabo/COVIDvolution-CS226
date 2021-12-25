# CSC226 Project

**Term**: Fall 2021

**Author(s)**: Daize Njounkeng and Maria Belen Saavedra Rios

❗ indicates action items; you should remove these emoji as you complete/update the items which they accompany. (This means that your final README should have no ❗️in it!)

---

**References**: 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, and describe how you integrated the ideas or code into your program. This includes online sources, people who have helped you, and any other resources that are not solely your own contribution. Update as you go.

---

## Milestone 1: Setup, Planning, Design (due 1 Dec 2021)

**Title**: SARS-COVID-19 Genome Analyzer 

**Purpose**: It transcribes and translates viral genome. It compares COVID-19 strands sequenced in 12 countries with the first COVID-19 Sequence from December 2019.
The objective is to observe SARS-CoV-2 mutations from Dec 2019.

**Sources**: Which assignments or code will you base your project on?
  We are going to base our project on A07: It's in Your Genes and T09 Oh The Places You Will Go 


**CRC Card**:
  - Please write a CRC card for a class that your project will implement.
  - See this link for a sample CRC card and a template to
  use for your own cards (you will have to make a copy to edit): https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing
  - Tables in markdown are not easy, so we suggest saving your CRC card
  as an image and including the image(s) in the README. You can do this
  by saving an image in the repository and linking to it. See the sample CRC card below - and replace it with your own.
  
![alt text](images/DNA_class.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one")
![alt text](images/percent_diff_class.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one")

---

## Milestone 2: Code (due 3 Dec 2021)

No README action items. You should have some code and a preliminary test suite pushed to your repository. 🙃

---

## Milestone 3: Virtual Check-In (due 6 Dec 2021)

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: 75%

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some strategies you can employ to increase the likelihood that you'll be successful in completing this project before the deadline.
We have been making good progress these past week by having in-person meetings and doing some tasks on our own time.
At this point, our program works properly, now we are using t-tinker to make our program interactive. We are going to ensure we finish our project on time by setting up daily goals.

Tasks for the following days:
Tuesday ==> finish adding widgets, revise documentation on readme and code
Wednesday ==> make powerpoint presentation
Thursday ==> prepare speech for the presentation
Friday ==> present @11am!
---

## Milestone 4: Final Code, Presentation, Demo (due 10 Dec 2021)

### User Instructions
In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button. 
Once the user clicks the "Start Analyzing" botton, a world map will pop out. The user should select the COVID sequence they would like to analyze from the 12 available countries. After that, the percentage similarity will pop out in a new window.

### Errors and Constraints
Every program has bugs or features that had to be scrapped for time. Use this section to create a bullet list of all known errors and deficiencies that remain in your code. Bugs found that aren't acknowledged here will be penalized.

Biological limitations:
- Data, the samples have been collected at different times. It would be more accurate to observe the mutation having the same collection date.
- Quality of DNA sequence, we rely on the quality of the DNA sequences
- Comparing the mutations as DNA nucleotides would be better to identify what type of mutations happened in the strands of interest.

Technical limitations:
- We end up having three pages at the end of the execution of the program: the main page, the map and the result page. Our program would be perhaps more user-friendly if we closed the 
main page once the result page is executed.

### Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?

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

#####