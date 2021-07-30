#to print all subsets of r elements each from a given set of N elements
def allSubsets(s):
    l=list(s)
    n=len(l)
    sets=[]
    for x in range(0,2**n):
        subset=[]
        for j in range(n):
            if x&(1<<j)>0:
                subset.append(l[j])
        sets.append(subset)
    return sets
s={1,2,3,4,5}
r=2
n=len(s)
for i in allSubsets(s):
    if len(i)==r:
        print(i)
    
