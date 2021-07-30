#fibonacci series
num=int(input("Enter a number"))
i=1
a=0
b=1
while i<=num:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1
