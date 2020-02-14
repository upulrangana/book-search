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
search_button = Button(search_frame, text='  Search!  ')
search_button.grid(row=0, column=2, sticky='w', padx=20)
# list frame
list_frame = Frame(body_frame)
list_frame.grid(row=1, column=0, sticky='wens')
list_frame.grid_columnconfigure(0, weight=1)
list_frame.grid_rowconfigure(0, weight=1)
# sample
canvas = Canvas(list_frame, bg="Black")

canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
canvas.grid(column=0, row=0, sticky='news')
lst = []
yy = 0
for i in range(1, 100):
    frame = Frame(canvas, bg='red', borderwidth=1)
    label = Label(frame, text="File number " + str(i), font=("Courier", 16), compound=RIGHT)
    label.pack()
    canvas.create_window(0, yy, window=frame, anchor=NW)
    yy += 60
scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, yy))
# MAIN LOOP
window.mainloop()
