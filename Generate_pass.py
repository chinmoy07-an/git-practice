#The below python code will help you to Generate Password
#Enter the password length and rest leave it to the code
#Python community
#Be secure Be Safe


import random
import string
letters = string.ascii_letters
numbers = '0123456789'
special_char = '-+*%&$!_'
combine = letters + numbers + special_char
length_pass = int(input("Enter Pass.length:"))
password = ''.join(random.sample(combine, length_pass))
print(password)
