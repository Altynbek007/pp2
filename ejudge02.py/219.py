n = int(input())
episodes = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    episodes[s] = episodes.get(s, 0) + k

for s in sorted(episodes):
    print(s, episodes[s])
