#set of firt n prime numbers
n=int(input("Enter the limit:"))
s=set()
x=2
while n:
    if all(x%i!=0 for i in range(2,x)):
        s.add(x)
        n=n-1
    x=x+1
print(s)


