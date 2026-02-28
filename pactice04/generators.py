#1
def square_gen(N):
    for i in range(N + 1):
        yield i * i

N = int(input())
for x in square_gen(N):
    print(x)

#2
def evens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(x) for x in evens(n)))

#3
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for x in div_by_3_and_4(n):
    print(x)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input())
b = int(input())

for val in squares(a, b):
    print(val)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for x in countdown(n):
    print(x)