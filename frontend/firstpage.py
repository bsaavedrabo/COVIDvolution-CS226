# Author(s): Daize Njounkeng and Maria Belen Saavedra Rios
# Username(s): njounkengdaizem and saavedrariosm
######################################################################
# Purpose: A test suite to test the two classes in our program
######################################################################
# Acknowledgements:
# Youtube, Google and Liberty
######################################################################
import tkinter as tk
from PIL import Image, ImageTk
from tkinter_map import execute

# creating window
first_page = tk.Tk()  # instance
first_page.title("Intro to COVIDvolution")  # adding title page
first_page.iconbitmap("logo_asicon.ico")  # setting the icon for the page
canvas = tk.Canvas(first_page, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo in main page
logo = Image.open("../images/logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# text below the logo and above the start botton
text = tk.Label(first_page, text="How much has COVID-19 changed since December 2019?", font="Aharoni")
text.grid(columnspan=3, column=0, row=1)
botton_text = tk.StringVar()
button_btn = tk.Button(first_page, textvariable=botton_text, command=lambda: execute(), font="Raleway", bg="#20bebe",
                       fg="white", height=2, width=15)
botton_text.set("Start Analyzing")
button_btn.grid(column=1, row=2)

# changing window size
canvas = tk.Canvas(first_page, width=600, height=250)
canvas.grid(columnspan=3)

first_page.mainloop()
