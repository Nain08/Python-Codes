#hcf
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
i=1
while i<=num1 or i<=num2:
    if num1%i==0 and num2%i==0:
        x=i
    i=i+1    
print("HCF=",x)        
    
