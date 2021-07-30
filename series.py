#program to print following series
#1
#23
#456
#78910
           
b=1
n=int(input("Enter no of lines"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(b,end='')
        b=b+1
    print()   
