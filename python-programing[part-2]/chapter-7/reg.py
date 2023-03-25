# python3 chapter-7/reg.py

import re

s = 'Bangladesh is our homeland'
text = 'House number: 5, phone number: 017 12345678'
multipleText = 'Multiple phone number: 01711111111, 01711111111, 01811111111, 01911111111, 00000000000, 111111111111, 123-123'


match = re.search('....', s)
match = re.search('o\w\w', s)
match = re.search('B\w+h', s)
match = re.search('B\w.+', s)
match = re.search('B\w.+?h', s)

match = re.search('\d{3}\s*\d{8}', text)

result = re.findall(r'\d{3}\s*\d{8}', multipleText)
result = re.findall(r'01[56789]\s*\d{8}', multipleText)


print(match.group())
print(result)