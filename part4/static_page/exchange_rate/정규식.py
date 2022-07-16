import re

s = 'hi'
print(re.match(r'hi', s))
print(re.match(r'hey', s))
print(re.match(r'h.', s))