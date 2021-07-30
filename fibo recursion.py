#to print nth term of fibonacci series
def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)

no=fib(int(input("Enter the limit:")))
print(no)
