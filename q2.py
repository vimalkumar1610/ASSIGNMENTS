'''Write a program to replace the duplicate elements in an matrix into zero.
Eg:
    3 4 6
    2 6 8
    4 3 7
Output :
    3 4 6
    2 0 8
    0 0 7'''
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))

matrix=[[input(f"Enter element for row of {j+1} and column of {i+1} : ")for i in range(c)]for j in range(r)]
peerless=[]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] not in peerless:peerless.append(matrix[i][j])
        else:matrix[i][j]='0'
for _ in matrix:
    print(" ".join(_))