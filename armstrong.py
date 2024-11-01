def countDigits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
def isArmstrong(num):
    numOfDigits = countDigits(num)
    temp = num 
    arm = 0
    while num != 0:
        rem = num % 10
        arm = arm + (rem ** numOfDigits)
        num //= 10
    return temp == arm
def ArmstrongRange(start, end):
    armstrong_list = []
    for num in range(start, end + 1):
        if isArmstrong(num):
            armstrong_list.append(num)
    return armstrong_list
start = int(input("Enter the lower limit"))
end = int(input("Enter the upper limit"))
print("The Armstrong numbers are\t", ArmstrongRange(start, end))
