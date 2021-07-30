#palindrome
sum=0
num=int(input("Enter a number"))
numcopy=num
while numcopy>0:
    sum=sum*10
    sum=sum+(numcopy%10)
    numcopy=numcopy//10
if num==sum:
    print("Palindrome")
else:
    print("Not Palindrome")
    

