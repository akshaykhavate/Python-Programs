a=[22,89,8,99,1]
for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
        if a[j]<a[min]:
            min=j
    a[i],a[min]=a[min],a[i]
print("sorted array is:")
for i in range(len(a)):
    print('%d'%a[i])
