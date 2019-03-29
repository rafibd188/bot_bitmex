class Kolebanie(object):
    def __init__(self):
       # self.h=...
    def _raschet_(self):

    def first_proizvod(self,y):
        buf=(y[-1]-y[-2])/(self.h)
        return buf
    def second_proizvod(self,y):
        return (y[-1]-2*y[-2]+y[-3])/(2*(self.h)**2)

    def analise(self,y):
        if self.first_proizvod(y)>0:
            if self.second_proizvod(y)
