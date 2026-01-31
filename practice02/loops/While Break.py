# 1. Exit at specific value
i = 2
while i < 15:
    if i == 8:
        break
    print(i)
    i += 2

# 2. One-time loop simulation
while True:
    print("Running once")
    break  # Stop loop

# 3. Stop when threshold reached
count = 5
while count <= 50:
    if count == 25:
        break
    count += 5

# 4. Finding first multiple
n = 1
while n < 40:
    if n % 9 == 0:
        break
    n += 1
# 5. Stop when value becomes negative
num = 10
while num >= 0:
    if num == 3:
        break
    print(num)
    num -= 1
