# Ex1.create function to sum number in string "1 2 3 4 5 6"

def sum(string):
    total = 0
    for i in range(len(string)):
        if string[i]!=" ":
            total += int(string[i])
    return total
string_num= input(": ")
print(sum(string_num) )