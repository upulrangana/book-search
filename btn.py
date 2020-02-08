from tkinter import *
from tkinter import messagebox
from whoosh.fields import Schema, TEXT, ID
from whoosh import index, highlight
import os.path


def clicked():

    def search(string1):
        if not os.path.exists("indexdir"):
            os.mkdir("indexdir")
        schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))
        ix = index.create_in("indexdir", schema)

        writer = ix.writer()
        writer.add_document(title=u"my 1st short length try", content=u"hello",
                            path=u"/b")
        writer.add_document(title=u"My 1st long text document",
                            content=u"This is my python document! hello big world1 is the good place for live with  who we know very well",
                            path=u"/a")
        writer.add_document(title=u"my 2nd try",
                            content=u"This is the second example hello world2 qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq wwwwwwwwwwwww.",
                            path=u"/b")
        writer.add_document(title=u"my 3rd try",
                            content=u"This is the second example hello world3 wwwwwwwwwww eeeeeeeeeeeeeeeee rrrrrrrrrrr.",
                            path=u"/b")
        writer.add_document(title=u"my 4th try",
                            content=u"This is the second example hello world4 rttttttttttttttt ggggggggggggggg vvvvvvvvvvvvvvv.",
                            path=u"/b")
        writer.add_document(title=u"Third time's the charm",
                            content=u"More examples. Examples are many.The breeding season for frogs usually occurs during the spring in temperate climates and during the rainy season in tropical climates. When male frogs are ready to breed, they often use loud croaking calls to attract partners. Males produce these calls by filling a vocal sac with air and moving the air back and forth to create a chirp-like sound.Many species lay their eggs in calm water among vegetation, where the eggs can develop in relative safety. The female frog lays numerous eggs in masses that tend to clump together in groupings known as spawn. As she deposits the eggs, the male releases sperm onto the eggs and fertilizes them In many species of frogs, the adults leave the eggs to develop without further care. But in a few species, parents remain with the eggs to look after them as they develop. As the fertilized eggs mature, the yolk in each egg splits into more and more cells and begins to take the form of a tadpole, the larva of a frog. Within one to three weeks, the egg is ready to hatch, and a tiny tadpole breaks free.",
                            path=u"/c")

        writer.commit()

        from whoosh.qparser import QueryParser

        with ix.searcher() as searcher:
            # string1='hello'
            query = QueryParser("content", ix.schema).parse(string1)
            results = searcher.search(query, terms=True)
            results.fragmenter = highlight.PinpointFragmenter()
            results.formatter = highlight.UppercaseFormatter()
            # results.fragmenter.charlimit = 1000000
            listbox = Listbox(window)
            listbox.pack(expand=1, fill="both")

            for hit in results:
                print(hit["title"])
                # Assume "content" field is stored
                print(hit.highlights("content"))
                i=hit.highlights("content")
                listbox.insert(END, i)
                # attach listbox to scrollbar

            listbox.config()

    search_text = 'hel'
    search(e.get())
    # messagebox.showinfo('Predicted Answer', e.get())
window = Tk()
window.configure(background="blue")
window.title("BOOK SEACH ")

window.geometry('650x600')
lbl = Label(window, text="SEARCH BOX", background="green")
lbl.pack(fill=BOTH)
e = Entry(window)
e.pack()
btn = Button(window, text="Search", command=clicked)
btn.pack(fill=BOTH, padx=40, pady=20)
window.mainloop()


# ****************

# # tkinter is the module to create a GUI
# import tkinter
# from ui import *
#
#
# # we create the window here and the root to which we will attach the button
# # this is an istance of the class Tk(), the main class of tkinter
# root = tkinter.Tk()
# inp = Inputbox(text="Search")
# print(inp.get)
# # before we create the button, we make a function that
# # contains the action that takes place when the button's clicked
# # the name of the function can be anything, I chose clicked.
# def clicked():
# 	print("Hello world")
# 	# let's make something to the button
# 	# you can change the attributes of the button this way
# 	# putting the name of the attribute in square brackets and apostrophes
# 	button['text'] = "I have been clicked, dude"
#
# # here we create the BUTTON ====================================
# # We give a name to the istance of Button, the class to create it
# button = tkinter.Button(root, text="Click me")
# # remember then to pack it, otherwise it is not visible
# button.pack()
#
# # now we give the name of the function that will handle the click
# button['command'] = clicked
# # notice that we could have placed 'command' above in the Button class istance
# # this is an alternative method
#
#
# # at the end of the code put the method to create the loop for the window
# # it is necessary
# root.mainloop()