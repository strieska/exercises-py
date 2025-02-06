from random import randrange

number =  randrange(ord('A'), ord('Z'))

attempts = 0
for i in range(int((ord('Z') - ord('A'))/2)):
    guess = input("Guess:")
    attempts += 1
    if ord(guess) == number:
        print("Correct")
        print(f"Number of attempts: {attempts}")
        exit()
    elif ord(guess) < number:
        print("More")
    else:
        print ("Less")
print("FAIL")
print(chr(number))