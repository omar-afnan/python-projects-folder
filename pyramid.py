n = int(input("Enter a number: "))

if n % 2 == 0 or n < 1 or n >= 1000:
    print("Enter an odd number between 1 and 999")
else:
    for i in range(n):
        spaces = (n - i - 1) // 2
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)
