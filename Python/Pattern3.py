n=6
for i in range(1,n):
    for j in range(1,n):
        if i+j>=n:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()


'''
output:
        * 
      * * 
    * * * 
  * * * * 
* * * * *

'''
