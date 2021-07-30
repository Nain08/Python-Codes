#list of first n prime numbers
n=int(input("Enter natural no:"))
l=[]
x=2
while n:
    if all(x%i!=0 for i in range(2,x)):
        l=l+[x]
        n=n-1
    x=x+1
print (l)
