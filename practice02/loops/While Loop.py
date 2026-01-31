# 1. Count to 4
i = 1
while i <= 4:
    print(i)
    i += 1

# 2. Counting down from 5
i = 5
while i > 0:
    print(i)
    i -= 1

# 3. Loop through a string index
text = "OK"
i = 0
while i < len(text):
    print(text[i])
    i += 1

# 4. Powers of 3
n = 1
while n < 30:
    print(n)
    n *= 3

# 5. Removing items from list
items = ["a", "b", "c"]
while items:
    print(items.pop(0))
