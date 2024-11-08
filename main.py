rows = int(input("Enter the number of rows: "))

if rows%2 == 0:
    half_of_rows = rows//2
else:
    half_of_rows = (rows//2 +1)

space= half_of_rows-1
for i in range(1, half_of_rows+1):
    for j in range(1, space+1):
        print( end=' ')
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num+1
    print()
space= 1
for i in range(1, half_of_rows):
    for j in range(1, space+1):
        print( end=' ')
    space = space+1
    num = 1
    for j in range(1, 2*(half_of_rows-i)):
        print(end=str(num))
        num = num+1
    print()

