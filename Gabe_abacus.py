def print_abacus(value):
    i,num=1000000000,0
    while i>0.1:
        print "|"+"00000*****"[:10-(value/i)]+"   "+"00000*****"[10-(value/i):]+"|"
        i=i/10

    return(value)

print_abacus(12345678)
