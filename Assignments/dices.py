import random
sums = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(100):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  print(f"throws: {dice1} {dice2}")
  throw_sum = dice1 + dice2
  sums[throw_sum] += 1  
value = 2 
for t in range(2,13):
  print(f"Sum {value} was thrown {sums[t]} times.")
  value += 1
number_of_throws = max(sums)
print("------------------------------")
print(f"Sum of {sums.index(number_of_throws)} was thrown {number_of_throws} times.")