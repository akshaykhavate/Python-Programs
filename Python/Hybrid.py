class A:
    a=10
    def __init__(self,b):
        self.b=b

class B(A):
    c=20
    def __init__(self,d,b):
        self.d=d
        A.__init__(self,b)

obj=B(999,1009)
print(obj.b,obj.d)
        

class C(A):
    g=18
    def __init__(self,b,e):
        self.e=e
        A.__init__(self,b)

obj=C(99,109)
print(obj.b,obj.e)

class D(B,C):
    r=18
    def __init__(self,b,t,e):
        self.t=t
        B.__init__(self,b)
        C.__init__(self,e)

obj=C(9,1)
print(obj.b,obj.e)
