#1)Creatig a function getting two integers from user and printing
def math(a,b):
    print("Addition of the two numbers is",a+b)
    print("Subtraction of the two numbers is",a-b)
    print("Division of two numbers is",a//b)
    print("Multiplication of two numbers is",a*b)
    
num1=int(input("Enter the first integer:"))
num2=int(input("Enter the second integer:"))
math(num1,num2)

#2)Creating a function covid()
def covid(Patient_name,body_temperature):
    print("Patient name is",Patient_name,)
    if(body_temperature==""):
        default="98"
        print("His body temperature is",default,"degrees")
    else:
        print("His body temperature is",body_temperature,"degrees")
        
x=input("Enter the patient name:")
y=(input("Enter the patient\'s body temperature:"))
covid(x,y)
