import os
from tkinter import *
from tkinter import messagebox
from whoosh.fields import Schema, TEXT, ID
from whoosh import index, highlight

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