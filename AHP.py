import numpy as np

def ahp_daily(M, Q):
    C = np.zeros(len(M))
    C[0] = M[0]
    for t in range(len(M)-1):
        C[t+1] = ((1-Q[t]/2.)*C[t] + M[t]*Q[t])/(1+Q[t]/2)
    return C

def ahp_tick(P, Rho):
    C = np.zeros(len(P))
    C[0] = P[0]
    for t in range(len(P)-1):
        C[t+1] = C[t] + P[t]*Rho[t]/(1+Rho[t])
    return C

if __name__ == '__main__':
    N = 1000
    Q = np.random.lognormal(size=N)
    dM = np.random.normal(size=N, scale=0.01)
    M0 = 100
    M = M0*np.cumprod(1+dM)

    C = ahp_daily(M, Q)
    print C


    Rho = np.random.lognormal(size=N)
    dP = np.random.normal(size=N, scale=0.01)
    P0 = 100
    P = P0 * np.cumprod(1 + dP)
    C = ahp_daily(P, Rho)
    print C