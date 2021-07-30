#create homogeneous tuple from heterogeneous tuple
t=eval(input("Enter heterogeneous tuple values:"))
t1=[]
t2=[]
t3=[]
t4=[]
t5=[]
for x in t:
    if type(x)==int:
        t1.append(x)
    elif type(x)==float:
        t2.append(x)
    elif type(x)==complex:
        t3.append(x)
    elif type(x)==str:
        t4.append(x)
    elif type(x)==bool:
        t5.append(x)
t1=tuple(t1)
t2=tuple(t2)
t3=tuple(t3)
t4=tuple(t4)
t5=tuple(t5)
print(t1,t2,t3,t4,t5,sep='\n')
