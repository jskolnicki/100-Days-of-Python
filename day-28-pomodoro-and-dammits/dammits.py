import tkinter
import os
import pandas as pd
import datetime
import csv

os.chdir(os.path.dirname(__file__))

window = tkinter.Tk()
window.title("Dammit Counter")

#variables
dammits_db = pd.read_csv("dammits.csv")
dammits_db['Week'] = pd.to_datetime(dammits_db['Week'])


today = datetime.date.today()

today = today + datetime.timedelta(days= 2)

start_of_week = pd.to_datetime(dammits_db['Week'].to_list()[-1])

current_week_index = int(dammits_db['Week'][dammits_db['Week'] == start_of_week].index[0])

num_of_yikes = dammits_db.iloc[current_week_index, 1]
num_of_dammits = dammits_db.iloc[current_week_index, 2]

#FUNCTIONS



def increase_dammits():
    global current_week_index, dammits_db
    with open("dammits.csv") as f:
        reader = csv.reader(f)
        data = list(reader)
    
    data[current_week_index + 1][2] = int(data[current_week_index + 1][2]) + 1
    
    with open("dammits.csv", "w", newline = "") as f: 
        a = csv.writer(f)
        for row in data:
            a.writerow(row)
    
    dammits_db = pd.read_csv("dammits.csv")
    dammits_db['Week'] = pd.to_datetime(dammits_db['Week'])

    update_board()

def decrease_dammits():
    global current_week_index, dammits_db
    with open("dammits.csv") as f:
        reader = csv.reader(f)
        data = list(reader)
    
    data[current_week_index + 1][2] = int(data[current_week_index + 1][2]) - 1
    
    with open("dammits.csv", "w", newline = "") as f: 
        a = csv.writer(f)
        for row in data:
            a.writerow(row)
    
    dammits_db = pd.read_csv("dammits.csv")
    dammits_db['Week'] = pd.to_datetime(dammits_db['Week'])

    update_board()

def increase_yikes():
    global current_week_index, dammits_db
    with open("dammits.csv") as f:
        reader = csv.reader(f)
        data = list(reader)
    
    data[current_week_index + 1][1] = int(data[current_week_index + 1][1]) + 1
    
    with open("dammits.csv", "w", newline = "") as f: 
        a = csv.writer(f)
        for row in data:
            a.writerow(row)
    
    dammits_db = pd.read_csv("dammits.csv")
    dammits_db['Week'] = pd.to_datetime(dammits_db['Week'])

    update_board()

def decrease_yikes():
    global current_week_index, dammits_db
    with open("dammits.csv") as f:
        reader = csv.reader(f)
        data = list(reader)
    
    data[current_week_index + 1][1] = int(data[current_week_index + 1][1]) - 1
    
    with open("dammits.csv", "w", newline = "") as f: 
        a = csv.writer(f)
        for row in data:
            a.writerow(row)
    
    dammits_db = pd.read_csv("dammits.csv")
    dammits_db['Week'] = pd.to_datetime(dammits_db['Week'])

    update_board()

def update_board():
    global current_week_index
    num_of_yikes = dammits_db.iloc[current_week_index, 1]
    num_of_yikes_label.config(text=f"{num_of_yikes}")
    num_of_dammits = dammits_db.iloc[current_week_index, 2]
    num_of_dammits_label.config(text=f"{num_of_dammits}")
    week_of_label.config(text=f"{dammits_db.iloc[current_week_index,0].strftime('%m/%d/%Y')} - {(dammits_db['Week'][current_week_index] + datetime.timedelta(days=6)).strftime('%m/%d/%Y')}")
    if current_week_index == 0:
        previous_week_button.grid_remove()
    elif (current_week_index == len(dammits_db['Week'])-1) and (pd.Timestamp(today - datetime.timedelta(days= 7)) < dammits_db['Week'].to_list()[-1]):
        next_week_button.grid_remove()
    else:
        previous_week_button.grid()
        next_week_button.grid()
    print(f"Current week index: {current_week_index}")
    print(f"Total number of weeks: {len(dammits_db['Week'])-1}")

def next_week():
    global current_week_index, num_of_dammits, num_of_dammits_label, num_of_yikes, num_of_yikes_label, start_of_week, week_of_label, dammits_db
    print("")
    print(f"current week index: {current_week_index}")
    print(f"start_of_week: {start_of_week}")
    print("")
    if current_week_index < len(dammits_db['Week'])-1:
        current_week_index += 1
        num_of_yikes = dammits_db.iloc[current_week_index, 1]
        num_of_dammits = dammits_db.iloc[current_week_index, 2]
        update_board()

    elif pd.Timestamp(today - datetime.timedelta(days= 7)) >= dammits_db['Week'].to_list()[-1]:
        with open('dammits.csv', 'a', newline = "") as file:
            writer_object = csv.writer(file)
            date_to_append = (pd.to_datetime(today + datetime.timedelta(days=-today.weekday())).strftime('%Y-%m-%d'))
            writer_object.writerow([date_to_append,0,0])
            file.close()
            dammits_db = pd.read_csv("dammits.csv")
            dammits_db['Week'] = pd.to_datetime(dammits_db['Week'])
            current_week_index += 1
            num_of_yikes = dammits_db.iloc[current_week_index, 1]
            num_of_dammits = dammits_db.iloc[current_week_index, 2]
            update_board()
            # num_of_yikes = dammits_db.iloc[current_week_index, 1]
            # num_of_yikes_label.config(text=f"{num_of_yikes}")
            # num_of_dammits = dammits_db.iloc[current_week_index, 2]
            # num_of_dammits_label.config(text=f"{num_of_dammits}")
            # week_of_label.config(text=f"{dammits_db.iloc[current_week_index,0].strftime('%m/%d/%Y')} - {(dammits_db['Week'][current_week_index] + datetime.timedelta(days=6)).strftime('%m/%d/%Y')}")

def previous_week():
    global current_week_index, num_of_dammits, num_of_yikes, num_of_yikes_label, num_of_dammits_label
    if current_week_index > 0:
        current_week_index -= 1
        num_of_yikes = dammits_db.iloc[current_week_index, 1]
        num_of_dammits = dammits_db.iloc[current_week_index, 2]
        update_board()
        # num_of_yikes = dammits_db.iloc[current_week_index, 1]
        # num_of_yikes_label.config(text=f"{num_of_yikes}")
        # num_of_dammits = dammits_db.iloc[current_week_index, 2]
        # num_of_dammits_label.config(text=f"{num_of_dammits}")
        # week_of_label.config(text=f"{dammits_db.iloc[current_week_index,0].strftime('%m/%d/%Y')} - {(dammits_db['Week'][current_week_index] + datetime.timedelta(days=6)).strftime('%m/%d/%Y')}")


#print(f"Test: {pd.to_datetime(start_of_week + datetime.timedelta(days=6)).strftime(('%m/%d/%Y'))}")
print(f"Test: {(start_of_week + datetime.timedelta(days=6)).strftime('%m/%d/%Y')}")

#WEEKLY ROW
previous_week_button = tkinter.Button(text="⟵", width= 11, command= previous_week)
previous_week_button.grid(column=0, row=0)

week_of_label = tkinter.Label(text=f"{start_of_week.strftime('%m/%d/%Y')} - {(start_of_week + datetime.timedelta(days=6)).strftime('%m/%d/%Y')}", font=('Arial', 18,'bold'))
week_of_label.config(padx=40, pady=50)
week_of_label.grid(column=1, row=0)

next_week_button = tkinter.Button(text="⟶", width= 11, command= next_week)
next_week_button.grid(column=2, row=0)
if pd.Timestamp(today - datetime.timedelta(days= 7)) < dammits_db['Week'].to_list()[-1]:
    next_week_button.grid_remove()

#DAMMITS ROW
decrease_dammits_button = tkinter.Button(text="-", width= 5, command= decrease_dammits)
decrease_dammits_button.grid(column=0, row=1)

dammits_label = tkinter.Label(text=f"DAMMITS", font=('Arial', 35,'normal'))
dammits_label.config(pady=30)
dammits_label.grid(column= 1, row=1)

increase_dammits_button = tkinter.Button(text="+", width= 5, command= increase_dammits)
increase_dammits_button.grid(column=2, row=1)

num_of_dammits_label = tkinter.Label(text=f"{num_of_dammits}", font=('Arial', 35,'normal'))
num_of_dammits_label.config(padx=20)
num_of_dammits_label.grid(column= 3, row= 1)

#YIKES ROW

decrease_yikes_button = tkinter.Button(text="-", width= 5, command= decrease_yikes)
decrease_yikes_button.grid(column=0, row=2)

# canvas = tkinter.Canvas(width=400, height=128, highlightthickness=0)
# yikes_label = tkinter.PhotoImage(file="yikes.png")
# canvas.create_image(258/2+200,64,image=yikes_label)
# canvas.grid(columns=2,rows=3)

yikes_label = tkinter.Label(text=f"YIKES", font=('Arial', 35,'normal'))
yikes_label.config(pady=30)
yikes_label.grid(column= 1, row=2)

increase_yikes_button = tkinter.Button(text="+", width= 5, command= increase_yikes)
increase_yikes_button.grid(column=2, row=2)

num_of_yikes_label = tkinter.Label(text=f"{num_of_yikes}", font=('Arial', 35,'normal'))
num_of_yikes_label.config(padx=20)
num_of_yikes_label.grid(column=3,row=2)


window.mainloop()



#TODO
# fix this bug where when today is far out, it still toggles correctly.. do i want to add each week until I get there or skip the csv to the current week? probably skip to current week to start
#
#
#
#
#