n=int(input("Enter the no of month:"))
if n==2:
    print("28 days")
elif n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("31 days")
elif n==4 or n==6 or n==9 or n==11:
    print("30 days")
else:
    print("Enter upto 12 only")
