rows = int(input())
columns = int(input())
tree_number = int(input())

if tree_number <= columns or tree_number % columns == 1 or tree_number % columns == 0:
    print("true")
else:
    print("false")