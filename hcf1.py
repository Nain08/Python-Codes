#Hcf
a=int(input("Enter first no"))
b=int(input("Enter second number"))
h=min(a,b)
while h>=1:
    if a%h==0 and b%h==0:
        print("HCF is",h)
        break
    h=h-1
