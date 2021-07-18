import math
def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
def Addition(Number1,Number2):
    print ("The addition is ",Number1+Number2)
def Subtraction(Number1,Number2):
    print ("The subtraction is ",Number1-Number2)
def Multiplication(Number1,Number2):
    print ("The multiplication is ",Number1*Number2)
def Division(Number1,Number2):
    print ("The division is ",Number1/Number2)
def Exponents(Number1,Number2):
    print ("The exponential product is ",Number1**Number2)
def Root(Number1,Number2):
    Root1=math.sqrt(Number1)
    Root2=math.sqrt(Number2)
    print ("The root of the first number is ",Root1)
    print ("The root of the second number is ",Root2)
print ("Welcome to the calculator!")
Use=str(input("Would you like to use this calculator? (Yes/No) "))
if Use=="No":
    quit()
if Use=="Yes":
    while True:
        print ("There are many functions this calculator can do for you:\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exponents\n6)Root")
        Operation=int(input("Enter the operation you wish to use (1/2/3/4/5/6) "))
        if Operation==1:
            Number1=int(input("Enter the first number - "))
            Number2=int(input("Enter the second number - "))
            Addition(Number1,Number2)
        elif Operation==2:
            Number1=int(input("Enter the first number - "))
            Number2=int(input("Enter the second number - "))
            Subtraction(Number1,Number2)
        elif Operation==3:
            Number1=int(input("Enter the first number - "))
            Number2=int(input("Enter the second number - "))
            Multiplication(Number1,Number2)
        elif Operation==4:
            Number1=int(input("Enter the first number - "))
            Number2=int(input("Enter the second number - "))
            Division(Number1,Number2)
        elif Operation==5:
            Number1=int(input("Enter the first number - "))
            Number2=int(input("Enter the second number - "))
            Exponents(Number1,Number2)
        elif Operation==6:
            Number1=int(input("Enter the first number - "))
            Number2=int(input("Enter the second number - "))
            Root(Number1,Number2)
        else:
            print ("Invalid input.")
        if not Continue():
            break