from study8_3 import text
import csv

with open('test.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book)
        
