class A:
    a=10
    def __init__(self,b):
        self.b=b

class B:
    c=20
    def __init__(self,d):
        self.d=d

class C(A,B):
    def __init__(self,b,d):
        A.__init__(self,b)
        B.__init__(self,d)

obj=C(99,109)
print(obj.b,obj.c,obj.d)
