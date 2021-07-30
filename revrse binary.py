#to print reverse of a binary representation of a given number
def f1(a):
    while a>0:
        print(a%2,end='')
        a=a//2
f1(int(input("Enter a no:")))
        
