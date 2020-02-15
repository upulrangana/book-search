from core.paragraph_parser import Book
from core.search_engine import search_book

book = Book('./data/book.txt', min_paragraph_length=50)

print('Starting up')
query = 'same sex marriage'
results = search_book(query, book)
print(f'===== Search results for "{query}" =====')
for i, r in enumerate(results):
    print(f'({i + 1})\n{r.body[: 500]}...')
