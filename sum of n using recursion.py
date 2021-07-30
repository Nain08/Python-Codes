#to calculate sum of first n natural no
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
no=sum(int(input("Enter the limit:")))
print(no)


        
