#program to print following series
"""
      1
     232
    34543
   4567654
           """
n=int(input("Enter how n

            many lines:"))
for i in range(1,n+1):
    a=i
    b=2*i-2
    for j in range(1,n-i+1):
        print(' ',end='')
    for k in range(1,i+1):
        print (a,end='')
        a=a+1
    for h in range(1,i):
        print(b,end='')
        b=b+1
    print()
    
 
    
