#to print first n even natural no
def even(n):
    if n>0:
        even(n-1)
        print(2*n)
print("Enter the starting and ending limit")
no=even(int(input()))
    
