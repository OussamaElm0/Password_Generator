import random
import string

def genPassword(length):
    rand = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(int(length)) :
        password += random.choice(rand)
    return password
