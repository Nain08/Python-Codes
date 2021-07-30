#to print squares in reverse order
def rev_square(n):
    if n>0:
        print(n,"--",n**2)
        rev_square(n-1)
no=rev_square(int(input("Enter the limit:")))

