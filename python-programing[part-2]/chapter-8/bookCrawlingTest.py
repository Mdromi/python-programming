# python3 chapter-8/bookCrawlingTest.py

import requests
import re
import sys

# get categories
url = 'http://books.toscrape.com/index.html'
response = requests.get(url)

if response.ok is False:
    sys.exit('Could not get response from server')

page_content = response.text

# result = re.findall(r'<div class="side_categories">(.*?)</div>', page_content, re.M | re.DOTALL)
category_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?<', re.M | re.DOTALL)

result = re.findall(category_pat, page_content)

# for item in result:
#     print(item)

# print(len(result))

# category books link
book_pat_url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
book_pat_response = requests.get(url)

if book_pat_response.ok is False:
    sys.exit('Could not get response from server')

book_pat_page_content = book_pat_response.text
book_pat_page_content = book_pat_page_content.replace('\n', ' ')
book_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')
book_pat_result = re.findall(book_pat, book_pat_page_content)
# for item in book_pat_result:
#     print(item)


# next page link
next_page = re.findall(r'<li class="next"><a href="(.*?)">next</a></li>', book_pat_page_content)
# print(next_page)

# url convert
url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
i = url.rfind('/')
url = url[0:i+1] + next_page[0]


print(url)