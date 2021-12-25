# Author(s): Daize Njounkeng and Maria Belen Saavedra Rios
# Username(s): njounkengdaizem and saavedrariosm
######################################################################
# Purpose: A test suite to test the two classes in our program
######################################################################
# Acknowledgements:
# Youtube, Google and Liberty
######################################################################
import turtle
from backend.comp_genomics import comparative_genome
from tkinter import *
from tkinter import ttk


def getxy(x, y):
    opening = 0
    results = ""

    if (-3 < x < 15) and (14.0 < y < 38.0):
        opening = comparative_genome("../sequences/sequence.benin.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Benin: " + str(opening) +
                             "% \n Nuc Completeness: Complete  \n Collection "
                             "Date: 15-3-2020 \n Host: Homo Sapiens \n Mol Type: RNA")

    if (366 < x < 390) and (-61 > y > -80):
        opening = comparative_genome("../sequences/sequence.australia.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Australia: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 21-08-2020 \n Host: Homo Sapiens \n "
                             "Mol Type: RNA")
    if (331 < x < 353) and (30 < y < 47):
        opening = comparative_genome("../sequences/sequence.phillippines.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Philippines: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 21-04-2021 \n Host: Homo Sapiens \n "
                             "Mol Type: RNA")

    if (77 < x < 100) and (63 < y < 83):
        opening = comparative_genome("../sequences/sequence.egypt.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Egypt: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 23-10-2021 \n Host: Homo Sapiens \n "
                             "Mol Type: RNA")

    if (29 < x < 47) and (105 < y < 122):
        opening = comparative_genome("../sequences/sequence.italy.txt")
        results = results + (" RESULTS OF COMPARISON \n\n Wuhan vs Italy: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 01-03-2020 \n Host: Homo Sapiens \n "
                             "Mol Type: RNA")

    if (143 < x < 162) and (82 < y < 96):
        opening = comparative_genome("../sequences/sequence.iran.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Iran: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 28-04-2020\n Host: Homo Sapiens \n "
                             "Mol Type: RNA")

    if (290 < x < 307) and (161 < y < 175):
        opening = comparative_genome("../sequences/sequence.russia.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Russia: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 04-21-2020\n Host: Homo Sapiens \n "
                             "Mol Type: RNA")
    if (60 < x < 73) and (-73 > y > -93):
        opening = comparative_genome("../sequences/sequence.southafrica.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs South Africa: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 16-11-2020 \n Host: Homo Sapiens \n "
                             "Mol Type: RNA")

    if (-155 > x > -177) and (-82 > y > -100):
        opening = comparative_genome("../sequences/sequence.argentina.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Argentina: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 14-09-2020\n Host: Homo Sapiens \n "
                             "Mol Type: RNA")

    if (-137 > x > -157) and (-27 > y > -50):
        opening = comparative_genome("../sequences/sequence.brazil.txt")
        results = results + ("RESULTS OF COMPARISON \n\n Wuhan vs Brazil: " + str(opening) +
                             "% \n Nuc Completeness: Complete \n Collection Date: 15-03-2021 \n Host: Homo Sapiens \n "
                             "Mol Type: RNA")

    if (-211 > x > -230) and (40 < y < 60):
        opening = comparative_genome("../sequences/sequence.jamaica.txt")
        results = results + (
                " RESULTS OF COMPARISON \n\n Wuhan vs Jamaica: " + str(opening) +
                "% \n Nuc Completeness: Complete \n Collection Date: 03-09-2020 \n Host: Homo Sapiens \n Mol "
                "Type: RNA")

    if (-227 > x > -250) and (94 < y < 110):
        opening = comparative_genome("../sequences/sequence.kentucky.txt")
        results = results + (
                "RESULTS OF COMPARISON \n\n Wuhan vs Kentucky: " + str(opening) +
                "% \n Nuc Completeness: Complete \n Collection Date: 06-11-2021\n Host: Homo Sapiens \n Mol Type: "
                "RNA")

    if opening != 0:
        # Create an instance of Tkinter Frame
        win = Tk()
        # Set the geometry of Tkinter Frame
        win.geometry("300x300")
        win.title("Sequencing Results...")

        # Define a function for exit
        def exit_program():
            win.destroy()

        # Add a canvas widget
        canvas = Canvas(win, width=500)

        # Add a Label widget in the Canvas
        label = Label(canvas, text=results, font='Helvetica 10 bold')
        label.pack(pady=60)

        # Create a button in canvas widget
        ttk.Button(canvas, text="Exit", command=exit_program).pack()
        canvas.pack()

        win.mainloop()


def parse_file(filename):
    """
    Iterates through the file, and creates the list of places
    :param filename: the name of the file to be opened
    :return: a list representing multiple places
    """
    file_content = open(filename, 'r')  # Opens file for reading
    str_num = file_content.readline()  # The first line of the file, which is the number of entries in the file
    str_num = int(str_num[:-1])  # The '/n' character needs to be removed
    places_list = []
    for i in range(str_num):
        places_list.append(extract_place(file_content))  # Assembles the list of places
    file_content.close()
    return places_list


def place_pin(window, place):
    """
    This function places a pin on the world map.
    :param window: the window object where the pin will be placed
    :param place: a tuple object describing a place to be put on the map
    :return: None
    """
    pin = turtle.Turtle()
    pin.penup()
    if len(place) == 5:
        pin.color(place[4])  # Set the pin to user's chosen color
    pin.shape("circle")  # Sets the pin to a circle shape
    if len(place) == 5:
        pin.goto((place[3] / 195) * window.window_width() / 2, (place[2] / 120) * window.window_height() / 2)
    pin.stamp()  # Stamps on the location
    text = "Unknown place"
    if len(place) == 5:
        text = "{0}\n    {1}".format(place[0], place[1])  # Setting up pin label
    pin.write(text, font=("Arial", 10, "bold"))  # Stamps the text describing the location


def extract_place(file_content):
    """
    This function extracts five lines out of file_content,
    which is a variable holding all of the file content from the calling function. Each extracted line represents,
    in order, the place's name, Location, latitude, longitude, and user color. The function returns the five elements
    to the function call as a tuple.
    :param file_content: contents of the file which represents all places
    :return: a tuple representing a single place.
    """
    # removing the last character \n in name, location, latitude, longitude and user_color
    name = file_content.readline().strip("\n")
    location = file_content.readline().strip("\n")
    latitude = file_content.readline().strip("\n")
    longitude = file_content.readline().strip("\n")
    user_color = file_content.readline().strip("\n")

    # Constructed a tuple with all five values in the correct order.
    place_tuple = (name, location, float(latitude), float(longitude), user_color)  # Finished assembling the tuple
    return place_tuple  # return the different locations as tuples


def execute():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a tuple.
    Each tuple is then added to a list.
    The list of tuples is used to populate the map.

    :return: None
    """
    # The next three lines set up the world map

    wn = turtle.Screen()
    wn.setup(width=1100, height=650, startx=0, starty=0)
    wn.bgpic("world-map.gif")
    wn.title("SARS-COVID-19 Genome Analyzer")
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(-400, 280)
    turtle.pendown()
    turtle.write("Please Click On A Location To Compare With The COVID Strand From Wuhan China",
                 font=("Arial", 16, "normal"))
    wn.onclick(getxy)
    place_list = parse_file("countries.txt")  # generates place_list from the file

    # Iterates through each item in the place_list list, calling the place_pin() function
    for place in place_list:
        place_pin(wn, place)  # Adds ONE place to the map for each loop iteration

    print("Map created!")
    wn.mainloop()
