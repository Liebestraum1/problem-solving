import sys

N, K = map(int, sys.stdin.readline().split())

def comb(N, K):
    if K == 0 or N==K:
        return(1)
    if N-K < K:
        K = N-K
    Ntemp = N
    for i in range(1, K):
        Ntemp -=1
        N *= Ntemp
        K *= i
    return(N//K)

print(comb(N,K)%10007)