#count of substring in a string
c=0
s=input("Enter a string:")
p=input("Enter a substring:")
if p in s:
    c=s.count(p)
print(p,"is present",c,"times")
