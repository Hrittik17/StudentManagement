import re


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def EmailValidation(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
    
m = input("Enter email: ")
if(EmailValidation(m)):
    print("Valid")
else:
    print("invalid")