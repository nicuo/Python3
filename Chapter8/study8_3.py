text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''

with open('test.csv', 'wt') as outfile:
    outfile.write(text)
    
