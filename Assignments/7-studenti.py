f = open("7-studenti.txt")
# print(f.read())
content = f.readlines()
if len(content) == 0:
    print("File not loaded.")
    exit(-1)
f.close()
sum_excused = sum_unexcused = 0
max_excused = max_unexcused = ("",0)
student_count = int(content[0])
content.remove(content[0])
for row in content:
    name, surname, excused_str, unexcused_str = row.split(" ")
    excused, unexcused = int(excused_str), int(unexcused_str)
    sum_excused += int(excused)
    sum_unexcused += int(unexcused)
    if excused > max_excused[1]:
        max_excused = (f"{name} {surname}", int(excused))
    if unexcused > max_unexcused[1]:
        max_unexcused = (f"{name} {surname}", int(unexcused))

out = open("7-out.txt", "w+")
out.write(f"Avg excused: {sum_excused/student_count}, avg unexcused: {sum_unexcused/student_count}\n")
out.write(f"Most excused absences: {max_excused[0]}\n")
out.write(f"Most unexcused absences: {max_unexcused[0]}")
out.close()