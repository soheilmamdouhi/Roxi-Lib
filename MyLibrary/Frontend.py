from tkinter import *
import Backend

selected_item = ()


def delete_listbox():
    listBox.delete(0, END)


def list_result(book):
    for b in book:
        listBox.insert(END, b)


# =====================Right Buttons Functions==================================

def view_all():
    delete_listbox()
    exist_books = Backend.view()
    list_result(exist_books)


def search_entry():
    delete_listbox()
    #searched_books = Backend.search(titleEntry.get(), authorEntry.get(), yearEntry.get(), ISBNEntry.get())
    searched_books = Backend.search(titleEntry.get())
    list_result(searched_books)


def add_entry():
    Backend.insert(titleEntry.get(), authorEntry.get(), yearEntry.get(), ISBNEntry.get())
    view_all()


def get_selected_row(_):
    global selected_item
    if len(listBox.curselection()) > 0:
        index = listBox.curselection()[0]
        selected_item = listBox.get(index)

        titleEntry.delete(0, END)
        titleEntry.insert(END, selected_item[1])

        authorEntry.delete(0, END)
        authorEntry.insert(END, selected_item[2])

        yearEntry.delete(0, END)
        yearEntry.insert(END, selected_item[3])

        ISBNEntry.delete(0, END)
        ISBNEntry.insert(END, selected_item[4])


def delete_items():
    delete_listbox()
    if selected_item:
        Backend.delete(selected_item[0])
    else:
        print("no object")
    view_all()


def update_entry():
    global selected_item
    Backend.update(titleEntry.get(), authorEntry.get(), yearEntry.get(), ISBNEntry.get(), selected_item[0])
    view_all()


# =====================this is the main window=================================
bookLIB = Tk()
bookLIB.title("Book Library")
bookLIB.geometry("500x500")
bookLIB.resizable(width=False, height=False)
bookLIB.configure(bg="lightblue")
# =====================This is the Top of the window Frame======================
topFrame = Frame(bookLIB, width=500, height=100, bg="lightblue")
topFrame.pack(side=TOP)
title = Label(topFrame, text="Title:", bg="lightblue")
title.grid(row=0, column=0, padx=10, pady=10)
titleEntry = Entry(topFrame)
titleEntry.grid(row=0, column=1, padx=10, pady=10)

year = Label(topFrame, text="Year:", bg="lightblue")
year.grid(row=1, column=0, padx=10, pady=10)
yearEntry = Entry(topFrame)
yearEntry.grid(row=1, column=1, padx=10, pady=10)

author = Label(topFrame, text="Author:", bg="lightblue")
author.grid(row=0, column=2, padx=10, pady=10)
authorEntry = Entry(topFrame)
authorEntry.grid(row=0, column=3, padx=10, pady=10)

ISBN = Label(topFrame, text="ISBN", bg="lightblue")
ISBN.grid(row=1, column=2, padx=10, pady=10)
ISBNEntry = Entry(topFrame)
ISBNEntry.grid(row=1, column=3, padx=10, pady=10)
# ===============================This is Right Frame============================
rightFrame = Frame(bookLIB, width=150, height=300, bg="lightblue")
rightFrame.pack(side=RIGHT, padx=30)

buttons_name = {"View All": view_all, "Search Entry": search_entry, "Add Entry": add_entry,
                "Delete Selected": delete_items,
                "Update Selected": update_entry, "Close": bookLIB.destroy}
for i, cmd in buttons_name.items():
    all_Buttons = Button(rightFrame, text=i, width=15, height=1, command=cmd)
    all_Buttons.pack(padx=5, pady=10)

# ==============================This is Left Frame===============================
leftFrame = Frame(bookLIB, width=350, height=300)
leftFrame.pack(side=LEFT, padx=20)
listBox = Listbox(leftFrame)
listBox.pack(side=LEFT, ipadx=60, ipady=60)
listBox.bind("<<ListboxSelect>>", get_selected_row)
scroll_bar = Scrollbar(leftFrame, orient="vertical", width=20)
scroll_bar.pack(side=RIGHT)
scroll_bar.configure(command=listBox.yview)
listBox.configure(yscrollcommand=scroll_bar.set)
# ===============================================================================
view_all()
bookLIB.mainloop()
