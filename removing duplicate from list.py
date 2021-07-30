n=int(input("Enter how many numbers in the list:"))
list=[]
print("Enter list elements:")
for i in range(0,n):
    a=int(input())
    list.append(a)
print(list)
print("New list after removal of duplicates")
new_list=[]
for a in list:
    if a not in new_list:
        new_list.append(a)
print(new_list)
