#power set
s1=eval(input("Enter set values:"))
l1=list(s1)
n=len(s1)
powerset=set()
for i in range(2**n):
    t=tuple({l1[j] for j in range(n) if (i&(1<<j))})
    powerset.add(t)
print(powerset)
