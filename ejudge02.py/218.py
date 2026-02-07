n = int(input())
arr = [input().strip() for _ in range(n)]

first_pos = {}
for i, s in enumerate(arr, 1):
    if s not in first_pos:
        first_pos[s] = i

for s in sorted(first_pos):
    print(s, first_pos[s])
