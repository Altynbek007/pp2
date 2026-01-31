# 1. Multi-level grade check
points = 62
if points >= 85: print("Excellent")
elif points >= 60: print("Good")
else: print("Needs improvement")

# 2. Weather by temperature
temp = 5
if temp < 0: print("Freezing")
elif temp < 15: print("Cold")
else: print("Warm")

# 3. Comparing three values
a, b = 8, 8
if a > b: print("a is greater")
elif b > a: print("b is greater")
else: print("Values are equal")

# 4. User role check
role = "admin"
if role == "user": print("Standard access")
elif role == "admin": print("Full access")
else: print("No access")

# 5. Price category
price = 120
if price < 50: print("Cheap")
elif price < 100: print("Medium")
else: print("Expensive")
