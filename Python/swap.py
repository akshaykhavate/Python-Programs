def swap(a,b):
    a,b=b,a
    return a,b

a,b=10,20
print('before swaping value of a is {0}, and b is {1}'.format(a,b))
a,b=swap(a,b)
print('After swaping value of a is {0}, and b is {1}'.format(a,b))
