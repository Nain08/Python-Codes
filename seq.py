#to print a sequence of number with given step size and boundary value
l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
s=int(input("Enter the step size:"))
for i in range(l,u+1,s):
    print(i)
