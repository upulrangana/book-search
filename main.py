from core.paragraph_parser import Book
from ui import MainApp

book = Book('./data/book.txt', min_paragraph_length=50)

# results = book.search('same sex marriage')
# for i, r in enumerate(results):
#     print(f'({i + 1})\n{r.body[: 500]}...')

app = MainApp(book)
app.mainloop()
