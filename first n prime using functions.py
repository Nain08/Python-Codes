#first n prime no using functions
def f1(n):
    x=2
    while n:
        if all(x%i!=0 for i in range(2,x)):
            print(x)
            n=n-1
        x=x+1
a=f1(int(input("Enter the limit:")))
