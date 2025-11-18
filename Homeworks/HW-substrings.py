def find_largest_common_substring(str1, str2):
    # Write your code here
    return


# Do not modify code under this line
# -----------------------------------
# Testing 1
str1 = "abcdefg"
str2 = "bcdfgh"
result = find_largest_common_substring(str1, str2)
if result == "bcd":
    print("Test 1: OK")
else:
    print("Test 1: Failed!")

# Testing 2
str1 = "Lorem ipsum"
str2 = "Dalas sat akat"
result = find_largest_common_substring(str1, str2)
if result == " ":
    print("Test 1: OK")
else:
    print("Test 1: Failed!")

# Testing 3
str1 = ""
str2 = "abcdefgh"
result = find_largest_common_substring(str1, str2)
if result == "":
    print("Test 1: OK")
else:
    print("Test 1: Failed!")

# Testing 4
str1 = "Random text to check the function"
str2 = "andom text to check the function"
result = find_largest_common_substring(str1, str2)
if result == "andom text to check the function":
    print("Test 1: OK")
else:
    print("Test 1: Failed!")
