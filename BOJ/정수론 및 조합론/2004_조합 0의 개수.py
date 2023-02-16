import sys

N, K = map(int, sys.stdin.readline().split())

def exp(x):
    def five_exp(x, param=5):
        if param > x:
            return 0
        return x//param + five_exp(x, param*5)
    
    def two_exp(x, param=2):
        if param > x:
            return 0
        return x//param + two_exp(x, param*2)
    return [two_exp(x), five_exp(x)]

print(min([exp(N)[0] - exp(K)[0] - exp(N-K)[0], exp(N)[1] - exp(K)[1] - exp(N-K)[1]]))