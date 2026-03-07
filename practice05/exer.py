#1
import re

pattern = r'^ab*$'

s = input()

if re.match(pattern, s):
    print("Match")
else:
    print("No match")

#2
import re

pattern = r'^ab{2,3}$'

s = input()

if re.match(pattern, s):
    print("Match")
else:
    print("No match")

#3
import re

pattern = r'\b[a-z]+_[a-z]+\b'

s = input()
matches = re.findall(pattern, s)

print(matches)

#4
import re

pattern = r'\b[A-Z][a-z]+\b'

s = input()
matches = re.findall(pattern, s)

print(matches)

#5
import re

pattern = r'^a.*b$'

s = input()

if re.match(pattern, s):
    print("Match")
else:
    print("No match")

#6
import re

s = input()
result = re.sub(r'[ ,.]', ':', s)

print(result)

#7
import re

def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

s = input()
print(snake_to_camel(s))

#8
import re

s = input()
parts = re.split(r'(?=[A-Z])', s)

parts = [p for p in parts if p]
print(parts)

#9
import re

s = input()
result = re.sub(r'(?<!^)([A-Z])', r' \1', s)

print(result)

#10
import re

s = input()
result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()

print(result)