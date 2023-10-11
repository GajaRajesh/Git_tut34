aList = []
print("Please Enter 5 numbers")
for i in range(1,6):
    aList.append(int(input(f"Enter {i} number:\t")))
aSet = set(aList)
print(aSet)