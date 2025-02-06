f = open("26-charity.txt")
file_content = f.readlines()
f.close()
print(f"Call count: {len(file_content)}")
total_length = 0
longest_call_id = 0
longest_call_time = 0
for caller in file_content:
    #id, caller_id, call_time = caller.split(" ")
    caller_id = caller.split(" ")[1]
    total_caller_time = 0
    for call_time in caller.split(" ")[2:]:
        total_length += int(call_time)
        total_caller_time += int(call_time)

    #total_length += int(call_time)
    if longest_call_time < int(total_caller_time):
        longest_call_time = int(total_caller_time)
        longest_call_id = caller_id
print(f"Total time: {total_length}")
print(f"Longest call ID: {longest_call_id}")
print(f"Average call length: {float(total_length)/len(file_content)}")
f = open("26-result.txt", "w+")
f.write(f"Call count: {len(file_content)}\n")
f.write(f"Total time: {total_length}\n")
f.write(f"Longest call ID: {longest_call_id}\n")
f.write(f"Average call length: {float(total_length)/len(file_content)}")
f.close()