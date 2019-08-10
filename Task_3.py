#Data input
x = int(input("Please input 3-digit number \n"))

#Reverse workflow
number1 = x // 100
number3 = x % 10
number2 = (x % 100) // 10

#Output the result
print(str(number3) + str(number2) + str(number1))