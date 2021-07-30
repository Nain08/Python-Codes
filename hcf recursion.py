#HCF using recursion
def hcf(a,b):
    if a<b:
        a,b=b,a
    return(b if a%b==0 else hcf(a%b,b))
x=hcf(int(input()),int(input()))
print(x)
