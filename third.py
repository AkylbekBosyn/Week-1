import math
num = float(input("Enter number"))
temp = math.floor(num)
print(temp)
print(int((num-temp)*100*100) , "," , temp/100)
