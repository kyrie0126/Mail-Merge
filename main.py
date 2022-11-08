#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("C:/Users/Kyrie/Documents/100 Days of Code/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_text:
    letter = letter_text.read()
    print(letter)

with open("C:/Users/Kyrie/Documents/100 Days of Code/Mail Merge Project Start/Input/Names/invited_names.txt") as names_text:
    names = names_text.readlines()
    names = [x[:-1] for x in names]
    print(names)
    for name in names:
        print(name)
        edit = letter.replace("[name]", name)
        print(edit)
        with open(f"C:/Users/Kyrie/Documents/100 Days of Code/Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode="w") as final_letter:
            final_letter.write(edit)


