# python3 chapter-8/workCSV.py

import csv

field_name = ['Name', 'Author', 'Publisher', 'Price', 'category']

book1 = ['Computer programming, part 1', 'Subeen', 'Onnorokm prokasoni', '230', 'Programming']
book2 = ['Computer programming 2', 'Subeen', 'Onnorokm prokasoni', '230', 'Programming']
book3 = ['Computer programming 3', 'Subeen', 'Onnorokm prokasoni', '230', 'Programming']

book_list = [book1, book2, book3]

with open("chapter-8/books.csv", 'w') as csvf:
    csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_name)
    for book in book_list:
        csv_writer.writerow(book)


book1 = {"Name": 'Computer programming, part 1', "Author":'Subeen', "Publisher":'Onnorokm prokasoni', "Price":'230', "category":'Programming'}
book2 = {"Name": 'Computer programming 2', 'Author':'Subeen', 'Publisher':'Onnorokm prokasoni', 'Price':'230', 'category':'Programming'}
book3 = {'Name': 'Computer programming 3', 'Author':'Subeen', 'Publisher':'Onnorokm prokasoni', 'Price':'230', 'category':'Programming'}

book_list = [book1, book2, book3]
with open("chapter-8/books_list.csv", 'w') as csvf:
    csv_writer = csv.DictWriter(csvf, fieldnames=field_name)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)

with open("chapter-8/books_list.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)