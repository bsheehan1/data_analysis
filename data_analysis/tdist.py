import math
import numpy as np

import special

def t_test(X1,X2):
    X1_bar = np.mean(X1)
    X2_bar = np.mean(X2)
    Z = abs(X1_bar - X2_bar)
    s1 = np.std(X1)
    s2 = np.std(X2)
    n1 = len(X1)
    n2 = len(X2)
    s = np.sqrt((s1**2)/(n1-1)+(s2**2)/(n2-1))
    t = Z/s
    v = n1 + n2 - 2
    return t, v
    
def p_value(t,v):
    x = v/(t**2+v)
    y = special.betaireg(x,v/2,0.5)
    return y
    

if __name__ == '__main__':
    x1 = [1,2,3]
    x2 = [10,11,12]
    y = t_test(x1,x2)
    print(y)
    x = p_value(5.913,6)
    print(x)
