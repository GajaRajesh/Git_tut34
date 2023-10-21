def sumNum(num):
    sum = 0
    if num >= 0:
        while num > 0:
            sum += num % 10
            num = int(num / 10)
        print(sum)
    else:
        print("Invalid Entry")

num = int(input("Enter a Number: "))
sumNum(num)
