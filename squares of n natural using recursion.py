#to print squares of first n natural no
def square(n):
    if n>0:
        square(n-1)
        print(n,"--",n**2)
no=square(int(input("Enter the limit:")))
