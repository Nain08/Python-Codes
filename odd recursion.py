#to print first odd nos
def odd(n):
    if n>0:
        odd(n-1)
        print(2*n-1)
print("Enter the ending limit")
no=odd(int(input()))
    
