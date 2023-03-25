# python3 chapter-7/email.py

import re

emailList = 'Email your feedback here: book@subeen.com py.book@subeen.com book_py@subeen.com'
result = re.findall(r'([.\w]+@\w+[.]\w+)', emailList)
print(result)


email = 'book at subbeen.com, book At subbeen.com, book (at) subbeen dot com, book [at] subbeen [dot]com,'
regex = r'\b([A-Za-z0-9._%+-]+)(\s*(?:\[(?:at|dot)\]|\(?[aA][tT]\)?|\s)*)+([A-Za-z]{2,})\b'

formatted_email = re.sub(regex, lambda match: match.group(1) + '@' + match.group(3).replace('dot', '.').replace('[dot]', '.').replace('at', '@').replace('[at]', '@').replace('(at)', '@').replace(' ', ''), email)

print(formatted_email)