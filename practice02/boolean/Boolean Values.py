# 1. Direct boolean assignment
is_active = False

# 2. bool() with a string (non-empty is True)
print(bool("hello"))  # True

# 3. bool() with empty string (False)
print(bool(""))  # False

# 4. bool() with zero (False)
print(bool(0))  # False

# 5. Logical result of a function
def is_valid():
    return 5 > 3
print(is_valid())  # True
