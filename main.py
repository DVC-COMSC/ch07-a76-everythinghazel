
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
if len(num1) > len(num2):
    val = num1
    num1 = num2
    num2 = val
    num3 = num1 + num2

print (num3)


# ******************************

# print (num3) 
