i=1
factor=0
num=int(input("Enter a number:"))
while i<=num:
    if num%i==0:
        factor=factor+1
    i=i+1
if factor==2:
    print("Prime")
else:
    print("Not Prime")

    
    
    
