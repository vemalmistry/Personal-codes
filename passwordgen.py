#Create a strong password between 8 and 50 characters
import random
a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(a, random.randint(8,50))) 
print(password)