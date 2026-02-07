n = int(input())
arr = list(map(int, input().split()))

freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

max_count = max(freq.values())
candidates = [x for x, c in freq.items() if c == max_count]

print(min(candidates))
