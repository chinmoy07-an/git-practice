import random
import string
letters = string.ascii_letters
numbers = '0123456789'
special_char = '-+*%&$!_'
combine = letters + numbers + special_char
length_pass = int(input("Enter Pass.length:"))
password = ''.join(random.sample(combine, length_pass))
print(password)