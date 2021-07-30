R1=int(input("Enter the no of rows of matrix 1="))
C1=int(input("Enter the no of columns of matrix 1="))
A=[]
for i in range (R1):
    a=[]
    for j in range (C1):
        a.append(int(input()))
    A.append(a)
R2=int(input("Enter the no of rows of matrix 2="))
C2=int(input("Enter the no of columns of matrix 2="))
B=[]
for i in range (R2):
    b=[]
    for j in range (C2):
        b.append(int(input()))
    B.append(b)
result=[[0,0,0],[0,0,0],[0,0,0]]
print("Matrix 1:")   
for i in range (R1):
    for j in range (C1):
        print (A[i][j],end=" ")
    print()
print ("Matrix 2:")
for i in range (R2):
    for j in range (C2):
        print (B[i][j],end=" ")
    print()
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
for r in result:
    print(r)
    
