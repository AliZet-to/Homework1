#Data input
radius1 = float(input("Please input the Rotation Radius of the First Planet \n"))
period1 = float(input("Please input the Rotation Period of the First Planet \n"))
radius2 = float(input("Please input the Rotation Radius of the Second Planet \n"))

#Calculation of the Second Planet Rotation Period
period2 = (radius1**3 / (period1**2 * radius2**3))**0.5

#Results displaying
print("The Second Planet Rotation Period is " + str(period2))