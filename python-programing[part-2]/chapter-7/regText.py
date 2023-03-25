# python3 chapter-7/regText.py

import re

with open("chapter-7/text.txt", "r") as f:
    text = f.read()

result = re.findall(r'^.*?$', text, re.M)
print(result)

s = '<li>Tamim</li><li>Sakib</li><li>Mahmudullah</li><li>Mominul</li>'
result = re.findall(r'<li>(.*?)</li>', s)
print(result)

text = 'This is line 1. Date is 2017/06/01. And there is another date : 2017-07-01. The third and final date is 2017/08/03'
pat = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
result = pat.findall(text)
print(result)


s = '22/07/2017, 20/01/4303, 23/09/2019'
result = re.sub(r'(\d{2})[-/](\d{2})[-/](\d{4})', r'\3-\2-\1', s)
print(result)