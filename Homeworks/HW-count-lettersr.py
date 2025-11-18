# User enters a letter and program counts all occurences in the list of names

names = ["Olivia Smith", "David Brown", "Sophia Taylor", "Michael Davis", "Sarah Anderson",
    "John Clark", "Emily Wilson", "Daniel Lee", "Alice Moore", "Robert Johnson",
    "Sophia Moore", "Michael Smith", "Olivia Davis", "John Lee", "Emily Davis",
    "David Wilson", "Sarah Smith", "Daniel Moore", "Alice Taylor", "Robert Brown",
    "Sophia Lee", "Michael Moore", "Olivia Davis", "John Taylor", "Daniel Smith",
    "Emily Wilson", "Alice Anderson", "David Johnson", "Sarah Smith", "Robert Clark",
    "Michael Taylor", "Sophia Lee", "Daniel Davis", "Olivia Brown", "David Wilson",
    "Sarah Clark", "Emily Lee", "John Davis", "Alice Moore", "Michael Anderson",
    "Robert Smith", "Sophia Davis", "Olivia Lee", "Daniel Taylor", "David Davis",
    "Sarah Moore", "Emily Clark", "John Wilson", "Alice Smith", "Robert Johnson",
    "Michael Clark", "Sophia Anderson"]

while True:
    while True:
        chosen_letter = input("Choose a letter: ")
    
        letter_counter1 = 0
    
        for letter_check in chosen_letter:
            letter_counter1 = letter_counter1 + 1

        if chosen_letter == "":
            break
        if letter_counter1 == 1:
            break
        else:
            print("You entered more than one character!")
            print("")
            continue

    if chosen_letter == "":
            break
        
    letter_counter2 = 0 

    for single_name in names:
        for letter in single_name:
            if letter == chosen_letter:
                letter_counter2 = letter_counter2 + 1
    
    print(f"Your letter, {chosen_letter}, appears in the list {letter_counter2} times.")
    print("")
            
