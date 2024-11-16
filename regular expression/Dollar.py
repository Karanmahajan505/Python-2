import RE
import re

pattern = r"World!$"
s = RE.content2()

match = re.search(pattern,s)

if match:
    print("Match Found")
else:    
    print("Match not found")    