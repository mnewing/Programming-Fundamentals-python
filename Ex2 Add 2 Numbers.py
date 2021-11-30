#get two numbers from the user then add them together

#input returns strings so we will need to force num1 and num2 to be integeres before we do the calculation
num1 = int(input("1st number "))
num2 = int(input("2nd number "))

result = num1 + num2
print(type(result))
print("the result of adding "+str(num1)+" and "+str(num2)+" is "+str(result))
