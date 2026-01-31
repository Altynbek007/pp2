# 1. Skip a specific number
for n in [4, 5, 6]:
    if n == 5:
        continue
    print(n)

# 2. Skip specific character
for ch in "Programming":
    if ch == "g":
        continue
    print(ch)

# 3. Print only even numbers
for i in range(6):
    if i % 2 != 0:
        continue
    print(i)

# 4. Skip last element
for i in range(5):
    if i == 4:
        continue
    print(i)

# 5. Skip based on condition
for word in ["hide", "show", "hide"]:
    if word == "hide":
        continue
    print(word)
