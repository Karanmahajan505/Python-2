import re
import RE
regex = r'^The'
str = RE.content3()

for string in str:
    if re.match(regex,str):
         print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')     