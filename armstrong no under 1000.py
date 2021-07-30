#print armstrong no under 1000

for n in range(1,1001):
    t=n
    s=0
    while n>0:
        r=n%10
        c=r**3
        s=s+c
        n=n//10
    if s==t:
        print(s)
       
        
            
