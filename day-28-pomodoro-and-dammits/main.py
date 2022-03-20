import tkinter
import os

os.chdir(os.path.dirname(__file__))

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
#GREEN = "#9bdeac"
GREEN = "#029b00"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BLUE = "#d8e6f3"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text= f"{WORK_MIN}:00")
    canvas.itemconfigure(1, state='normal')
    canvas.itemconfigure(2, state='hidden')
    canvas.itemconfigure(3, state='hidden')
    canvas.itemconfigure(4, state='hidden')
    checkmark_label.config(text="")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0

def bromato_working():
    canvas.itemconfigure(1, state='normal')
    canvas.itemconfigure(2, state='normal')
    canvas.itemconfigure(3, state='hidden')
    canvas.itemconfigure(4, state='hidden')

def bromato_break():
    canvas.itemconfigure(1, state='hidden')
    canvas.itemconfigure(2, state='hidden')
    canvas.itemconfigure(3, state='normal')
    canvas.itemconfigure(4, state='normal')


def start_timer():
    global reps 
    reps += 1
    
    if reps % 8 == 0:
        bromato_break()
        checkmarks = "✔" * math.floor((reps + 1)/2)
        checkmark_label.config(text=checkmarks)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        bromato_break()
        checkmarks = "✔" * math.floor((reps + 1)/2)
        checkmark_label.config(text=checkmarks)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        bromato_working()
        countdown(WORK_MIN * 60)

        
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math

def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text= f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        start_timer()


    


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=BLUE, highlightthickness=0)

canvas = tkinter.Canvas(width=350, height=350, bg= BLUE, highlightthickness=0)

tomato_img = tkinter.PhotoImage(file="bad_bromato.png")
sleeping_tomato_img = tkinter.PhotoImage(file="bad_bromato_sleeping.png")

working_img = tkinter.PhotoImage(file="working.png")
taking_break_img = tkinter.PhotoImage(file="break2.png")

canvas.create_image(197,190,image=tomato_img)

canvas.create_image(298,85,image=working_img)
canvas.itemconfigure(2, state='hidden')


canvas.create_image(171,190,image=sleeping_tomato_img)
canvas.itemconfigure(3, state='hidden')

canvas.create_image(295,85,image=taking_break_img)
canvas.itemconfigure(4, state='hidden')


timer_text = canvas.create_text(165,30,text= f"{WORK_MIN}:00", fill='black', font=("Arial",35,"bold"))

canvas.grid(column=1, row=1)

#Start Timer Button
start_timer_button = tkinter.Button(text="Start Timer", width= 11, command= start_timer)
start_timer_button.grid(column=0, row=2)
#start_timer_button.config(padx=10,pady=10)

#Reset Button
reset_button = tkinter.Button(text="Reset", command= reset, width =8)
reset_button.grid(column=2, row=2)
#reset_button.config(padx=10,pady=10)


#Check Mark
checkmark_label = tkinter.Label(text="", bg= BLUE, fg= GREEN, font=('Arial', 12,'normal'))
checkmark_label.grid(column= 1, row= 2)

window.mainloop()