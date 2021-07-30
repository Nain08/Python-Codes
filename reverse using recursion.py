#first n natural nos in reverse order
def reverse(n):
    if n>0:
        print(n,end=' ')
        reverse(n-1)
no=reverse(int(input("Enter the limit:")))
