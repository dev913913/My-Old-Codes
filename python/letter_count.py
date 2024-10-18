
# get user input for string and letter
my_input = input("Enter the input string\n")
# check if input string is empty
while True:
    if my_input =='': 
        print("The input string is empty")
        my_input = input("Enter the input string again\n")
    else:
        break
#get user input for count
letter = input("Enter the letter to be counted\n")
# check if input string is empty
while True:
    if letter == '': 
        print("The letter to be counted is empty")
        letter = input("Enter the letter to be counted again\n")
    else:
        break
count = 0
for i in my_input: 
    if i==letter:count = count + 1
if len(letter) == 1: 
    print("The letter '", letter, "'appears", count, "time in the string")
else: 
    print("The letter '", letter, "'appears", count, "times in the string", sep='')
    

# if my_input is txt = '   '
#     x = txt.isspace()
#     print(x)
# if len(letter) == 1: 
#         print("The space", "appears", count, "time in the string")
#     else: 