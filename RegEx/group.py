import re

s = "Welcome to time now"

# here x is the match object
res = re.search(r"\D{10} t", s)

print(res.group())
