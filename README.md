## Application flow

1. `/main.py` is the entry point of the program
2. `/main.py` creates a new `Book` class instance, and passes it into a new `MainApp` instance
3. `MainApp` class is located at `/ui/main_app.py`, it is the UI of the application.
4. `MainApp` uses `Book` to get search results, and displays them on the UI
5. `Book` class at `/core/book` reads **/data/book.txt** and loads all the paragraphs.
6. when `Book.search(query)` function is called, the book uses `/core/search_engine.py` to get the search results
7. the `Book` returns a list of `SearchResult` instances as the results. that class is at `/core/search_result.py`

## technologies used

1. `sklearn` python library
    - used for generating a tf–idf matrix (read about it, link below)
2. `pandas` python library
    - this library makes dealing with datasets, data tables etc. easier
3. `numpy` python library
    - this library used by `sklearn` python package
    - we also use it to easily select most matching search results
4. `tkinter` python library
    - tkinter is used for generating the UI, and the user interactions

## Academic topics used

TAKE A LOOK AT THIS ARTICLE: 
https://medium.com/@deangelaneves/how-to-build-a-search-engine-from-scratch-in-python-part-1-96eb240f9ecb

1. tf-idf
    - In information retrieval, tf–idf or TFIDF, short for term frequency–inverse document frequency, is a numerical 
    statistic that is intended to reflect how important a word is to a document in a collection or corpus.
2. cosine similarity