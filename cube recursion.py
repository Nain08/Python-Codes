#to print cubes
def cube(n):
    if n>0:
        cube(n-1)
        print(n,"--",n**3)
no=cube(int(input("Enter the limit:")))


