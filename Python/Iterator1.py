class power:
    def __init__(self,max):
        self.max=max

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<=self.max:
            res=4**self.n
            self.n+=1
            return res
        raise stopiteration
