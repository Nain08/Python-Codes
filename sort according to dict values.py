#sort according to dict values
d=eval(input("Enter rollno and name as roll no:name each item seperated by comma:"))
for v in sorted(d.values()):
    for k in d:
        if d[k]==v:
            print(k,d[k])
