def binarysearch(a,l,r,x):
    if r>=l:
        mid=(l+r)//2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            return binarysearch(a,l,mid-1,x)
        else:
            return binarysearch(a,mid+1,r,x)
    else:
        return -1
a=[10,20,30,40,50,60]
x=50
result=binarysearch(a,0,len(a)-1,x)
if result!=-1:
    print('element is present at index:',result)
else:
    print('element not present')
