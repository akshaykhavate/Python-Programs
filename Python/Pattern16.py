n=8
st=2
sp=4
for i in range(1,n):
    for j in range(1,sp):
        print(' ',end=" ")
    for k in range(1,st):
        print("*",end=' ')
    print()
    if i<n/2:
        sp=sp-1
        st+=2
    else:
        sp=sp+1
        st-=2
