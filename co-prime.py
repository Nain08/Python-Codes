#co-prime number
a=int(input("Enter first number"))
b=int(input("Enter second number"))
H=min(a,b)
while H>=1:
    if a%H==0 and b%H==0:
        if H==1:
            print("Co-Prime")
        else:
            print("Not co prime")
        break
    H=H-1
