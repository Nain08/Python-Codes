#program to find greatest of three numbers
a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
c=int(input("Enter the third no:"))
if(a>b and a>c):
    print(a,"is the largest no")
elif(b>a and b>c):
    print(b,"is the largest no")
else:
    print(c,"is the largest no")
