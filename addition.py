R1=int(input("Enter the no of rows of matrix 1="))
C1=int(input("Enter the no of columns of matrix 1="))
matrix1=[]
for i in range (R1):
    a=[]
    for j in range (C1):
        a.append(int(input()))
    matrix1.append(a)
R2=int(input("Enter the no of rows of matrix 2="))
C2=int(input("Enter the no of columns of matrix 2="))
matrix2=[]
for i in range (R2):
    b=[]
    for j in range (C2):
        b.append(int(input()))
    matrix2.append(b)
print("Matrix 1:")   
for i in range (R1):
    for j in range (C1):
        print (matrix1[i][j],end=" ")
    print()
print ("Matrix 2:")
for i in range (R2):
    for j in range (C2):
        print (matrix2[i][j],end=" ")
    print()

result=[[matrix1[i][j]+matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
for r in result:
    print(r)
