# 1. Stop list at specific value
for ch in ["x", "y", "z"]:
    if ch == "y":
        break
    print(ch)

# 2. Stop range early
for i in range(15):
    if i == 6:
        break
    print(i)

# 3. Finding first negative number
for n in [5, 3, -1, 7]:
    if n < 0:
        print(n)
        break

# 4. Character search in string
for c in "Python":
    if c == "t":
        break
    print(c)

# 5. Nested break (breaks only inner loop)
for a in range(3):
    for b in range(5):
        if b == 2:
            break
    print(a)
