# python3 chapter-5/readFile.py
import io

file_name = 'chapter-5/file.txst'
mode = 'r'

lines = ['This is first line', 'This is second line', 'This is third line']

with open(file_name, 'w') as fp:
    for line in lines:
        fp.write(line + '\n')

try:
    with open(file_name, mode) as fp:
        for line in fp:
            print(line)
except io.UnsupportedOperation as e:
    print('Are you sure', file_name, 'is readble?', e)
except:
    print(file_name, 'not found. Please check if the file\'s name is correct')
