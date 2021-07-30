num=complex(input("enter a complex number"))
if num.real>num.imag:
    print("%d is greater"%num.real)
elif num.real<num.imag:
    print("%d is greater"%num.imag)
else:
    print("both are equal")
    
