#Data input
x = int(input("Please input the 4-digit number \n"))

#Calculation workflow
first_digit = x // 1000
print(first_digit)
last_digit = x % 1000 % 100 % 10
result = first_digit % last_digit

#Output the result
print("Result is " + str(result))
