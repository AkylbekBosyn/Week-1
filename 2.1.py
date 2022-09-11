num1 = int(input("First number:"))
operation = input("Operation:")
num2 = int(input("Second number:"))
if operation in ('+','-','*','/'):
     if operation == "+":
         print(num1 + num2)
     elif operation == "-":
         print(num1-num2)
     elif operation == "*":
         print(num1*num2)
     else:
         print(num1/num2)
 else:
     print("It's common calculator")
