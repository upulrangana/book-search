from tkinter import *

# window
window = Tk()
window.title('The Law and Economics of Marriage and Divorce')
window.configure(bg='white')
window.minsize(0, 500)
window.resizable(0, 0)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
# top frame
top_frame = Frame(window, bg='white')
top_frame.grid(row=0, column=0, sticky='we')
top_frame.grid_columnconfigure(0, weight=1)
# banner
banner_img = PhotoImage(file="../img/banner.png")
banner = Label(top_frame, image=banner_img, bg='white')
banner.grid(row=0, column=0)
# body frame
body_frame = Frame(window, bg='yellow')
body_frame.grid(row=1, column=0, sticky='news')
body_frame.grid_columnconfigure(0, weight=1)
body_frame.grid_rowconfigure(1, weight=1)
# search frame
search_frame = Frame(body_frame, bg='white', padx=20, pady=20)
search_frame.grid(row=0, column=0, sticky='we')
search_frame.grid_columnconfigure(0, weight=1)
search_frame.grid_columnconfigure(1, weight=1)
search_frame.grid_columnconfigure(2, weight=1)
# search box
search_label = Label(search_frame, text="Enter Your Query: ", bg=search_frame['bg'])
search_label.grid(row=0, column=0, sticky='e')
search_entry = Entry(search_frame)
search_entry.focus()
search_entry.grid(row=0, column=1, sticky='we')
search_button = Button(search_frame, text='  Search!  ')
search_button.grid(row=0, column=2, sticky='w', padx=20)
# list frame
list_frame = Frame(body_frame)
list_frame.grid(row=1, column=0, sticky='wens')
list_frame.grid_columnconfigure(0, weight=1)
list_frame.grid_rowconfigure(0, weight=1)
# sample
canvas = Canvas(list_frame, bg="white")

canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
canvas.grid(column=0, row=0, sticky='news')
lst = []
pointer_y = 0
item_height = 80
body_frame.update()
canvas_width = body_frame.winfo_width()
for i in range(1, 10):
    item_frame = Frame(canvas, bg='#eee', borderwidth=1, cursor="hand2")
    item_frame.grid_columnconfigure(0, )
    item_frame.grid_columnconfigure(1, weight=1)
    # index text
    index_text = Text(item_frame, width=10, font=('Arial', 12), relief="flat", bg=item_frame['bg'], cursor="hand2")
    index_text.tag_configure('tag-center', justify='center')
    index_text.insert(END, f'#{i}', 'tag-center')
    index_text.config(state=DISABLED)
    index_text.grid(column=0, row=0, sticky='we')
    # body text
    body_text = Text(item_frame, font=('Arial', 12), relief="flat", bg=item_frame['bg'], cursor="hand2")
    body_text.insert(END,
                     'The fact that the two individuals went to the police station together after an allegedly brutal attack by the husband, and the fact that the wife continued to cook for the husband and he paid for some household expenses, were interpreted as ‘cohabitation’ and that the marriage had not been ‘deserted’. Therefore, the contextual realities and contradictions that play out in marital relationships, do not find a place in the law.')
    body_text.config(state=DISABLED)
    body_text.grid(column=1, row=0, sticky='we', padx=5, pady=5)
    canvas.create_window(0, pointer_y, window=item_frame, width=canvas_width - 25, height=item_height - 5, anchor=NW)
    item_frame.columnconfigure(0, weight=1)
    pointer_y += item_height
scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, pointer_y))
# MAIN LOOP
window.mainloop()
