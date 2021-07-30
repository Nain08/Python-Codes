n=int(input("Enter a positive number:"))
for x in range(2,n):
    if n%x==0:
        print(n, "is not prime and it is expressed as ",x,'*',int(n/x))
        break
else:
    print(n,"is prime number")
          
