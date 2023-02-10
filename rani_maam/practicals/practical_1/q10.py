n = int(input("Enter a number: "))

sum = 0

for i in range(1, n+1):
    sum += i**2

print("Sum of square of first", n, "natural numbers is", sum)