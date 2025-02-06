word1 = "striing"
word2 = "strings"

if len(word1) != len(word2):
    print("Not match.")
    exit()
if set(word1) == set(word2):
    print("Set check pass")
if sorted(word1) == sorted(word2):
    print("Match")
else:
    print("Not match")