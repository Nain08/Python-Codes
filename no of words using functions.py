#count words in a string
def f1(n):
    c=1
    x=n.count(' ')
    x=x+1
    return x
a=f1(input("Enter a string without extra spaces:"))
print("NO of words=",a)
