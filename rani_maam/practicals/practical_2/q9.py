list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
list3 = []

for i in list1:
    if i%2 == 0:
        list2.append(i)
    else:
        list3.append(i)

print("Even numbers are:",list2)
print("Odd numbers are:",list3)
