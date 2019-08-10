#Input of Data
square = float(input("Please input the value of triangle's square \n"))
diff = float(input("Please input the value of the difference between the triangle's base and its height \n"))

#Discriminant
D = diff**2 + 8 * square
print(D)

#Calculations
if D < 0:
    print("No existing solutions")
elif D == 0:
    height = -diff / 2
    if height <= 0:
        print("No solutions")
    else:
        print("height = ", round(height, 3))
else:
    height_1 = (-diff - D**0.5) / 2
    if height_1 <= 0:
        print("No solutions")
    else:
        print("height_1 = ", round(height_1, 3))
    height_2 = (-diff + D**0.5) / 2
    if height_2 <= 0:
        print("No solutions")
    else:
        print("height_2 = ", round(height_2, 3))