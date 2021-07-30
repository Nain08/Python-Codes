i=2
sum=1.0
n=int(input("Enter value of n"))
while i<=n:
    sum=sum+(((-1)**i)*(1/i))
    i=i+1
print(sum)
