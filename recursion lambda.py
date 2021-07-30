#recursion in lambda
n=lambda a:1 if a==0 else a*n(a-1)
r=n(5)
print(r)
