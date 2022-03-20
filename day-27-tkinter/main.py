import tkinter

switch_value = "mi_to_km"

def mi_to_km():
    if switch_value == "mi_to_km": 
        input_text = float(input.get())
        input_text = input_text * 1.60934
        output_value_label.config(text=input_text)
    elif switch_value == "km_to_mi":
        input_text = float(input.get())
        input_text = input_text / 1.60934
        output_value_label.config(text=input_text)

def switch():
    global switch_value
    if output_label.cget("text") == "Kilometers":
        output_label.config(text="Miles")
        input_label.config(text="Kilometers")
        output_value_label.config(text="N/A")
        switch_value = "km_to_mi"
    
    elif output_label.cget("text") == "Miles":
        output_label.config(text="Kilometers")
        input_label.config(text="Miles")
        output_value_label.config(text="N/A")
        switch_value = "mi_to_km"


window = tkinter.Tk()
window.title("Jared's First GUI Program")
window.minsize(width= 500, height= 300)
window.config(padx=100,pady=80)

#is equal to label
is_equal_to_label = tkinter.Label(text="Is equal to", font=("Arial", 12, 'normal'))
is_equal_to_label.grid(column= 0,row= 1)
is_equal_to_label.config(padx=10,pady=10)

#Input Label
input_label = tkinter.Label(text="Miles", font=("Arial", 12, 'normal'))
input_label.grid(column=2,row= 0)
input_label.config(padx=10,pady=10)

#Kilometers Label
output_label = tkinter.Label(text="Kilometers", font=("Arial", 12, 'normal'))
output_label.grid(column=2,row= 1)
output_label.config(padx=10,pady=10)

#Output Value Label
output_value_label = tkinter.Label(text="N/A", font=("Arial", 12, 'normal'))
output_value_label.grid(column=1,row= 1)
output_value_label.config(padx=10,pady=10)

#Input
input = tkinter.Entry(width= 15)
input.grid(column= 1,row= 0)

#Calculate Button
calculate_button = tkinter.Button(text="Calculate", command= mi_to_km)
calculate_button.grid(column= 1,row= 2)
calculate_button.config(padx=10,pady=10)

#Switch Button
#Km -> Mi goes to Mi -> Km
switch_button = tkinter.Button(text="Switch", command= switch)
switch_button.grid(column= 2,row= 2)
switch_button.config(padx=10,pady=10)




window.mainloop() #mainloop is a while loop that is always listening to what the screen tells it to do:
