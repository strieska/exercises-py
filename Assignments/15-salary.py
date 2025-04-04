def count_bank_notes(igor, amount):
    if amount // igor == 0:
        return amount
    print(f"Note {igor}: {amount//igor}x")
    return amount % igor

f=open("15-salary.txt")
file_values = f.readlines()
for value in file_values:
    name, surname, amount = value.split(" ")
    print(f"{name} {surname}:")

    bank_notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    amount = 1234

    for note in bank_notes:
        amount = count_bank_notes(note, amount)
    print("\n")