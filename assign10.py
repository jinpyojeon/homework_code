#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
import numpy as np 

Alice = {'name': 'Alice',
         'profession': 'Teacher',
         'age': 30 }

class Monoid():
    __metaclass__ = ABCMeta

    @abstractmethod
    def e(): pass 

    @abstractmethod
    def op(x, y): pass

class Matrix22():
    def __init__(self, a, b, c, d):
        self.mat = [a, b, c, d] 

    def __str__(self):
        return "[%d %d]\n[%d %d]" % (self.mat[0], self.mat[1], self.mat[2], self.mat[3]) 

class Matrix22Multiplication(Monoid):
    
    def e(self): 
        return Matrix22(1,0,0,1) # identity matrix

    def op(self, x, y):
        return Matrix22(x.mat[0] * y.mat[0] + x.mat[1] * y.mat[2], 
                        x.mat[0] * y.mat[1] + x.mat[1] * y.mat[3],
                        x.mat[2] * y.mat[0] + x.mat[3] * y.mat[2],
                        x.mat[2] * y.mat[1] + x.mat[3] * y.mat[3])
        

def main():

    F = Matrix22(1,1,1,0)
    mm = Matrix22Multiplication()
    print mm.op( mm.op(F, F), F)

    F_test = np.matrix('1 1; 1 0')
    print (F_test * F_test * F_test)

if __name__ == '__main__':
    main()
