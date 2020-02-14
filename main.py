from core.paragraph_parser import Book
from core.search_engine import search_book

book = Book('./data/book.txt', min_paragraph_length=50)

print('Starting up')
results = search_book('same sex marriage', book)
for r in results:
    print(r.body)
