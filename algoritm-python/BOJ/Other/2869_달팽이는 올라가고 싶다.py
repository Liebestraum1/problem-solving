a, b, v = map(int, input().split())
print(int((v-b) / (a-b)) if (v-b) % (a-b) == 0 else int((v-b) / (a-b) + 1))