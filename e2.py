# Ex2.create function to sum odd number in string "1 2 3 4 5 6"
def sum(string):
    total = 0
    for i in range(len(string)):
        if string[i]!=" ":
            if int(string[i])%2==1:
                total += int(string[i])
    return total
string_num= input(": ")
print("Sum Odd Number: "+str(sum(string_num)))