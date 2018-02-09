class A:
    a=10

class B(A):
    b=20

obj=B()
print(obj.a,obj.b)
print(B.a,B.b)
print(A.a)
A.a=30
print()
print(obj.a,obj.b)
print(B.a,B.b)
print(A.a)
B.a=40
print()
print(obj.a,obj.b)
print(B.a,B.b)
print(A.a)
A.a=50
print()
print(obj.a,obj.b)
print(B.a,B.b)
print(A.a)
obj.a=60
print()
print(obj.a,obj.b)
print(B.a,B.b)
print(A.a)
