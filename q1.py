'''Create two integer matrix of same size MX N ( M rows and M columns). Write a program to find how many common elements are there between them and print the elements also'''
matrix=[input("Enter row to elements separated by space : ").split() for i in range(int(input("Enter the range of square matrix :")))]
common=[]
alle=[]
for i in matrix:
    for j in i:
        if j not in alle:alle.append(j)
        elif j not in common:common.append(j)
        else:continue
print(f"Number of common elements is {len(common)}","The elements are "+",".join(common),sep="\n")