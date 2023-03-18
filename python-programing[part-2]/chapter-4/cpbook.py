# python3 chapter-4/cpbook.py

import requests
import sys

base_url = 'http://subeen.com/download/'

info_dt = {'name': 'Romi', 'email': 'ro@email.com', 'country': 'Bangladesh'}

url = base_url + 'process.php'

res = requests.post(url, data=info_dt)

if res.ok is False:
    sys.exit('Error downloading the file.')

with open('chapter-4/cpbook.pdf', 'wb') as fb:
    fb.write(res.content)

print('Book download complete!')