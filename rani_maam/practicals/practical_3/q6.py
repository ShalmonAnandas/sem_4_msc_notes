my_tuple = (2, 4, 5, 6, 2, 3, 4, 4, 7)

num = int(input("What do you want to search for?: "))

if num in my_tuple:
    print("Element exists in tuple")
else:
    print("Element does not exist in tuple")