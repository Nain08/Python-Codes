#lcm using fuctions takes something teturns something
def f1(a,b):
    l=max(a,b)
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l=l+1
x=f1(int(input("Enter first no:")),int(input("Enter second no :")))
print("LCM is",x)
        
