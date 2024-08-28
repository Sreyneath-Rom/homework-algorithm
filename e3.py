
# Ex3.create function to find min number in string "1 2 6 3 4 0 5"
def find_min(string):
    numbers = string
    min_value = (numbers[0])
    for i in range(len(string)):
        num = (string[i])
        if num < min_value:
            min_value += num
    return min_value
input_string = input("Enter numbers: ")
print("Minimum value:", find_min(input_string))
