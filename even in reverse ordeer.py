#program to print first n even nos in reverse order
n=int(input("Enter the limit"))
if n%2==0:
    n=n
else:
    n=n-1
for i in range(n,-1,-2):
    print(i)
    
