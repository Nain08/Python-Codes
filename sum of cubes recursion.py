#to calculate sum of cubes of first n natural no
def sum(n):
    if n==1:
        return 1
    else:
        return n**3+sum(n-1)
no=sum(int(input("Enter the limit:")))
print(no)

