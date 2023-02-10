my_tuple = (1, 2, 3, 4, 5, 6)
print("tuple before adding an item: " , my_tuple)

list = list(my_tuple)
list.append(7)
my_tuple = tuple(list)

print("tuple after adding an item: ",my_tuple)
