#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
no_letters= int(input("How many letters would you like in your password?\n")) 
no_symbols = int(input(f"How many symbols would you like?\n"))
no_numbers = int(input(f"How many numbers would you like?\n"))

# converting list into string
# x = ["0", "1", "2"]
# y = ''.join(x) 4
# z = int(y)

# Easy
# password = " "

# for i in range(1, no_letters + 1):
#     password += random.choice(letters)
# for i in range (1, no_numbers + 1):
#     password += random.choice(numbers)
# for i in range (1, no_symbols + 1):
#     password += random.choice(symbols)

# print(password)

#Hard
password = ""
for i in range(1, no_letters + 1):
    password += random.choice(letters)
for i in range (1, no_numbers + 1):
    password += random.choice(numbers)
for i in range (1, no_symbols + 1):
    password += random.choice(symbols)
  
final = ''.join(random.sample(password,len(password)))
print(final)