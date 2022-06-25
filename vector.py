import numpy as np

class Vec:
    def __init__(self, array):
        self.vec = np.array(array)
        self.normalised = False
    def x():
        return self.vec[0]
    def y():
        return self.vec[1]
    def z():
        return self.vec[2]
        
    def mag2(self):
        return np.sum(np.square(self.vec))
    
    def mag(self):
        return mag2(self) ** 0.5
    
    def dot(self, dotWith):
        return np.dot(self.vec, dotWith)
    
    def times(self, scalar):
        return scalar * self.vec
    
    def return_normalised(self):
        return self.vec / self.mag(self)
    
    def normalise(self):
        if self.normalised:
            return
        else:    
            self.vec = self.return_normalised(self)
            return
    
    def add(self, addWith):
        return self.vec + addWith
    
    