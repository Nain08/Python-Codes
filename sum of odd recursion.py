#to calculate sum of first n odd natural no
def sum(n):
    if n==1:
        return 1
    else:
        return 2*n-1+sum(n-1)
no=sum(int(input("Enter the limit:")))
print(no)

