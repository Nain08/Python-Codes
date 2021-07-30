#lcm
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
l=max(a,b)
while l<=a*b:
    if l%a==0 and l%b==0:
        print("LCM is",l)
        break
    l=l+1
