import random

language = input("Select language (EN/ES):")
if language == "EN":
    tf = open("EN.txt")
elif language == "ES":
    tf = open("ES.txt")
else:
    exit(1)
translations = tf.readlines()
tf.close()
sf = open("SK.txt")
words = sf.readlines()
sf.close()
# ------------------------- #
correct = incorrect = 0
reps = input("select word count:")
for i in range(int(reps)):
    index = random.randint(0, 105)
    t = input(f"{words[index][0:-1]}: \n")
    if t == translations[index][0:-1]:
        print("\u2713")
        correct +=1
    else:
        incorrect +=1
        print(f"X ({translations[index]})")
print(f"Correct: {correct}, incorrect: {incorrect}")
