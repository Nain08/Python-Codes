#palindrome
s1=input("Enter a string:")
t=s1
x=s1[::-1]
if t==x:
    print("Palindrome")
else:
    print("Not Palindrome")
