import tkinter
import os
import pandas as pd
import random

os.chdir(os.path.dirname(__file__))

BACKGROUND_COLOR = "#B1DDC6"

name = input("What is your first and last name?").lower().replace(" ", "")



try:
    df = pd.read_csv(f"C:/Users/jared/GitHub/continued-ed/100-Days-of-Python/day-31-flash-cards/data/{name}_words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv(f"C:/Users/jared/GitHub/continued-ed/100-Days-of-Python/day-31-flash-cards/data/spanish_words.csv")
    words_remaining = df.to_dict(orient='records')
else:
    words_remaining = df.to_dict(orient='records')


current_card = {}
english_face_up = False


def new_flashcard():
    global current_card, english_face_up
    current_card = random.choice(words_remaining)
    english_face_up = False
    canvas.itemconfigure(flashcard_title, text="Spanish", fill= 'black')
    canvas.itemconfigure(flashcard_word, text= current_card['Spanish'], fill= 'black')
    canvas.itemconfigure(card_background, image=front_card_img)

def flip_card():
    global english_face_up
    english_face_up = not english_face_up
    if english_face_up == True:  
        canvas.itemconfigure(flashcard_title, text='English', fill='white')
        canvas.itemconfigure(flashcard_word, text=current_card["English"], fill='white')
        canvas.itemconfigure(card_background, image=back_card_img)
    
    elif english_face_up == False:
        canvas.itemconfigure(flashcard_title, text='Spanish', fill='black')
        canvas.itemconfigure(flashcard_word, text=current_card["Spanish"], fill='black')
        canvas.itemconfigure(card_background, image=front_card_img)


def is_known():
    global current_card, words_remaining
    words_remaining.remove(current_card)
    df = pd.DataFrame(words_remaining)
    df.to_csv(f'C:/Users/jared/GitHub/continued-ed/100-Days-of-Python/day-31-flash-cards/data/{name}_words_to_learn.csv', index=False)
    new_flashcard()

window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = tkinter.PhotoImage(file=r"C:\Users\jared\GitHub\continued-ed\100-Days-of-Python\day-31-flash-cards\images\card_front.png")
back_card_img = tkinter.PhotoImage(file=r"C:\Users\jared\GitHub\continued-ed\100-Days-of-Python\day-31-flash-cards\images\card_back.png")
card_background= canvas.create_image(400, 263, image= front_card_img)
flashcard_title= canvas.create_text(400,150, text= '', font=('Ariel', 40,'italic'))
flashcard_word= canvas.create_text(400,263, text= '', font=('Ariel', 60,'bold'))
canvas.grid(row=0, column = 0, columnspan=3)

wrong_image = tkinter.PhotoImage(file= r'C:\Users\jared\GitHub\continued-ed\100-Days-of-Python\day-31-flash-cards\images\wrong.png')
wrong_button = tkinter.Button(image=wrong_image, command=new_flashcard, width= None)
wrong_button.grid(row=1,column=0)

flip_image = tkinter.PhotoImage(file= r'C:\Users\jared\GitHub\continued-ed\100-Days-of-Python\day-31-flash-cards\images\flip.png')
flip_button = tkinter.Button(image=flip_image, command=flip_card, width= None)
flip_button.grid(row=1,column=1)

right_image = tkinter.PhotoImage(file= r'C:\Users\jared\GitHub\continued-ed\100-Days-of-Python\day-31-flash-cards\images\right.png')
right_button = tkinter.Button(image=right_image, command=is_known, width = None)
right_button.grid(row=1,column=2)





new_flashcard()


window.mainloop()