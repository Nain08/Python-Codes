#to calculate sum of first n even natural no
def sum(n):
    if n==0:
        return 0
    else:
        return 2*n+sum(n-1)
no=sum(int(input("Enter the limit:")))
print(no)
