#to print even nos in reverse order
def rev_even(n):
    if n>0:
        print(2*n)
        rev_even(n-1)
print("Enter the limit:")
no=rev_even(int(input()))
        
        
