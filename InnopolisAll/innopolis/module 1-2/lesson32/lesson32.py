import re

sentence = "1357 hello world!"
r = re.match(r'\d+', sentence)
print(r.group(0))
print(r)