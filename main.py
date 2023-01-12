#This code will generate password with custom length 

import secrets,string

def get_pass():

    length = 10
    letters = string.ascii_letters
    digits = string.digits
    punct = string.punctuation
    characters = letters + digits + punct
    password = ""
    for i in range(length):
        password += "".join(secrets.choice(characters))
    print(password)

get_pass()


