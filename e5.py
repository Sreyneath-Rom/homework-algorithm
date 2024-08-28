# Ex5.create function to count letter "B" or "b" in string "abcdbeB"
def count(string):
    count_letter = 0
    for i in range(len(string)):
        if string[i] == "B" or string[i] == "b":
            count_letter += 1
    return count_letter
user_input = input("Enter a string: ")
print("Count of letter 'B' or 'b':", count(user_input))