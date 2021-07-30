m=int(input("Enter number of rows,m="))
n=int(input("Enter number of columns,n="))
matrix=[]
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)
for i in range(0,m):
    for j in range(0,n):
        print("Entry in row:",i+1,"column:",j+1)
        matrix[i][j]=int(input())
print(matrix)
