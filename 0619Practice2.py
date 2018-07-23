a_n=0
a_nplus1=1
a_nplus2=1

while(a_nplus2<100):
    print(a_nplus2)
    a_nplus2=a_nplus1+a_n
    a_n=a_nplus1
    a_nplus1=a_nplus2


 
    

def abc(x):
    if x>=0:
        return x 
    else:
        return -x
print(abs(-3))