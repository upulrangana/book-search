from tkinter import *


class MainApp(Tk):
    def __init__(self, book):
        super(MainApp, self).__init__()
        self.setup()
        self.top_frame = TopFrame(self)
        self.body_frame = BodyFrame(self)

    def setup(self):
        self.title('The Law and Economics of Marriage and Divorce')
        self.configure(bg='white')
        self.minsize(0, 500)
        self.resizable(0, 0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


class TopFrame(Frame):
    def __init__(self, parent):
        super(TopFrame, self).__init__(master=parent)
        self.setup()
        # banner
        self.banner_img = PhotoImage(file="./img/banner.png")
        self.banner = Label(self, image=self.banner_img, bg='white')
        self.banner.grid(row=0, column=0)

    def setup(self):
        self.configure(bg='white')
        self.grid(row=0, column=0, sticky='we')
        self.grid_columnconfigure(0, weight=1)


class BodyFrame(Frame):
    def __init__(self, parent):
        super(BodyFrame, self).__init__(master=parent)
        self.setup()
        self.search_frame = SearchFrame(self)
        self.list_frame = ListFrame(self)

    def setup(self):
        self.configure(bg='yellow')
        self.grid(row=1, column=0, sticky='news')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


class SearchFrame(Frame):
    def __init__(self, parent):
        super(SearchFrame, self).__init__(master=parent)
        self.setup()
        self.search_label = Label(self, text="Enter Your Query: ", bg=self['bg'])
        self.search_label.grid(row=0, column=0, sticky='e')
        self.search_entry = Entry(self)
        self.search_entry.focus()
        self.search_entry.grid(row=0, column=1, sticky='we')
        self.search_button = Button(self, text='  Search!  ')
        self.search_button.grid(row=0, column=2, sticky='w', padx=20)

    def setup(self):
        self.configure(bg='white', padx=20, pady=20)
        self.grid(row=0, column=0, sticky='we')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


class ListFrame(Frame):
    def __init__(self, parent):
        super(ListFrame, self).__init__(master=parent)
        self.setup()
        self.canvas = Canvas(self, bg="white")
        self.canvas.bind_all("<MouseWheel>",
                             lambda event: self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        self.canvas.grid(column=0, row=0, sticky='news')
        pointer_y = 0
        item_height = 80
        self.master.update()
        self.canvas_width = self.master.winfo_width()
        for i in range(1, 10):
            self.item_frame = Frame(self.canvas, bg='#eee', borderwidth=1, cursor="hand2")
            self.item_frame.grid_columnconfigure(0, )
            self.item_frame.grid_columnconfigure(1, weight=1)
            # index text
            self.index_text = Text(self.item_frame, width=10, font=('Arial', 12), relief="flat",
                                   bg=self.item_frame['bg'], cursor="hand2")
            self.index_text.tag_configure('tag-center', justify='center')
            self.index_text.insert(END, f'#{i}', 'tag-center')
            self.index_text.config(state=DISABLED)
            self.index_text.grid(column=0, row=0, sticky='we')
            # body text
            self.body_text = Text(self.item_frame, font=('Arial', 12), relief="flat", bg=self.item_frame['bg'],
                                  cursor="hand2")
            self.body_text.insert(END,
                                  'The fact that the two individuals went to the police station together after an allegedly brutal attack by the husband, and the fact that the wife continued to cook for the husband and he paid for some household expenses, were interpreted as ‘cohabitation’ and that the marriage had not been ‘deserted’. Therefore, the contextual realities and contradictions that play out in marital relationships, do not find a place in the law.')
            self.body_text.config(state=DISABLED)
            self.body_text.grid(column=1, row=0, sticky='we', padx=5, pady=5)
            self.canvas.create_window(0, pointer_y, window=self.item_frame, width=self.canvas_width - 25,
                                      height=item_height - 5, anchor=NW)
            self.item_frame.columnconfigure(0, weight=1)
            pointer_y += item_height
        self.scrollbar = Scrollbar(self.canvas, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
        self.canvas.config(yscrollcommand=self.scrollbar.set, scrollregion=(0, 0, 0, pointer_y))

    def setup(self):
        self.grid(row=1, column=0, sticky='wens')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
