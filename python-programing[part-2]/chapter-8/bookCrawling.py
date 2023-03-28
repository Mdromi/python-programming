# python3 chapter-8/bookCrawling.py

import logging
import requests
import re
import sys
import csv

def get_category_list(content):
    """get_category_list takes content of home page and returns a list of categories and their urls"""
    return category_pat.findall(content)

def get_book_list(content):
    """get_book_list takes content of book list page and returns a list of books (name and url)"""
    pass

def get_product_details(content):
    """get_product_details takes content of product page, press the page and returns details about a product"""
    pass

def get_page_content(url):
    """get_page_content takes a url and return the content of the page"""
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logging.error(e)
    
    if response.ok:
        return response.text
    
    logging.error('Can not get content from URL:' + url)
    return None

def get_next_page(content):
    """checks the content of the book list page and return link of the next page, return None, if there is no more next page"""
    result = next_page_pat.findall(content)
    if len(result) == 0:
        return None
    i = url.rfind('/')
    return url[0:i+1] + result[0]

def scrape_book_info(book_info, category_name):
    """gets the content of a book details page, and press different components and store the info"""

def crawl_category(category_name, category_url):
    """crawl a particular category of books"""
    while True:
        content = get_page_content(category_url)
        bool_list = get_book_list(content)

        for book in bool_list:
            scrape_book_info(book, category_name)
        
        if get_next_page(content) is None:
            break

def crawl_website():
    """crawl_website() is the main function that coordinates the whole crawling task"""
    url = 'http://books.toscrape.com/index.html'
    host_name = 'books.toscrape.com'

    content = get_page_content(url)
    if content is None:
        logging.critical('Failed to get content from ' + url)
        sys.exit(1)

    category_list = get_category_list(content)

    for category in category_list:
        category_url, category_name = category 
        category_url = 'http://' + host_name + '/' + category_url
        print(category_url)
        sys.exit(1)
        crawl_category(category_name, category_url)


if __name__ == '__main__':
    # Compile different regular expression patterns
    category_pat = re.compile(r'<li>\s*<a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*?<', re.M | re.DOTALL)
    next_page_pat = re.compile(r'<li class="next"><a href="(.*?)">next</a></li>')

    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='chapter-8/book_crawler.log', level=logging.DEBUG)

    with open("chapter-8/books_list.csv", 'w') as csvf:
        csv_writer = csv.DictWriter(csvf, fieldnames=['Name', 'Category', 'UPC', 'URL', 'ImageURl', 'Price', 'Availability', 'Description'])
        csv_writer.writeheader()
        crawl_website()