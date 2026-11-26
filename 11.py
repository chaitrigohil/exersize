'''
    write a program to check weather a password length is at least 8 characters.(if condition
'''
password=input("enter your password: ")

if len(password)>=8:
    print("valid password")
else:
    print("incorrect password !! please enter valid password and password must be at least 8 charactor")