n=6
for i in range(1,n):
    for j in range(1,n):
        if i==j or i+j==n or i==1 or j==1 or j==n or i==n:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()



'''
output:

* * * * * 
* *   *   
*   *     
* *   *   
*       *

'''
