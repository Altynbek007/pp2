from functools import reduce

# Sample data
numbers = [1, 2, 3, 4, 5, 6]
strings = ["1", "2", "three", "4"]

# 1. map() → apply a function to all elements
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# 2. filter() → keep elements that satisfy condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 3. reduce() → aggregate values into one result
sum_all = reduce(lambda x, y: x + y, numbers)
product_all = reduce(lambda x, y: x * y, numbers)
print("Sum:", sum_all)
print("Product:", product_all)

# 4. enumerate() → index + value
print("\nUsing enumerate:")
for index, value in enumerate(numbers):
    print(f"Index {index}: Value {value}")

# 5. zip() → pair elements from multiple lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

print("\nUsing zip:")
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# 6. Type checking and conversions
print("\nType checking and conversions:")

converted_numbers = []
for item in strings:
    if item.isdigit():  # check if string is numeric
        num = int(item)  # convert to int
        converted_numbers.append(num)
    else:
        print(f"Skipping non-numeric value: {item}")

print("Converted numbers:", converted_numbers)

# Additional type checking
for item in converted_numbers:
    if isinstance(item, int):
        print(f"{item} is an integer")