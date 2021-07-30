#print all indices of all the occurence of a given element in a given list
l=[]#or l=[eval(x) for x in input("Enter list elements seperated by comma).split(,)]
n=int(input("Enter the no of elements"))
for i in range(0,n):
    a=int(input())
    l.append(a)
print("My List:",l)
element=int(input("Enter element value:"))
index=0
while index<len(l):
    if l[index]==element:
        print(index,end=' ')
    index+=1
