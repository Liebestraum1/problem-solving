n = int(input())

def star(n):
    if n == 1:
        return '*'
    else:
        return ([i * 3 for i in star(n//3)]
        + [i + n//3 * ' ' + i for i in star(n//3)]
        + [i * 3 for i in star(n//3)])

print(*star(n), sep='\n')