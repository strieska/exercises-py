import random 
ticket_number = input() # User inputs number of tickets
f = open("tickets.txt", "w+")
tickets = [] # For easy access a variable that holds tickets in memory
for i in range(int(ticket_number)):
    tickets.append(f"{random.randint(1,50)},{random.randint(1,50)},{random.randint(1,50)}\n") # generating tickets
    f.writelines(tickets[i]) # write tickets to file
usr_input = input()+"\n" # users ticket
f.write(usr_input)
if tickets.count(usr_input) > 0: # verification
    f.write(f"{tickets.index(usr_input)+1}") # output
else:
    f.write("Lost")
f.close()