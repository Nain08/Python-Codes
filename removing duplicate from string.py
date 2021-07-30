#remove duplicates from list of strings
names=[]
n=int(input("How many names you want to enter?"))
for i in range(n):
    print(i+1,"enter name")
    names.append(input())
s=set(names)
names=list(s)
for x in names:
    print (x)
    


    
