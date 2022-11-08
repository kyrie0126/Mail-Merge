with open("C:/Users/Kyrie/Documents/100 Days of Code/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_text:
    letter = letter_text.read()

with open("C:/Users/Kyrie/Documents/100 Days of Code/Mail Merge Project Start/Input/Names/invited_names.txt") as names_text:
    names = names_text.readlines()
    names = [x[:-1] for x in names]
    for name in names:
        edit = letter.replace("[name]", name)
        with open(f"C:/Users/Kyrie/Documents/100 Days of Code/Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode="w") as final_letter:
            final_letter.write(edit)


