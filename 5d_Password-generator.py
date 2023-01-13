# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# ls = len(letters)
# ns = len(numbers)
# ss = len(symbols)
#
# a = 0
# b = 0
# c = 0
#
# x = nr_letters - a
# y = nr_numbers - b
# z = nr_symbols - c
# res = ""
#
# for i in range(0, nr_letters):
#     l = random.randint(0, (ls - 1), )
#     if a < x:
#         a = a + 1
#         # print(letters[l])
#         res += letters[l]
#     else:
#         break
#
# for j in range(0, nr_numbers):
#     n = random.randint(0, (ns - 1), )
#     if b < y:
#         b = b + 1
#         res += numbers[n]
#     else:
#         break
#
# for k in range(0, nr_symbols):
#     s = random.randint(0, (ss - 1), )
#     if c < z:
#         c = c + 1
#         res += symbols[s]
#     else:
#         break
#
# lista = list(res)
# random.shuffle(lista)
# Wynik = ''
#
# for g in lista:
#     Wynik += '' + g
#
# print(Wynik)
#
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password =""
#
# for char in range(1, nr_letters + 1):
#     password+= random.choice(letters)
#
# for char in range(1, nr_numbers + 1):
#     password+= random.choice(numbers)
#
# for char in range(1, nr_symbols + 1):
#     password+= random.choice(symbols)
#
# print(password)

password_list =[]

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password =""
for char in password_list:
    password += char

print(f"Your password is: {password}")
