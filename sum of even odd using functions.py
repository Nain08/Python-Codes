#sum of all even numbers and odd numbers from a given list of int values
def sum(l):
    so=0
    se=0
    for x in l:
        if x%2==0:
            se=se+x
        else:
            so=so+x
    return("Sum of even:",se,"Sum of odd:",so)
list=sum(eval(input("Enter a list of int values:")))
print(list)
    


    
