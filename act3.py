num = int(input("enter a number"))

if num % 2 == 0:
    print("it is an even number", num)
else:
    print("it is an odd number", num)

# Check if the number is positive, negative, or zero
if num > 0:
    print("the number is positive", num)
elif num == 0:
    print("the number is zero", num)
else:
    print("the number is negative", num)