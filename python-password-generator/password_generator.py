import random
import string

print("===== Password Generator =====")

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)
