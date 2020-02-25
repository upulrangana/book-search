from core.book import Book
from ui import MainApp

book = Book('./data/book.txt', min_paragraph_length=50)

app = MainApp(book)
app.mainloop()
