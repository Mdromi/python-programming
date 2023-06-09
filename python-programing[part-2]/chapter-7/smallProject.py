# python3 chapter-7/smallProject.py

import re
import os
import requests
import sys

# create main directory
def create_directory(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name, 'already exists')

# download image
def download_image(img_url, file_name):
    print('Downloading', img_url)
    r = requests.get(img_url)

    with open(file_name, 'wb') as f:
        f.write(r.content)
    print('Img Download Complete')

# img url covert to directory name
def get_directory_name(regex, url):
    result = re.findall(regex, url)
    dir_name = "_".join(result[0])
    return dir_name

# main function
def process():
    # create home directory
    main_dir = 'chapter-7/data'
    create_directory(main_dir)

    main_url = 'http://dimik.pub/'
    response = requests.get(main_url)
    if response.ok is False:
        sys.exit('Could not get response from server')

    page_content = response.text

    regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', re.S)

    result = re.findall(regexp, page_content)

    dir_regex = re.compile(r'book/(\d+)/(\w+)-(\w+)')


    for item in result:
        name = item[2]
        url = item[0]
        img_url = item[1]

        dir_name = main_dir + "/" + get_directory_name(dir_regex, url)
        create_directory(dir_name)

        file_name = dir_name + "/" + "info.txt"
        print(file_name)
        with open(file_name, 'w') as fp:
            fp.write(name + '\n')
            fp.write(url)
        
        img_file_name = dir_name + "/" + 'image.png'
        download_image(img_url, img_file_name)


if __name__ == '__main__':
    process()