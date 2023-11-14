''' Task no.2
    Design a simple calculator with basic arithmetic operations. 
    Prompt the user to input two numbers and an operation choice.
   Perform the calculation and display the result.
'''



def Addition (a,b):  #Function of addition
    c=a+b
    print(f"\n The Addition of {a} and {b} is  {c}")

def Substraction (a,b):   #Function of substraction
    c=a-b
    print(f"\n The Substraction of {a} and {b} is  {c}")  

def Division (a,b):    #Function of Division
    if (b==0):
        print(f"\n The ans is infinity")
    else :
        c=a/b
        print(f"\n The Division of {a} and {b} is  {c}")

def Multiplicattion (a,b):   #Function of Multiplication
    c=a*b
    print(f"\n The Multiplication of {a} and {b} is  {c}")

flag=1
while (flag==1) :
    print(" \n <----------Menu---------->\n 1.Addition \n 2.Substraction \n 3.Division \n 4.Multiplication \n 5.Exit")
    ch=int(input("Enter your choise in number : "))


    if (ch==1):
        a=int(input("Enter the 1st value : "))
        b=int(input("Enter the 2nd value : "))
        Addition(a,b)
    elif(ch==2):
        a=int(input("Enter the 1st value : "))
        b=int(input("Enter the 2nd value : "))
        Substraction(a,b)
    elif(ch==3):
        a=int(input("Enter the 1st value : "))
        b=int(input("Enter the 2nd value : "))
        Division(a,b)
    elif(ch==4):
        a=int(input("Enter the 1st value : "))
        b=int(input("Enter the 2nd value : "))
        Multiplicattion (a,b)
    elif(ch==5):
        flag==0
    else:
        print("Please enter the choise")