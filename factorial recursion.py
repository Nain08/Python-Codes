#to calculate factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
no=fact(int(input("enter a no:")))
print(no)
