numbers = [2, 3, 1, 4, 5, 3, 2]

seen = set()
for num in numbers:
    if num in seen:
        print("The first duplicate element is: ", num)
        break
    seen.add(num)
else:
    print("No duplicate elements found.")