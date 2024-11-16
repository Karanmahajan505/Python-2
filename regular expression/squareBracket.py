import RE
import re

s = RE.content()
pattern = "[a-m]"

result = re.findall(pattern,s)

print("Find the Pattern : ",result)