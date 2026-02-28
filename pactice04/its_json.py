#1
import json

data = '{"name": "Ann", "age": 20}'

parsed = json.loads(data)

print(parsed["name"])
print(parsed["age"])

#2
import json

data = '{"name": "Ann"}'
parsed = json.loads(data)

print(parsed.get("age", "No age found"))

#3
import json

data = '["apple", "banana", "cherry"]'

parsed = json.loads(data)

print(type(parsed))

#4
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#5
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))