#program to find inputted no is armstrong or not
n=int(input("Enter a no:"))
temp=n
sum=0
while(n>0):
    a=n%10
    cube=a**3
    sum=sum+cube
    n=n//10
if (sum==temp):
    print("Armstrong")
else:
    print("Not Armstrong")
    
