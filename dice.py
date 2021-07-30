#2 sets represents 2 identical dices(from 1 to 12)
#write a python script to produce sample space to get a sum of dice values when rolled is n.
s1=[1,2,3,4,5,6]
s2=[1,2,3,4,5,6]
l1=list(s1)
l2=list(s2)
n=int(input("Enter the number from 1 to 12:"))
print("All possible values:")
for i in range(0,6,1):
    for j in range(0,6,1):
        if l1[i]+l2[j]==n:
            print((l1[i],l2[j]))
           
        
