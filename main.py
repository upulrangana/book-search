# -*- coding: utf-8 -*-
from whoosh.fields import Schema, TEXT, ID
from whoosh import index, highlight
# To create an index in a directory, use index.create_in:
import os.path
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))
ix = index.create_in("indexdir", schema)

writer = ix.writer()
writer.add_document(title=u"my 1st short length try", content=u"hello",
                    path=u"/b")
writer.add_document(title=u"My 1st long text document", content=u"This is my python document! hello big world1 is the good place for live with  who we know very well",
                    path=u"/a")
writer.add_document(title=u"my 2nd try", content=u"This is the second example hello world2 qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq wwwwwwwwwwwww.",
                    path=u"/b")
writer.add_document(title=u"my 3rd try", content=u"This is the second example hello world3 wwwwwwwwwww eeeeeeeeeeeeeeeee rrrrrrrrrrr.",
                    path=u"/b")
writer.add_document(title=u"my 4th try", content=u"This is the second example hello world4 rttttttttttttttt ggggggggggggggg vvvvvvvvvvvvvvv.",
                    path=u"/b")
writer.add_document(title=u"Third time's the charm", content=u"More examples. Examples are many.The breeding season for frogs usually occurs during the spring in temperate climates and during the rainy season in tropical climates. When male frogs are ready to breed, they often use loud croaking calls to attract partners. Males produce these calls by filling a vocal sac with air and moving the air back and forth to create a chirp-like sound.Many species lay their eggs in calm water among vegetation, where the eggs can develop in relative safety. The female frog lays numerous eggs in masses that tend to clump together in groupings known as spawn. As she deposits the eggs, the male releases sperm onto the eggs and fertilizes them In many species of frogs, the adults leave the eggs to develop without further care. But in a few species, parents remain with the eggs to look after them as they develop. As the fertilized eggs mature, the yolk in each egg splits into more and more cells and begins to take the form of a tadpole, the larva of a frog. Within one to three weeks, the egg is ready to hatch, and a tiny tadpole breaks free.",
                    path=u"/c")


writer.commit()

from whoosh.qparser import QueryParser

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("hello")
    results = searcher.search(query, terms=True)
    results.fragmenter = highlight.PinpointFragmenter()
    results.formatter=highlight.UppercaseFormatter()
    # results.fragmenter.charlimit = 1000000
    for hit in results:
        print(hit["title"])
        # Assume "content" field is stored
        print(hit.highlights("content"))







    #
    # results.fragmenter= highlight.PinpointFragmenter()
    # results.formatter=highlight.UppercaseFormatter()
    # print('results')
    # print(results[0].highlights('content'))
    #
    # print(results.matched_terms())
#
#     for r in results:
#         print(r, r.score)
#         # Was this results object created with terms=True?
#         if results.has_matched_terms():
#             # What terms matched in the results?
#             print(results.matched_terms())
#
#     # What terms matched in each hit?
#     print("matched terms")
#     for hit in results:
#         print(hit.matched_terms())
#
#     print("more_results")
#     first_hit = results[0]
#     more_results = first_hit.more_like_this("content")
#     print(more_results)
#
# found = results.scored_length()
# if results.has_exact_length():
#     print("Scored", found, "of exactly", len(results), "documents")
# else:
#     low = results.estimated_min_length()
#     high = results.estimated_length()
#
#     print("Scored", found, "of between", low, "and", high, "documents")