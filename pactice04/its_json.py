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