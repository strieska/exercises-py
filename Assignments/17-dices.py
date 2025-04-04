from random import randint

f = open("17-dices.txt", "w")

throw_count = int(input("Number of dice throws:"))
throws = []
sums = [0] * 13
for i in range(throw_count):
    # throws[i] = input().split(" ")
    throws.append([randint(1,6),randint(1,6)])
    throw_sum = throws[i][0]+throws[i][1]
    f.write(f"{throws[i][0]} {throws[i][1]} -> {throw_sum}\n")
    sums[throw_sum] += 1

print(f"{sums.index(max(sums))} - {max(sums)}x")
f.close()