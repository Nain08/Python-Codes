#recursive function to print first n natural nos
def natural(n):
    if n>0:
        natural(n-1)
        print(n,end=' ')
no=natural(int(input("Enter the limit:")))


    
