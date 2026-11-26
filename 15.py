'''
    write a program to check weather a student qualifies for a scolership(marks above 85 and attendance above 90%).(if condition)
'''
marks=int(input("enter your marks: "))

if marks>85:
    attandance=float(input("enter your attandance:"))
    if attandance>90:
        print("congratulation !! you are qualify for the scolership.")
    else:
        print("sorry !! you are not qualify for the scolership.")
else:
    print("oops ! you fail. ")