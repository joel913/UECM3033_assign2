import numpy as np
ITERATION_LIMIT = 10
#Your optional code here
#You can import some modules or create additional functions
def LUdecomp(X):
       n=len(X)
       for z in range(0, n-1):
        for k in range(z+1, n):
            if X[k,z]!= 0.0:
                lam = X[k,z] / X[z,z]
                X[k, z+1:n] = X[k, z+1:n] - lam * X[z, z+1:n]
                X[k, z] = lam
        return X


def lu(X,y):
      X=LUdecomp(X)
      n = len(X)
      for z in range(1,n):
           y[z] = y[z] - np.dot(X[z,0:z], y[0:z])
           y[n-1]=y[n-1]/X[n-1, n-1]
      for z in range(n-2, -1, -1):
           y[z] = (y[z] - np.dot(X[z,z+1:n], y[z+1:n]))/X[z,z]
      return y
       
def sor(X, y):
    sol = []
    omega = 1.03
    
    f = np.zeros_like(y)
    for itr in range(ITERATION_LIMIT):
        for l in range(len(y)):
            sums = np.dot( X[l,:], f )
            f[l] = f[l] + omega*(y[l]-sums)/X[l,l]
    # Edit here to implement your code
    return list(sol)

def solve(X, y):
    condition = np.count_nonzero(X) > 1/2 *len(X)  # State and implement your condition here
    if condition:
        print('Solve by lu(X,y)')
        return lu(X,y)
    else:
        print('Solve by sor(X,y)')
        return sor(X,y)

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    X = np.array([[2,1,6],[8,3,2],[1,5,1]]).astype(float)
    y = np.array([9, 13, 7]).astype(float)
    
    sol = np.linalg.solve(X,y)
    solve(X,y)
    print(sol)
    
    X =np.array ([[6566, -5202, -4040, -5224, 1420, 6229],
                  [4104, 7449, -2518, -4588,-8841, 4040],
                  [5266,-4008,6803, -4702, 1240, 5060],
                  [-9306, 7213,5723, 7961, -1981,-8834],
                  [-3782, 3840, 2464, -8389, 9781,-3334],
                  [-6903, 5610, 4306, 5548, -1380, 3539.]]).astype(float)
    y =np.array( [ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]).astype(float)
    sol = np.linalg.solve(X,y)
    solve(X,y)
    print(sol)