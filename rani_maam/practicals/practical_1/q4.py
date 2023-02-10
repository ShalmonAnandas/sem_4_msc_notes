principal = int(input("Enter the principal: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))

simple_interest = principal * rate * time / 100

print("The simple interest is", simple_interest)