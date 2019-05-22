import datastruct
import numpy as np

class LinearRegression:
    def __init__(self,X,Y,set_intercept=True):
        self.X = X
        self.Y = Y
        self.set_intercept = set_intercept

        self.calculate(self.X,self.Y,self.set_intercept)
        
    def calculate(self,X,Y,set_intercept):
        """
        Linear Regression via orthoganal projection theorem:
        beta = (X^T,X)^-1A^TY
        """
        X = np.array(X,dtype=float)
        Y = np.array(Y,dtype=float)
        if len(X.shape) == 1:
            X = np.array([X])
        if set_intercept==True:
            ones = np.ones(len(X),dtype=float)
            X = np.insert(X.T,0,1.,axis=0).T
        X_TxX = np.matmul(X.T,X)
        # If det = 0 then there are multiple solutions to regression
        if np.linalg.det(X_TxX) == 0:
            print("No unique solution")
            raise ValueError
        X_TxX_inv = np.linalg.inv(X_TxX)
        H = np.matmul(X_TxX_inv,X.T)
        HxY = np.matmul(H,Y)
        beta = HxY.flatten()
        # Analyze quality of least-squares model: SUM(e^2) = SUM(Y-Y_hat)^2
        Y = Y.flatten()
        n = len(Y)
        p = len(beta) - 1
        Y_hat = np.matmul(X,beta)
        e = Y - Y_hat
        sum_e_squared = np.matmul(e,e.T)
        # approximate sigma using s = SUM(e^2)/n-p-1
        SSres = sum_e_squared/(n-p-1) 
        s_y = np.sqrt(SSres)
        y_bar = np.mean(Y)
        Y_bar = np.ones(len(Y))
        Y_bar.fill(y_bar)
        residual = Y-Y_bar
        Stot = np.matmul(residual,residual.T)
        SStot = Stot/(n-p-1)
        # R^2 = Coefficient of Determination (Sum of Squares =: SS)
        R_squared = 1-(SSres/SStot)
        R_squared_adjusted = R_squared - p*(1-R_squared)/(n-p)
        self.beta = beta
        self.R_squared = R_squared
        self.R_squared_adjusted = R_squared_adjusted
        self.s_y = s_y
        return beta
    
if __name__ == '__main__':
    data = datastruct.DataStruct('./test/mlr.txt')
    x = data.x
    y = data.y
    lr = LinearRegression(x,y)
    print(lr.beta)
    print(" y = 2.679481654 x1 - 9.492751478·10-1 x2 - 1.311691652 x3 + 19.92017216")


