n = int(input())
pans = [666]
digit = '0123456789'
stack = ['666']
while len(pans) < n:
    nans = []
    for i in stack:
        for j in digit:
            nans.extend([j + i, i + j])
    pans = list(set(map(int, pans + nans)))
    stack = nans
print(sorted(pans)[n-1])