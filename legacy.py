import os.path
from tkinter import *

from whoosh import index, highlight
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
from whoosh.query import FuzzyTerm

from listbox import MultiListbox

window = Tk()
window.configure()
window.title("BOOK SEARCH")
window.geometry('650x600')
mlb = MultiListbox(window, (('Rank', 5), ('Score', 18), ('Result', 80)))
lbl = Label(window, text="SEARCH BOX", background="green")
lbl.pack(fill=BOTH)
e = Entry(window)
e.pack(fill=BOTH, padx=120, pady=20)


class MyFuzzyTerm(FuzzyTerm):
    def __getitem__(self, item):
        pass

    def __init__(self, fieldname, text, boost=1.0, maxdist=2, prefixlength=1, constantscore=True):
        super(MyFuzzyTerm, self).__init__(fieldname, text, boost, maxdist, prefixlength, constantscore)


def clicked():
    string1 = e.get()
    with ix.searcher() as searcher:
        query = QueryParser("content", schema=ix.schema, termclass=MyFuzzyTerm).parse(string1)
        results = searcher.search(query, terms=True)
        results.fragmenter = highlight.PinpointFragmenter()
        results.formatter = highlight.UppercaseFormatter()
        mlb.clear()

        for hit in results:
            match_string = hit.highlights("content")
            mlb.insert(END,
                       (hit.rank + 1,
                        str(hit.score), match_string))
            mlb.pack(expand=YES, fill=BOTH)


def create_index():
    if not os.path.exists("index"):
        os.mkdir("index")
    schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))
    ix = index.create_in("index", schema)
    writer = ix.writer()
    writer.add_document(title=u"section 1",
                        content=u"The agony and anxiousness that a divorce proceeding in Sri Lanka inflicts on spouses is widely known and there are many who can speak to it. It is a proceeding usually faced in silence. Once it is done with, we want to forget it, we don’t want to relive it, and we want to get on with the next stage of building our lives after a divorce. As a result, these stories and experiences remain untold.")
    writer.add_document(title=u"section 2",
                        content=u"While this piece was penned, the Supreme Court added its voice to the state of divorce law in Sri Lanka. The Court in SC Appeal 123/14 felt compelled to uphold a decision not to grant a divorce and commented: “This is a sad case which has seen the parties locked in a long and bitterly-contested battle over whether they should remain married or not.")
    writer.add_document(title=u"section 3",
                        content=u"The wife sought this divorce in 2001, when she and her husband were both in their early forties. The fact that this appeal was fought by both of them suggests that the unhappy marriage which led to this action being instituted has continued to remain so during the 17 years in which this case has traversed the Courts. It seems that the rancour between the spouses continues unabated. This litigation has seen the plaintiff and the defendant into their late fifties and has to have exacted its heavy toll on both spouses and their children.” ")
    writer.add_document(title=u"section 4",
                        content=u"This Supreme Court judgment is the latest voice in an age-old call for reform of the General Marriages (Registration) Ordinance No. 19 of 1907. As a country, we choose to continue subjecting one of the most personal decisions of ending a marriage relationship to the most public adversarial form of adjudication. ")
    writer.add_document(title=u"section 5",
                        content=u"It is not enough that the law removes the right of individuals to decide that they want to end the relationship, the two individuals are also pitted against each other by framing divorce proceedings as an adversarial contest. This unnecessarily complicates a difficult, often traumatic personal and social experience, of deciding to separate. It introduces a legal blame game, reinforces animosity towards each other, and creates winners and losers where there ought to be none.")
    writer.commit()
    return ix


ix = create_index()
btn = Button(window, text="Search", command=clicked)
btn.pack(fill=BOTH, padx=40, pady=20)
Label(window, text='Search Results').pack(fill=X, padx=40, pady=20)
# w.mainloop(  )
window.mainloop()
