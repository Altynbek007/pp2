n = int(input())
a = {}
for i in range(n):
    st = input()
    if st in a:
        pass
    else:
        a[st] = (i+1)
sorted_d = dict(sorted(a.items()))
for x in sorted_d:
    print(x, a[x])