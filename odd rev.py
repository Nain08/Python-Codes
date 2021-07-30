#to print odd nos in reverse order
def rev_odd(n):
    if n>0:
        print(2*n-1)
        rev_odd(n-1)
print("Enter the limit:")
no=rev_odd(int(input()))
        
        
