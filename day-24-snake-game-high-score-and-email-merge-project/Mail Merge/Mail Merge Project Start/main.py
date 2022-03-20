#TODO: Create a letter using starting_letter.txt 


with open("./Day 24 - Snake Game High Score and Email Merge Project/Mail Merge/Mail Merge Project Start/Input/Names/invited_names.txt", 'r') as file:
    names = file.readlines()

final_list_of_names = []
for name in names:
    name = name.strip()
    final_list_of_names.append(name)


print(final_list_of_names)

with open("./Day 24 - Snake Game High Score and Email Merge Project/Mail Merge/Mail Merge Project Start/Input/Letters/starting_letter.txt", 'r') as file:
    letter = file.read()
    print(letter)
    for name in final_list_of_names:
        temp_letter = letter.replace("[name]",name)
        with open(f"./Day 24 - Snake Game High Score and Email Merge Project/Mail Merge/Mail Merge Project Start/Output\ReadyToSend/send_to_{name}", 'w') as file:
            file.write(temp_letter)


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp