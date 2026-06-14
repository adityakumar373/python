import random
import string

passwordlen=12
#using letters,numbers and punctuators in string library of ascii
charvalues = string.ascii_letters + string.digits + string.punctuation #add all in one string

password=""
for i in range(random.randint(8,12)): #gives 8-12 random length password
    password+=random.choice(charvalues)

print("your password is:",password)  

#list comprehension method
#.join is used to join strings ""have anything written will be added between strings
password="".join([random.choice(charvalues) for i in range(passwordlen)])

print("your password is:",password)  
