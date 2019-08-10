#Data input
#Point A coordinates
x1 = int(input("Please input the X coordinate for A \n"))
y1 = int(input("Please input the Y coordinate for A \n"))

#Point B coordinates
x2 = int(input("Please input the X coordinate for B \n"))
y2 = int(input("Please input the Y coordinate for B \n"))

#Point C coordinates
x3 = int(input("Please input the X coordinate for C \n"))
y3 = int(input("Please input the Y coordinate for C \n"))

#Point D coordinates
x4 = int(input("Please input the X coordinate for D \n"))
y4 = int(input("Please input the Y coordinate for D \n"))

#Calculation workflow
#Defining of the length of every side
side_AB_len = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(side_AB_len)

side_CD_len = ((x4 - x3)**2 + (y4 - y3)**2)**0.5
print(side_CD_len)

side_BC_len = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
print(side_BC_len)

side_AD_len = ((x4 - x1)**2 + (y4 - y1)**2)**0.5
print(side_AD_len)

#Verification for the parallelogram
if (side_AB_len != side_CD_len) or (side_BC_len != side_AD_len):
    print("This is not a parallelogram")
else:
    print("This is a parallelogram")

#Calculation of the Height and Square
if (x1 == x2) and (x3 == x4):
    height = x4 - x1
    square = side_AB_len * height
elif (y1 == y4) and (y2 == y3):
    height = y2 - y1
    square = side_AD_len * height
    print("Square is " + str(square))
else:
    print("OK")



# #Diagonal AC length calculation
# diag_AC_len = (2 * (side_AB_len**2 + side_BC_len**2) - diag_BD_len**2)**0.5
#
# #Diagonal BD length calculation
# diag_BD_len = (2 * (side_AB_len**2 + side_BC_len**2) - diag_BD_len**2)**0.5