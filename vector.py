import numpy as np
import collections.abc

    
class Vec:
    def __init__(self, array):
        self.vec = np.array(array)
        self.normalised = False
        
    def __len__(self):
        return len(self.vec)
    
    def __abs__(self):
        return np.sum(np.square(self.vec)) ** 0.5
    
    def __str__(self):
        return f"{self.vec}"
    
    def __bool__(self):
        return len(self.vec) > 0
    
    def __add__(self, thing):
        
        if isinstance(thing, Vec):
            return Vec(self.vec + thing.vec)
        else:
            thing = np.array(thing)
            return Vec(self.vec + thing)
        
    def __iadd__(self, thing):
        self.vec = self.__add__(thing)
        return self
        
    def __radd__(self, thing):
        return self.__add__(thing)
        
    def __sub__(self, thing):
        
        if isinstance(thing, Vec):
            return Vec(self.vec - thing.vec)
        else:
            thing = np.array(thing)
            return Vec(self.vec - thing)
    
    def __isub__(self, thing):
        self.vec = self.__sub__(thing)
        return self
        
    def __rsub__(self, thing):
        return self.__sub__(thing)
        
    def __mul__(self, thing):
        
        if isinstance(thing, Vec):
            return Vec(self.vec * thing.vec)
        
        elif isinstance(thing, collections.abc.Sequence):
            thing = np.array(thing)
            return Vec(self.vec * thing)
        
        elif isinstance(thing, int) or isinstance(thing, float):
            return Vec(self.vec * thing)
        else:
            raise NotImplementedError(f"Type {type(thing)} not implemented for using operator '*'")
            
    def __imul__(self, thing):
        self.vec = self.__mul__(thing)
        return self
    
    def __rmul__(self, thing):
        return self.__mul__(thing)
        
    def __truediv__(self, thing):
        
        if isinstance(thing, Vec):
            return Vec(self.vec / thing.vec)
        
        elif isinstance(thing, collections.abc.Sequence):
            thing = np.array(thing)
            return Vec(self.vec / thing)
        
        elif isinstance(thing, int) or isinstance(thing, float):
            return Vec(self.vec / thing)
        else:
            raise NotImplementedError(f"Type {type(thing)} not implemented for using operator '/'")
    
    def __itruediv__(self, thing):
        self.vec = self.__truediv__(thing)
        return self
        
    def __rtruediv__(self, thing):
        
        if isinstance(thing, Vec):
            return Vec(self.vec / thing.vec)
        
        elif isinstance(thing, collections.abc.Sequence):
            thing = np.array(thing)
            return Vec(self.vec / thing)
        
        elif isinstance(x, int) or isinstance(x, float):
            raise TypeError("Cannot divide scalar by a vector")
        else:
            raise NotImplementedError(f"Type {type(thing)} not implemented for using operator '/'")
            
    def __pow__(self, thing):
        return Vec(self.vec ** thing)
    
    def __matmul__(self, thing):
        if isinstance(thing, Vec):
            return Vec(self.vec @ thing.vec)
        
        elif isinstance(thing, collections.abc.Sequence):
            thing = np.array(thing)
            return Vec(self.vec @ thing)
        
        elif isinstance(x, int) or isinstance(x, float):
            return TypeError("Cannot matmul scalar by a vector")
        else:
            raise NotImplementedError(f"Type {type(thing)} not implemented for using operator '*'")
            
    def __xor__(self, thing):
        # This is used as a dot product (the ^ symbol)
        
        if isinstance(thing, Vec):
            return np.dot(self.vec, thing.vec)
        elif isinstance(thing, collections.abc.Sequence):
            thing = np.array(thing)
            return np.dot(self.vec, thing)
        else:
            raise NotImplementedError(f"Type {type(thing)} not implemented for using operator '^'")
        
        
    def __getitem__(self, i):
        return self.vec[i]
    
    def __setitem__(self, i, val):
        self.vec[i] = val
    
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        
        if self.index < self.__len__():
            val = self.vec[self.index]
            self.index += 1
            return val
        raise StopIteration

        
    def mag2(self):
        return np.sum(np.square(self.vec))

    
    def return_normalised(self):
        return self / self.__abs__()
    
    def normalise(self):
        if self.normalised:
            return
        else:    
            self.vec = self.return_normalised()
            return

    
