#program to print all prime numbers upto n
n=int(input("Enter the value of n "))
for i in range(2,n):
    for x in range(2,i):
        if i%x==0:
            break
    else:
        print(i)
