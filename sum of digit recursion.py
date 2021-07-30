#sum of digits of a given no
def digits(n):
    if n==0:
        return 0
    else:
        return n%10+digits(n//10)
no=digits(int(input("Enter the limit:")))
print(no)
