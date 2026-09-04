import random

import pandas
from pandas.errors import EmptyDataError

current_data={}
data_dict={}
try:
    data=pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/states.csv")
    data_dict = original_data.to_dict(orient="records")
except EmptyDataError:
    original_data = pandas.read_csv("data/states.csv")
    data_dict = original_data.to_dict(orient="records")


else:
    data_dict = data.to_dict(orient="records")
#displaying State
def next_button():
    global current_data,flip_timer
    window.after_cancel(flip_timer)
    current_data=random.choice(data_dict)
    canvas.itemconfig(title_word,text="State",fill="black")
    canvas.itemconfig(text_word,text=current_data["State"],fill="black")
    canvas.itemconfig(background_img,image=card_front_img)
    flip_timer=window.after(3000,flip_card)

 #flip card to capital
def flip_card():
    canvas.itemconfig(title_word,text="Capital",fill="white")
    canvas.itemconfig(text_word,text=current_data["Capital"],fill="white")
    canvas.itemconfig(background_img,image=card_back_img)
def restart_game():
    global data_dict

    original_data = pandas.read_csv("data/states.csv")
    data_dict = original_data.to_dict(orient="records")

    next_button()
def check_card():
    data_dict.remove(current_data)
    print(len(data_dict))
    data=pandas.DataFrame(data_dict)
    data.to_csv("data/to_learn.csv",index=False)
    if len(data_dict) > 0:
        next_button()
    else:
        canvas.itemconfig(title_word, text="Finished!")
        canvas.itemconfig(text_word, text="Restart the game")



from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

# Setting up Window
window=Tk()
window.configure(padx=50,pady=50,background=BACKGROUND_COLOR)
flip_timer=window.after(3000,flip_card)
canvas=Canvas(width=800,height=526)

card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
background_img=canvas.create_image(400,263,image=card_front_img)
title_word=canvas.create_text(400,150,text="State",font=("Arial", 50, "italic"),fill="black")
text_word=canvas.create_text(400,300,text="Capital",font=("Arial", 70, "italic"),fill="black")
canvas.config(highlightthickness=0,background=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2)
wrong_button_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_button_img,highlightthickness=0,background=BACKGROUND_COLOR,command=next_button)
wrong_button.grid(row=1,column=0)
right_button_img=PhotoImage(file="images/right.png")
right_button=Button(image=right_button_img,highlightthickness=0,background=BACKGROUND_COLOR,command=check_card)
right_button.grid(row=1,column=1)
right_button.grid(row=1,column=1)

canvas.grid(row=0,column=0)
next_button()
window.mainloop()