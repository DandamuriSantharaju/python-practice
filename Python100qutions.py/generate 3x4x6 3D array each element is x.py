
#generate 3*4*6 3D array each element is *.py
rows, columns, depth = 3, 4, 6

# Create the 3D array
array = [[['*' for _ in range(depth)] for _ in range(columns)] for _ in range(rows)]

# Print the 3D array
for layer in array:
    for row in layer:
        print(row)
    print()