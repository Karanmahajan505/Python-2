import re

s = "Atharv.Babar"

match = re.search(r'.',s)
print("Without using ",match)
match = re.search(r'\.',s)
print("With using ",match)
