# python3 chapter-4/downloadPic.py

import requests
import sys

# img_url = 'http://prowebscraping.com/wp-content/uploads/2015/09/web-scraping-process1.png'

img_url = sys.argv[1]
file_name = 'chapter-4/' + sys.argv[2]

req = requests.get(img_url)

with open (file_name, 'wb') as f:
    f.write(req.content)