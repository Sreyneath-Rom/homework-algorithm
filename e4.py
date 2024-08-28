# EX4.create function to reverse string "abc" =>cda
def reverse_string(string):
    result = ""
    for i in range(len(string)):
        result += string[len(string) - 1 - i]
    return result
input_string = input("Enter a string: ")
print("Reversed string:", reverse_string(input_string))