# 1. Skip number 4
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)

# 2. Skip odd numbers
i = 0
while i < 7:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

# 3. Skip negative values (print only positives)
i = -4
while i < 4:
    i += 1
    if i < 0:
        continue
    print(i)

# 4. Skip specific character in string
s = "world"
i = -1
while i < len(s) - 1:
    i += 1
    if s[i] == "o":
        continue
    print(s[i])

# 5. Skip until threshold reached
i = 0
while i < 12:
    i += 1
    if i <= 9:
        continue
    print(i)  # Prints 10, 11, 12
