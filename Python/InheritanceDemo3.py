class A:
    a=10
    def __init__(self,b):
        self.b=b

class B(A):
    c=20
    def __init__(self,b,d):
        self.d=d
        super().__init__(b)

class C(B):
    e=30
    def __init__(self,b,d,f):
        self.f=f
        super().__init__(b,d)

obj=C(100,200,300)
print(obj.a,obj.b,obj.d,obj.e,obj.f)
#print(obj.a,obj.b,obj.c,obj.d,obj.e,obj.f)
