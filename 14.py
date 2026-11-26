'''
    write a program to check weather a person's monthly income is greater than the avergae income of three given people.(if condition)
'''
person1=10000
person2=20000
person3=30000

average = (person1+person2+person3)/3   

income=float(input("enter your monthly income: "))

if income==average:
    print("your income is equal to the average")
elif income>average:
    print("your monthly income is greater then 3 person's ")
else:
    print("your monthly income is less then 3 person's")