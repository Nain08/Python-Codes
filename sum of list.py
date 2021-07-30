#find the sum of elements in the list
n=int(input("Enter the no of elements:"))
list=[]
sum=0
for i in range(0,n):
    a=int(input())
    list.append(a)
print("My List is:",list)
for i in range(0,n):
    sum=sum+list[i]
print("Sum of all elements:",sum)    
