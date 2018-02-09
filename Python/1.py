class A:
    a=10
    def __init__(self,a1):
        self.a1=a1

class B:
    a=20
    def __init__(self,a1):
        self.a1=a1


class C(B,A):
    d=30
    def __init__(self,d,a1):
        super().__init__(a1)
        self.d=d

obj=C(50,60)
print(obj.a,obj.a1,obj.d)
