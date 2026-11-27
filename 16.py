'''
    write a program to check weather a number is a 3-digit number and it's last digit is 7.(if condition)
'''
num=int(input("enter number :"))

if (100 <= num <=999) and num % 10 == 7:
    print("It is a 3-digit number and its last digit is 7.")
else:
    print("Condition not met.")
    