with open('./Input/Letters/starting_letter.txt') as file:
    letter_template = file.read()

with open('./Input/Names/invited_names.txt') as names:
    all_names = names.readlines()

for i in range(len(all_names)):
    all_names[i] = all_names[i].strip("\n")

for name in all_names:
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as custom_letter:
            new_letter = letter_template.replace('[name]',name)
            custom_letter.write(new_letter)