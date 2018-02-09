def linearsearch(a,n):
    for i in range(len(a)):
        if a[i]==n:
            return i
        else:
            return -1

a=[10,20,30,5,25,89]
n=5
result=linearsearch(a,n)
if result!=-1:
    print('element found at',result)
else:
    print('element not found')
