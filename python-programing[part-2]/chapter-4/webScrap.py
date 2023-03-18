# python3 chapter-4/webScrap.py

import requests
import os
import webbrowser as wb

url = 'https://www.freecodecamp.org/news/tag/blog/'

res = requests.get(url)
print(res.ok)
print(res.status_code)
print(res.reason)

with open ('chapter-4/result.html', 'w') as f:
    f.write(res.text)

file_path = os.path.realpath('chapter-4/result.html')
print(file_path)

wb.open('file://' + file_path)