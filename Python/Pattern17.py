n=26
for i in range(1,n):
    num=i
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+n-j-1
        print(end=" ")
    print()
