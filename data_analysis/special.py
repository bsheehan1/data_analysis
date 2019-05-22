import math

def  pochhammer(x,n):
    '''calculate Pochhammer symbol with calculation taken from:
    http://mathworld.wolfram.com/PochhammerSymbol.html
    '''
    y = 1
    for i in range(n):
        y *= x
        x += 1
    return y

def beta(a,b):
    '''calculate beta function'''
    y = math.gamma(a)*math.gamma(b)/math.gamma(a+b)
    return y
    
def betai(x,a,b,p=1/2**32):
    '''calculate incomplete beta function to precision p by series taken from:
    http://mathworld.wolfram.com/IncompleteBetaFunction.html
    '''    

    y = 0
    i = 0
    while True:
        num = pochhammer(1-b,i)
        inc = num/(math.factorial(i)*(a+i))*x**i
        y += inc
        i += 1
        if (inc/y < p):
            break
    y *= x**a
    return y

def betain(x,a,b,n):
    '''calculate incomplete beta function by n interations of series taken from:
    http://mathworld.wolfram.com/IncompleteBetaFunction.html
    '''
    s = 0
    for i in range(n):
        num = pochhammer(1-b,i)
        inc = num/(math.factorial(i)*(a+i))*x**i
        s += inc
    s *= x**a
    return s

def betaireg(x,a,b):
    y = betai(x,a,b)/beta(a,b)
    return y
    
