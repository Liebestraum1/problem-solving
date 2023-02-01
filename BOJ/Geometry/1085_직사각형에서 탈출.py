x, y, w, h = map(int, input().split())

print(min(min(x, w-x, key=abs), min(y, h-y, key=abs)))