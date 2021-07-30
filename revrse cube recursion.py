#to print cubes in reverse order
def rev_cube(n):
    if n>0:
        print(n,"--",n**3)
        rev_cube(n-1)
no=rev_cube(int(input("Enter the limit:")))


