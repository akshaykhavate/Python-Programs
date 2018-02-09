n=7
for i in range(1,n):
    for j in range(1,n):
        if ((i<=n/2 and j<=n/2) and i+j<=n/2+1):
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()

'''
Output:
* * * - - - 
* * - - - - 
* - - - - - 
- - - - - - 
- - - - - - 
- - - - - -
