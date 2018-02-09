n=11
for i in range(1,n):
    for j in range(1,n):
        if i==1 or j==n-1 or i==n-2 or i==(n-1)/2 or (j==1 and i>=(n-1)/2 and i!=n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

'''
Output:
* * * * * * * * * * 
                  * 
                  * 
                  * 
* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * * 
                  * 
'''
