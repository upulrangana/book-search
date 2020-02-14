from tkinter import *

# window
window = Tk()
window.title('My Computer Science Glossary')
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
search_button = Button(search_frame, text='Search!')
search_button.grid(row=0, column=2, sticky='w')
# list frame
list_frame = Frame(body_frame, bg='yellow')
list_frame.grid(row=1, column=0, sticky='wens')
# sample
b = Button(list_frame, text="muhaha")
b.pack()

# MAIN LOOP
window.mainloop()
