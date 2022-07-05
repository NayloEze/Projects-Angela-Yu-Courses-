#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passwords = []

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
for letter in range(nr_letters):
    random_letters = (random.choice(letters))
    passwords.append(random_letters)
nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(nr_symbols):
    random_symbols = (random.choice(symbols))
    passwords.append(random_symbols)
nr_numbers = int(input(f"How many numbers would you like?\n"))
for number in range(nr_numbers):
    random_number = (random.choice(numbers))
    passwords.append(random_number)
#print(passwords)
random.shuffle(passwords)
#password = random.sample(passwords, len(passwords))
print(passwords)
final_password = "".join(passwords)
print(final_password)
