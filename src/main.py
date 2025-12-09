import customtkinter as ctk
from tkinter import PhotoImage, Frame, CENTER
from database_functions import *
from CTkTable import *
from CTkXYFrame import *
from PIL import Image

# app appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue.json")
ctk.set_window_scaling(1)

root = ctk.CTk()


# theme swticher
def switch_theme(choice):
    ctk.set_appearance_mode(choice)


# fonts
font_1 = ctk.CTkFont(
    family="Opensans",
    size=19,
)
font_2 = ctk.CTkFont(family="Alegreya", size=23)
font_3 = ctk.CTkFont(family="Gentium Book Plus", size=52)

# configure window
root.title("Library Manager")
icon = PhotoImage(file="icons/icon.png")
root.iconphoto(True, icon)
root.minsize(1050, 650)

# window grid configuration (1x2)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=15)

# issue frame
IssueFrame = ctk.CTkFrame(root, corner_radius=0)

# (6x3)
IssueFrame.columnconfigure(0, weight=1)
IssueFrame.columnconfigure(1, weight=2)
IssueFrame.columnconfigure(2, weight=1)
IssueFrame.rowconfigure(0, weight=1)
IssueFrame.rowconfigure(6, weight=2)


def issue():
    global error_frame
    mid = mid_entry.get()
    bid = bid_entry.get()
    timespan = timespan_entry.get()
    try:
        mid = int(mid)
        bid = int(bid)
        timespan = int(timespan)
        x = lend(bid, mid, timespan)
        if x == 99:
            error = "Issue success!"
            mid_entry.delete(0, "end")
            bid_entry.delete(0, "end")
            timespan_entry.delete(0, "end")
        elif x == 4:
            error = "Error! maximum number of rents reached"
        elif x == 5:
            error = "Error! book is not currently available"
        elif x == 0:
            error = "Error! book or member not found"
        try:
            error_frame.grid_remove()
        except:
            pass
        error_frame = ctk.CTkFrame(IssueFrame)
        error_frame.grid(row=6, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(error_frame, text=error, font=font_1)
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame.grid_remove()
        except:
            pass
        error_frame = ctk.CTkFrame(IssueFrame)
        error_frame.grid(row=6, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(
            error_frame, text="Error! Invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


issue_label = ctk.CTkLabel(IssueFrame, text="Issue a book", font=font_2)
mid_entry = ctk.CTkEntry(IssueFrame, placeholder_text="Enter member ID", font=font_1)
bid_entry = ctk.CTkEntry(IssueFrame, placeholder_text="Enter book ID", font=font_1)
timespan_entry = ctk.CTkEntry(
    IssueFrame, placeholder_text="Enter timespan", font=font_1
)

issue_label.grid(row=1, column=1, sticky="nsew", pady=7)
mid_entry.grid(row=2, column=1, sticky="nsew", pady=7)
bid_entry.grid(row=3, column=1, sticky="nsew", pady=7)
timespan_entry.grid(row=4, column=1, sticky="nsew", pady=7)

issue_button = ctk.CTkButton(IssueFrame, text="Issue", font=font_1, command=issue)
issue_button.grid(row=5, column=1, sticky="nsw", pady=7)

# return frame
ReturnFrame = ctk.CTkFrame(root, corner_radius=0)

ReturnFrame.columnconfigure(0, weight=1)
ReturnFrame.columnconfigure(1, weight=2)
ReturnFrame.columnconfigure(2, weight=1)
ReturnFrame.rowconfigure(0, weight=1)
ReturnFrame.rowconfigure(6, weight=2)


def return_book_():
    global error_frame_2
    mid = mid_entry_2.get()
    bid = bid_entry_2.get()
    fee_per_day = fee_entry.get()
    try:
        mid = int(mid)
        bid = int(bid)
        fee_per_day = int(fee_per_day)
        x = return_book(bid, mid, fee_per_day)
        if x == 99:
            error = "Return success!"
            mid_entry_2.delete(0, "end")
            bid_entry_2.delete(0, "end")
            fee_entry.delete(0, "end")
        elif x == 0:
            error = "Error! book or member not found"
        elif x == 7:
            error = "Error! this book was not rented to this member"
        else:
            error = f"Book returned. Warning! Fine of {x} exists"
        try:
            error_frame_2.grid_remove()
        except:
            pass
        error_frame_2 = ctk.CTkFrame(ReturnFrame)
        error_frame_2.grid(row=6, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(error_frame_2, text=error, font=font_1)
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_2.grid_remove()
        except:
            pass
        error_frame_2 = ctk.CTkFrame(ReturnFrame)
        error_frame_2.grid(row=6, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(
            error_frame_2, text="Error! Invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


return_label = ctk.CTkLabel(ReturnFrame, text="Return books", font=font_2)
mid_entry_2 = ctk.CTkEntry(ReturnFrame, placeholder_text="Enter member ID", font=font_1)
bid_entry_2 = ctk.CTkEntry(ReturnFrame, placeholder_text="Enter book ID", font=font_1)
fee_entry = ctk.CTkEntry(
    ReturnFrame, placeholder_text="Enter fine per day", font=font_1
)
return_button = ctk.CTkButton(
    ReturnFrame, text="Return", font=font_1, command=return_book_
)

return_label.grid(row=1, column=1, sticky="nsew", pady=7)
bid_entry_2.grid(row=3, column=1, sticky="nsew", pady=7)
mid_entry_2.grid(row=2, column=1, sticky="nsew", pady=7)
fee_entry.grid(row=4, column=1, sticky="nsew", pady=7)
return_button.grid(row=5, column=1, sticky="nsw", pady=7)

# reserve frame
ReserveFrame = ctk.CTkFrame(root, corner_radius=0)

ReserveFrame.columnconfigure(0, weight=1)
ReserveFrame.columnconfigure(1, weight=2)
ReserveFrame.columnconfigure(2, weight=1)
ReserveFrame.rowconfigure(0, weight=1)
ReserveFrame.rowconfigure(6, weight=2)


def reserve():
    global error_frame_3
    mid = r_mid_entry.get()
    bid = r_bid_entry.get()
    timespan = r_time_entry.get()
    try:
        mid = int(mid)
        bid = int(bid)
        timespan = int(timespan)
        x = reserve_book(bid, mid, timespan)
        if x == 99:
            error = "Reservation success!"
            r_mid_entry.delete(0, "end")
            r_bid_entry.delete(0, "end")
            r_time_entry.delete(0, "end")
        elif x == 0:
            error = "Error! book or member not found"
        elif x == 8:
            error = "Error! this member cannot hold a book"
        elif x == 5:
            error = "Error! book is not currently available"
        elif x == 4:
            error = "Error! maximum number of reservations reached"
        try:
            error_frame_3.grid_remove()
        except:
            pass
        error_frame_3 = ctk.CTkFrame(ReserveFrame)
        error_frame_3.grid(row=6, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(error_frame_3, text=error, font=font_1)
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_3.grid_remove()
        except:
            pass
        error_frame_3 = ctk.CTkFrame(ReserveFrame)
        error_frame_3.grid(row=6, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(
            error_frame_3, text="Error! Invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


reserve_label = ctk.CTkLabel(ReserveFrame, text="Reserve books", font=font_2)
r_mid_entry = ctk.CTkEntry(
    ReserveFrame, placeholder_text="Enter member ID", font=font_1
)
r_bid_entry = ctk.CTkEntry(
    ReserveFrame, placeholder_text="Enter book ID", font=font_1
)
r_time_entry = ctk.CTkEntry(
    ReserveFrame, placeholder_text="Enter timespan", font=font_1
)
reserve_button = ctk.CTkButton(
    ReserveFrame, text="Reserve", font=font_1, command=reserve
)

reserve_label.grid(row=1, column=1, sticky="nsew", pady=7)
r_mid_entry.grid(row=2, column=1, sticky="nsew", pady=7)
r_bid_entry.grid(row=3, column=1, sticky="nsew", pady=7)
r_time_entry.grid(row=4, column=1, sticky="nsew", pady=7)
reserve_button.grid(row=5, column=1, sticky="nsw", pady=7)

# catalog query frame
CatalogQueryFrame = ctk.CTkFrame(root, corner_radius=0)
CatalogQueryFrame.columnconfigure(0, weight=1)
CatalogQueryFrame.rowconfigure(0, weight=1)

tabview_3 = ctk.CTkTabview(CatalogQueryFrame)
tabview_3.grid(row=0, column=0, sticky="nsew")

books_tab = tabview_3.add("Books")
books_tab.rowconfigure(0, weight=1)
books_tab.columnconfigure(0, weight=1)
tabview_4 = ctk.CTkTabview(books_tab)
tabview_4.grid(row=0, column=0, sticky="nsew")
display_books_tab = tabview_4.add("Books List")
display_books_tab.rowconfigure(0, weight=1)
display_books_tab.columnconfigure(0, weight=1)
books_frame = CTkXYFrame(display_books_tab)
books_frame.grid(row=0, column=0, sticky="nsew")
value2 = [["ID", "Title", "Genre", "Type", "ISBN", "Availability", "Edition", "No_of_copies", "Location", "Description"]]
books_table = CTkTable(books_frame, row=0, column=0, values=value2, font=font_1)
books_table.grid(row=0, column=0, padx=10, sticky="nsew")
n1 = 0
def load_more_books():
    global error_frame_5
    global n1
    try:
        error_frame_5.grid_remove()
    except:
        pass
    books = display_books(10, n1)
    if books != 1:
        for i in range(len(books)):
            books_table.add_row(list(books[i]))
        n1 += len(books)
    else:
        error_frame_5 = ctk.CTkFrame(books_frame)
        error_message = ctk.CTkLabel(error_frame_5, text="Cannot load more results!")
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
        error_frame_5.grid(row=2, column=0, sticky="nsw", padx=10, pady=10)
load_more_books()
load_more_books_btn = ctk.CTkButton(books_frame, text="Load More", command=load_more_books)
load_more_books_btn.grid(row=1, column=0, sticky="nw", padx=15, pady=15)
def refresh_books():
    global n1
    global error_frame_5
    try:
        error_frame_5.grid_remove()
    except:
        pass
    books_table.delete_rows(range(1, n1 + 1))
    n1 = 0
    load_more_books()


refresh_books_btn = ctk.CTkButton(books_frame, text="Refresh Results", command=refresh_books)
refresh_books_btn.grid(row=1, column=0, sticky="nw", padx=165, pady=15)

search_books_tab = tabview_4.add("Search Book")
search_books_tab.columnconfigure(0, weight=1)
search_books_tab.rowconfigure(0, weight=1)
search_books_frame = ctk.CTkScrollableFrame(search_books_tab)
search_books_frame.grid(sticky="nsew", row=0, column=0)
search_books_frame.columnconfigure(0, weight=10)
search_books_frame.columnconfigure(1, weight=1)
search_label = ctk.CTkLabel(search_books_frame, text="Search book by:", anchor="w", font=font_1)
search_label.grid(row=0, column=0,sticky="nsew",padx=7, pady=7)
search_type = ctk.CTkOptionMenu(search_books_frame, font=font_1, values=['Title', 'Author', 'Description'])
search_type.grid(row=0, column=1, sticky="nsew", padx=7, pady=7)
books_entry = ctk.CTkEntry(search_books_frame, placeholder_text=f"Search book", font=font_1)
books_entry.grid(sticky="new", row=1, column=0, padx=(10,2), pady=5)

def search_book():
    global error_frame_12
    book_name = books_entry.get()
    stype = search_type.get()
    if stype == "Author":
        x = search_book_by_author(book_name)
    elif stype == "Title":
        x = search_book_by_title(book_name)
    else:
        x = search_book_by_description(book_name)
    if x == 0:
        error = "No matches found"
        publisher_entry.delete(0, "end")
    else:
        error = ""
        authn = 1
        for bid in x:
            y = get_book_info(bid)
            error += f"Result {str(authn)} \n"
            authn +=1
            error += f" AID: {y['aid']} \n PID: {y['pid']} \n Title: {y['title']} \n Genre: {y['genre']} \n Type: {y['type']} \n ISBN: {y['isbn']} \n Edition: {y['edition']} \n Description: {y['description']}\n\n"
    try:
        error_frame_12.grid_remove()
    except:
        pass
    error_frame_12 = ctk.CTkFrame(search_books_frame)
    error_frame_12.grid(row=2, column=0, columnspan=2, pady=20, padx=10, sticky="n")
    error_message = ctk.CTkLabel(error_frame_12, text=error, font=font_1, justify="left")
    error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


s_book_button = ctk.CTkButton(search_books_frame, text="Search", command=search_book)
s_book_button.grid(row=1, column=1, padx=(5,5), pady=7, sticky="new")


authors_tab = tabview_3.add("Authors")
authors_tab.rowconfigure(0, weight=1)
authors_tab.columnconfigure(0, weight=1)
tabview_5 = ctk.CTkTabview(authors_tab)
tabview_5.grid(row=0, column=0, sticky="nsew")
display_authors_tab = tabview_5.add("Authors List")
display_authors_tab.rowconfigure(0, weight=1)
display_authors_tab.columnconfigure(0, weight=1)
authors_frame = CTkXYFrame(display_authors_tab)
authors_frame.grid(row=0, column=0, sticky="nsew")
value3 = [["ID", "Name", "Gender", "Date of Birth", "Country", "Info", "Phone", "Contact"]]
authors_table = CTkTable(authors_frame, row=0, column=0, values=value3, font=font_1)
authors_table.grid(row=0, column=0, padx=10, sticky="nsew")

n2 = 0
def load_more_authors():
    global error_frame_6
    global n2
    try:
        error_frame_6.grid_remove()
    except:
        pass
    authors = display_authors(10, n2)
    if authors != 1:
        for i in range(len(authors)):
            authors_table.add_row(list(authors[i]))
        n2 += len(authors)
    else:
        error_frame_6 = ctk.CTkFrame(authors_frame)
        error_message = ctk.CTkLabel(error_frame_6, text="Cannot load more results!")
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
        error_frame_6.grid(row=2, column=0, sticky="nsw", padx=10, pady=10)
load_more_authors()
load_more_authors_btn = ctk.CTkButton(authors_frame, text="Load More", command=load_more_authors)
load_more_authors_btn.grid(row=1, column=0, sticky="nw", padx=15, pady=15)
def refresh_authors():
    global n2
    global error_frame_6
    try:
        error_frame_6.grid_remove()
    except:
        pass
    authors_table.delete_rows(range(1, n2 + 1))
    n2 = 0
    load_more_authors()


refresh_authors_btn = ctk.CTkButton(authors_frame, text="Refresh Results", command=refresh_authors)
refresh_authors_btn.grid(row=1, column=0, sticky="nw", padx=165, pady=15)
search_authors_tab = tabview_5.add("Search Author")
search_authors_tab.columnconfigure(0, weight=1)
search_authors_tab.rowconfigure(0, weight=1)
search_authors_frame = ctk.CTkScrollableFrame(search_authors_tab)
search_authors_frame.grid(sticky="nsew", row=0, column=0)
search_authors_frame.columnconfigure(0, weight=10)
search_authors_frame.columnconfigure(1, weight=1)
author_entry = ctk.CTkEntry(search_authors_frame, placeholder_text="Search author by name", font=font_1, width=600)
author_entry.grid(sticky="new", row=0, column=0, padx=(10,2), pady=5)

def search_author():
    global error_frame_10
    author_name = author_entry.get()
    x = search_author_by_name(author_name)
    if x == 0:
        error = "No matches found"
        author_entry.delete(0, "end")
    else:
        error = ""
        authn = 1
        for aid in x:
            y = get_author_info(aid)
            error += f"Result {str(authn)} \n"
            authn +=1
            error += f" Name: {y['name']} \n Gender: {y['gender']} \n Date of Birth: {y['dob']} \n Country: {y['country']} \n Info: {y['info']} \n Phone: {y['phone']}\n\n"
    try:
        error_frame_10.grid_remove()
    except:
        pass
    error_frame_10 = ctk.CTkFrame(search_authors_frame)
    error_frame_10.grid(row=1, column=0, columnspan=2, pady=20, padx=10, sticky="n")
    error_message = ctk.CTkLabel(error_frame_10, text=error, font=font_1, justify="left")
    error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


s_author_button = ctk.CTkButton(search_authors_frame, text="Search", command=search_author)
s_author_button.grid(row=0, column=1, padx=(5,5), pady=7, sticky="new")


publishers_tab = tabview_3.add("Publishers")
publishers_tab.rowconfigure(0, weight=1)
publishers_tab.columnconfigure(0, weight=1)
tabview_6 = ctk.CTkTabview(publishers_tab)
tabview_6.grid(row=0, column=0, sticky="nsew")
display_publishers_tab = tabview_6.add("Publishers List")
display_publishers_tab.rowconfigure(0, weight=1)
display_publishers_tab.columnconfigure(0, weight=1)
publishers_frame = ctk.CTkScrollableFrame(display_publishers_tab)
publishers_frame.grid(row=0, column=0, sticky="nsew")
value4 = [["ID", "Name", "Contact", "Details"]]
publishers_table = CTkTable(publishers_frame, row=0, column=0, values=value4, font=font_1)
publishers_table.grid(row=0, column=0, padx=10, sticky="nsew")



n3 = 0
def load_more_publishers():
    global error_frame_7
    global n3
    try:
        error_frame_7.grid_remove()
    except:
        pass
    publishers = display_publishers(10, n3)
    if publishers != 1:
        for i in range(len(publishers)):
            publishers_table.add_row(list(publishers[i]))
        n3 += len(publishers)
    else:
        error_frame_7 = ctk.CTkFrame(publishers_frame)
        error_message = ctk.CTkLabel(error_frame_7, text="Cannot load more results!")
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
        error_frame_7.grid(row=2, column=0, sticky="nsw", padx=10, pady=10)
load_more_publishers()
load_more_publishers_btn = ctk.CTkButton(publishers_frame, text="Load More", command=load_more_publishers)
load_more_publishers_btn.grid(row=1, column=0, sticky="nw", padx=15, pady=15)
def refresh_publishers():
    global n3
    global error_frame_7
    try:
        error_frame_7.grid_remove()
    except:
        pass
    publishers_table.delete_rows(range(1, n3 + 1))
    n3 = 0
    load_more_publishers()


refresh_publishers_btn = ctk.CTkButton(publishers_frame, text="Refresh Results", command=refresh_publishers)
refresh_publishers_btn.grid(row=1, column=0, sticky="nw", padx=165, pady=15)
search_publishers_tab = tabview_6.add("Search Publisher")
search_publishers_tab.columnconfigure(0, weight=1)
search_publishers_tab.rowconfigure(0, weight=1)
search_publishers_frame = ctk.CTkScrollableFrame(search_publishers_tab)
search_publishers_frame.grid(sticky="nsew", row=0, column=0)
search_publishers_frame.columnconfigure(0, weight=10)
search_publishers_frame.columnconfigure(1, weight=1)
publisher_entry = ctk.CTkEntry(search_publishers_frame, placeholder_text="Search publisher by name", font=font_1)
publisher_entry.grid(sticky="new", row=0, column=0, padx=(10,2), pady=5)

def search_publisher():
    global error_frame_11
    publisher_name = publisher_entry.get()
    x = search_publisher_by_name(publisher_name)
    if x == 0:
        error = "No matches found"
        publisher_entry.delete(0, "end")
    else:
        error = ""
        authn = 1
        for pid in x:
            y = get_publisher_info(pid)
            error += f"Result {str(authn)} \n"
            authn +=1
            error += f" Name: {y['name']} \n Contact: {y['contact']} \n Details: {y['details']}\n\n"
    try:
        error_frame_11.grid_remove()
    except:
        pass
    error_frame_11 = ctk.CTkFrame(search_publishers_frame)
    error_frame_11.grid(row=1, column=0, columnspan=2, pady=20, padx=10, sticky="n")
    error_message = ctk.CTkLabel(error_frame_11, text=error, font=font_1, justify="left")
    error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


s_publisher_button = ctk.CTkButton(search_publishers_frame, text="Search", command=search_publisher)
s_publisher_button.grid(row=0, column=1, padx=(5,5), pady=7, sticky="new")

# catalog update frame
CatalogUpdateFrame = ctk.CTkFrame(root, corner_radius=0)
CatalogUpdateFrame.columnconfigure(0, weight=1)
CatalogUpdateFrame.rowconfigure(0, weight=1)

tabview_8 =ctk.CTkTabview(CatalogUpdateFrame)
tabview_8.grid(row=0, column=0, sticky="nsew")
book_tab = tabview_8.add("Books")
book_tab.rowconfigure(0, weight=1)
book_tab.columnconfigure(0, weight=1)
tabview_7 = ctk.CTkTabview(book_tab)
tabview_7.grid(row=0, column=0, sticky="nsew")
add_book_tab = tabview_7.add("Add Book")
add_book_tab.columnconfigure(0, weight=3)
add_book_tab.columnconfigure(1, weight=1)
add_book_tab.columnconfigure(2, weight=2)
add_book_tab.columnconfigure(3, weight=3)
add_book_tab.rowconfigure(0, weight=1)
add_book_tab.rowconfigure(12, weight=2)

book_types = get_book_types()
author_names = get_author_names()
publishers = get_publishers()

def add_a_book():
    global error_frame_13
    title_b = title.get()
    isbn_b = isbn.get()
    genre_b = genre.get()
    type_b = book_type.get()
    edition_b = edition.get()
    description_b = description.get()
    location_b = location.get()
    author_b = author.get()
    publisher_b = publisher.get()
    try:
        isbn_b = int(isbn_b)
        edition_b = int(edition_b)
        details = dict()
        details["title"] = title_b
        details["isbn"] = isbn_b
        details["genre"] = genre_b
        details["type"] = type_b
        details["edition"] = edition_b
        details["description"] = description_b
        details["location"] = location_b
        details["author"] = author_b
        details["publisher"] = publisher_b
        x = add_book(details)
        if x == 99:
            error = "Book successfully added!"
            title.delete(0, "end")
            isbn.delete(0, "end")
            genre.delete(0, "end")
            edition.delete(0, "end")
            description.delete(0, "end")
            location.delete(0, "end")
        elif x == 9:
            error = "Error! maximum length exceeded"
        try:
            error_frame_13.grid_remove()
        except:
            pass
        error_frame_13 = ctk.CTkFrame(add_book_tab)
        error_frame_13.grid(row=12, column=0, columnspan=4, pady=20, sticky="n")
        error_message = ctk.CTkLabel(error_frame_13, text=error, font=font_1)
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_13.grid_remove()
        except:
            pass
        error_frame_13 = ctk.CTkFrame(add_book_tab)
        error_frame_13.grid(row=12, column=0, columnspan=4, pady=20, sticky="n")
        error_message = ctk.CTkLabel(
            error_frame_13, text="Error! Invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


add_book_label = ctk.CTkLabel(add_book_tab, font=font_2, text="Add a new book")
isbn = ctk.CTkEntry(add_book_tab, font=font_1, placeholder_text="Book's ISBN")
title = ctk.CTkEntry(add_book_tab, font=font_1, placeholder_text="Book's title")
genre = ctk.CTkEntry(add_book_tab, font=font_1, placeholder_text="Book's genre")
type_label = ctk.CTkLabel(add_book_tab, font=font_1, text="Book Type:", anchor="w")
book_type = ctk.CTkComboBox(add_book_tab, font=font_1, values=book_types)
edition = ctk.CTkEntry(add_book_tab, font=font_1, placeholder_text="Book Edition")
description = ctk.CTkEntry(add_book_tab, font=font_1, placeholder_text="Book Description")
location = ctk.CTkEntry(add_book_tab, font=font_1, placeholder_text="Book's shelf location")
author_label = ctk.CTkLabel(add_book_tab, font=font_1, text="Author:", anchor="w")
author = ctk.CTkOptionMenu(add_book_tab, font=font_1, values=author_names)
publisher_label = ctk.CTkLabel(add_book_tab, font=font_1, text="Publisher:", anchor="w")
publisher = ctk.CTkOptionMenu(add_book_tab, font=font_1, values=publishers)
add_book_button = ctk.CTkButton(add_book_tab, font=font_1, text="Add Book", command=add_a_book)

add_book_label.grid(row=1, column=1, columnspan=2, sticky="nsew", pady=4)
isbn.grid(row=2, column=1, columnspan=2, sticky="nsew", pady=4)
title.grid(row=3, column=1, columnspan=2, sticky="nsew", pady=4)
genre.grid(row=4, column=1, columnspan=2, sticky="nsew", pady=4)
type_label.grid(row=5, column=1, sticky="nsew", pady=4)
book_type.grid(row=5, column=2, sticky="nsew", pady=4)
edition.grid(row=6, column=1, columnspan=2, sticky="nsew", pady=4)
description.grid(row=7, column=1, columnspan=2, sticky="nsew", pady=4)
location.grid(row=8, column=1, columnspan=2, sticky="nsew", pady=4)
author_label.grid(row=9, column=1, sticky="nsew", pady=4)
author.grid(row=9, column=2, sticky="nsew", pady=4)
publisher_label.grid(row=10, column=1, sticky="nsew", pady=4)
publisher.grid(row=10, column=2, sticky="nsew", pady=4)
add_book_button.grid(row=11, column=1, sticky="nw", pady=4)

del_book_tab = tabview_7.add("Remove a Book")
del_book_tab.columnconfigure(0, weight=1)
del_book_tab.columnconfigure(1, weight=2)
del_book_tab.columnconfigure(2, weight=1)
del_book_tab.rowconfigure(0, weight=1)
del_book_tab.rowconfigure(4, weight=2)

def decrement_book_count():
    global error_frame_15
    bid = book_id_entry.get()
    try:
        bid = int(bid)
        x = decrement_book(bid)
        if x == 0:
            error = "Error! book or member not found"
        elif x == 11:
            error = "Error! only one book left"
        elif x == 99:
            error = "Book count decremented by 1"
            book_id_entry.delete(0, "end")
        try:
            error_frame_15.grid_remove()
            error_frame_14.grid_remove()
        except:
            pass
        error_frame_15 = ctk.CTkFrame(del_book_tab)
        error_frame_15.grid(row=4, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(error_frame_15, text=error, font=font_1, justify="left")
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_15.grid_remove()
            error_frame_14.grid_remove()
        except:
            pass
        error_frame_15 = ctk.CTkFrame(del_book_tab)
        error_frame_15.grid(row=4, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(
            error_frame_15, text="Error! invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
def delete_a_book():
    global error_frame_14
    bid = book_id_entry.get()
    try:
        bid = int(bid)
        x = delete_book(bid)
        if x == 0:
            error = "Error! book or member not found"
        else:
            error = "Book successfully deleted!"
            error += f"\n\n Title: {x["title"]}\nISBN: {x["isbn"]}\nDescription: {x["description"]}\nEdition: {x["edition"]}"
            book_id_entry.delete(0, "end")
        try:
            error_frame_14.grid_remove()
            error_frame_15.grid_remove()
        except:
            pass
        error_frame_14 = ctk.CTkFrame(del_book_tab)
        error_frame_14.grid(row=4, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(error_frame_14, text=error, font=font_1)
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_14.grid_remove()
            error_frame_15.grid_remove()
        except:
            pass
        error_frame_14 = ctk.CTkFrame(del_book_tab)
        error_frame_14.grid(row=4, column=0, columnspan=3, pady=20, sticky="n")
        error_message = ctk.CTkLabel(
            error_frame_14, text="Error! invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


del_book_label = ctk.CTkLabel(del_book_tab, font=font_2, text="Remove a book")
book_id_entry = ctk.CTkEntry(del_book_tab, font=font_1, placeholder_text="Book ID")
decrement_book_btn = ctk.CTkButton(del_book_tab, font=font_1, text="Decrement book count", command=decrement_book_count)
del_book_btn = ctk.CTkButton(del_book_tab, font=font_1, text="Delete book", command=delete_a_book)

del_book_label.grid(row=1, column=1, pady=7, sticky="nsew")
book_id_entry.grid(row=2, column=1, pady=7, sticky="nsew")
decrement_book_btn.grid(row=3, column=1, pady=7, sticky="nsw")
del_book_btn.grid(row=3, column=1, pady=7, sticky="nsw", padx=(235,0))

# member query frame
MemberQueryFrame = ctk.CTkFrame(root, corner_radius=0)

MemberQueryFrame.columnconfigure(0, weight=1)
MemberQueryFrame.rowconfigure(0, weight=1)

tabview_1 = ctk.CTkTabview(MemberQueryFrame)
tabview_1.grid(row=0, column=0, sticky="nsew")

display_tab = tabview_1.add("Display Members")
dsply_frame = CTkXYFrame(display_tab)
dsply_frame.grid(row=0, column=0, sticky="nsew")
value = [["ID", "Name", "Address", "Phone", "Gender", "Class", "No. of books rented"]]
member_table = CTkTable(dsply_frame, row=0,column=0, values=value, font=font_1)
member_table.grid(row=0, column=0, padx=10, sticky="nsew")

n = 0
def load_more():
    global error_frame_4
    global n
    try:
        error_frame_4.grid_remove()
    except:
        pass
    members = display_members(10, n)
    if members != 1:
        for i in range(len(members)):
            member_table.add_row(list(members[i]))
        n += len(members)
    else:
        error_frame_4 = ctk.CTkFrame(dsply_frame)
        error_message = ctk.CTkLabel(error_frame_4, text="Cannot load more results!")
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
        error_frame_4.grid(row=2, column=0, sticky="nsw", padx=10, pady=10)


load_more()
load_more_btn = ctk.CTkButton(dsply_frame, text="Load More", command=load_more)
load_more_btn.grid(row=1, column=0, sticky="nw", padx=15, pady=15)


def refresh():
    global n
    global error_frame_4
    try:
        error_frame_4.grid_remove()
    except:
        pass
    member_table.delete_rows(range(1, n + 1))
    n = 0
    load_more()


refresh_btn = ctk.CTkButton(dsply_frame, text="Refresh Results", command=refresh)
refresh_btn.grid(row=1, column=0, sticky="nw", padx=165, pady=15)

display_tab.columnconfigure(0, weight=1)
display_tab.rowconfigure(0, weight=1)

search_tab = tabview_1.add("View Member Details")
search_tab.columnconfigure(0, weight=10)
search_tab.columnconfigure(1, weight=1)

query_input = ctk.CTkEntry(search_tab, placeholder_text="Enter member ID")
query_input.grid(row=0, column=0, sticky="new", padx=(15, 3), pady=15)


def search_member():
    global error_frame_5
    mid = query_input.get()
    try:
        mid = int(mid)
        x = get_member_info(mid)
        if x == 0:
            error = "Error! member not found"
        else:
            error = f" Name: {x['name']} \n Address: {x['address']} \n Phone: {x['phone']} \n Gender: {x['gender']} \n Class: {x['class']} \n No. of books rented: {x['no_of_books_rented']}"
        try:
            error_frame_5.grid_remove()
        except:
            pass
        error_frame_5 = ctk.CTkFrame(search_tab)
        error_frame_5.grid(
            row=1, column=0, columnspan=2, pady=20, sticky="new", padx=15
        )
        error_message = ctk.CTkLabel(
            error_frame_5, text=error, font=font_1, justify="left"
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_5.grid_remove()
        except:
            pass
        error_frame_5 = ctk.CTkFrame(search_tab)
        error_frame_5.grid(
            row=1, column=0, columnspan=2, pady=20, sticky="new", padx=15
        )
        error_message = ctk.CTkLabel(
            error_frame_5, text="Error! Invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


search_btn = ctk.CTkButton(search_tab, text="Search", command=search_member)
search_btn.grid(row=0, column=1, sticky="new", padx=(5, 15), pady=15)

# member update frame
MupdateFrame = ctk.CTkFrame(root, corner_radius=0)

MupdateFrame.columnconfigure(0, weight=1)
MupdateFrame.rowconfigure(0, weight=1)

tabview_2 = ctk.CTkTabview(MupdateFrame)
tabview_2.grid(row=0, column=0, sticky="nsew")

add_tab = tabview_2.add("Add Members")
add_tab.rowconfigure(0, weight=1)
add_tab.rowconfigure(8, weight=2)
add_tab.columnconfigure(0, weight=4)
add_tab.columnconfigure(1, weight=1)
add_tab.columnconfigure(2, weight=2)
add_tab.columnconfigure(3, weight=4)


def add_a_member():
    global error_frame_6
    name = member_name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    gender = gender_entry.get()
    m_class = membership_entry.get()
    try:
        phone = int(phone)
        m_class = int(m_class)
        details = dict()
        details["name"] = name
        details["address"] = address
        details["phone"] = phone
        details["gender"] = gender
        details["class"] = m_class
        x = add_member(details)
        if x == 99:
            error = "Member succesfully added!"
            member_name_entry.delete(0, "end")
            address_entry.delete(0, "end")
            phone_entry.delete(0, "end")
        elif x == 9:
            error = "Error! maximum input length exceeded"
        try:
            error_frame_6.grid_remove()
        except:
            pass
        error_frame_6 = ctk.CTkFrame(add_tab)
        error_frame_6.grid(row=8, column=0, columnspan=4, pady=20, sticky="n")
        error_message = ctk.CTkLabel(error_frame_6, text=error, font=font_1)
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_6.grid_remove()
        except:
            pass
        error_frame_6 = ctk.CTkFrame(add_tab)
        error_frame_6.grid(row=8, column=0, columnspan=4, pady=20, sticky="n")
        error_message = ctk.CTkLabel(
            error_frame_6, text="Error! Invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


add_member_label = ctk.CTkLabel(add_tab, text="Add a Member", font=font_2)
member_name_entry = ctk.CTkEntry(add_tab, placeholder_text="Member name", font=font_1)
address_entry = ctk.CTkEntry(add_tab, placeholder_text="Member's adress", font=font_1)
phone_entry = ctk.CTkEntry(
    add_tab, placeholder_text="Member's phone number", font=font_1
)
gender_label = ctk.CTkLabel(add_tab, text="Member's Gender:", font=font_1, anchor="w")
gender_entry = ctk.CTkOptionMenu(
    add_tab, font=font_1, values=["Male", "Female", "Other"]
)
membership_label = ctk.CTkLabel(
    add_tab, text="Membership Class:", font=font_1, anchor="w"
)
membership_entry = ctk.CTkOptionMenu(add_tab, font=font_1, values=["1", "2", "3"])
add_member_button = ctk.CTkButton(
    add_tab, text="Add Member", font=font_1, command=add_a_member
)

add_member_label.grid(row=1, column=1, columnspan=2, sticky="nsew", pady=7)
member_name_entry.grid(row=2, column=1, columnspan=2, sticky="nsew", pady=7)
address_entry.grid(row=3, column=1, columnspan=2, sticky="nsew", pady=7)
phone_entry.grid(row=4, column=1, columnspan=2, sticky="nsew", pady=7)
gender_label.grid(row=5, column=1, sticky="nsew", pady=7)
gender_entry.grid(row=5, column=2, sticky="nsew", pady=7)
membership_label.grid(row=6, column=1, sticky="nsew", pady=7)
membership_entry.grid(row=6, column=2, sticky="nsew", pady=7)
add_member_button.grid(row=7, column=1, sticky="nsw", pady=7)

del_tab = tabview_2.add("Remove Members")
del_tab.rowconfigure(0, weight=1)
del_tab.rowconfigure(4, weight=2)
del_tab.columnconfigure(0, weight=2)
del_tab.columnconfigure(1, weight=3)
del_tab.columnconfigure(2, weight=2)


def del_a_member():
    global error_frame_7
    mid = member_id.get()
    sticky_value = "n"
    try:
        mid = int(mid)
        y = get_member_info(mid)
        x = del_member(mid)
        if x == 99:
            error = "Member successfully removed!\n\n"
            details = f" Name: {y['name']} \n Address: {y['address']} \n Phone: {y['phone']} \n Gender: {y['gender']} \n Class: {y['class']} \n No. of books rented: {y['no_of_books_rented']}"
            error += details
            member_id.delete(0, "end")
            sticky_value="new"
        elif x == 0:
            error = "Error! member not found"
        elif x == 10:
            error = "Error! member has unreturned book"
        try:
            error_frame_7.grid_remove()
        except:
            pass
        error_frame = ctk.CTkFrame(del_tab)
        error_frame.grid(row=4, column=1, columnspan=1, pady=20, sticky=sticky_value)
        error_message = ctk.CTkLabel(error_frame, text=error, font=font_1, justify="left")
        error_message.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=7, padx=15)
    except:
        try:
            error_frame_7.grid_remove()
        except:
            pass
        error_frame = ctk.CTkFrame(del_tab)
        error_frame.grid(row=4, column=1, columnspan=1, pady=20, sticky=sticky_value)
        error_message = ctk.CTkLabel(
            error_frame, text="Error! Invalid entries", font=font_1
        )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


del_member_label = ctk.CTkLabel(del_tab, text="Remove a Member", font=font_2)
member_id = ctk.CTkEntry(del_tab, placeholder_text="Member ID for removal", font=font_1)
del_member_button = ctk.CTkButton(
    del_tab, text="Remove Member", font=font_1, command=del_a_member
)

del_member_label.grid(row=1, column=1, sticky="nsew", pady=7)
member_id.grid(row=2, column=1, sticky="nsew", pady=7)
del_member_button.grid(row=3, column=1, sticky="nsw", pady=7)

# greet frame
GreetFrame = ctk.CTkFrame(root, corner_radius=0)
greet_label = ctk.CTkLabel(GreetFrame, text="Library Manager v1.0", font=font_3)
greet_label.place(relx=0.5, rely=0.6, anchor=CENTER)
image = ctk.CTkImage(light_image=Image.open("icons/image.png"), size=(160, 160))
image_label = ctk.CTkLabel(GreetFrame, image=image, text="")
image_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# change the frame on button press function
active_frame = IssueFrame

def change_frame(frame):
    global active_frame
    if frame != active_frame:
        active_frame.grid_remove()
        frame.grid(row=0, column=1, sticky="nsew")
        active_frame = frame


change_frame(GreetFrame)

# sidebar
sidebar = ctk.CTkFrame(root, corner_radius=0)
sidebar.grid(row=0, column=0, sticky="nsew")

# sidebar grid configuration(1x12)
sidebar.columnconfigure(0, weight=1)
sidebar.rowconfigure(12, weight=5)

seperator = Frame(sidebar, width=2, bg="#606060")
seperator.place(relx=0.99, relheight=1)

label_1 = ctk.CTkLabel(sidebar, text="Circulation", font=font_2)
button_1 = ctk.CTkButton(
    sidebar, text="Issue", font=font_1, command=lambda: change_frame(IssueFrame)
)
button_2 = ctk.CTkButton(
    sidebar, text="Return", font=font_1, command=lambda: change_frame(ReturnFrame)
)
button_3 = ctk.CTkButton(
    sidebar, text="Reserve", font=font_1, command=lambda: change_frame(ReserveFrame)
)
label_2 = ctk.CTkLabel(sidebar, text="Catalog", font=font_2)
button_4 = ctk.CTkButton(sidebar, text="Query", font=font_1, command=lambda: change_frame(CatalogQueryFrame))
button_5 = ctk.CTkButton(sidebar, text="Update records", font=font_1, command=lambda: change_frame(CatalogUpdateFrame))
label_3 = ctk.CTkLabel(sidebar, text="Members", font=font_2)
button_6 = ctk.CTkButton(
    sidebar, text="Query", font=font_1, command=lambda: change_frame(MemberQueryFrame)
)
button_7 = ctk.CTkButton(
    sidebar,
    text="Update records",
    font=font_1,
    command=lambda: change_frame(MupdateFrame),
)
label_4 = ctk.CTkLabel(sidebar, text="Statistics", font=font_2)
button_8 = ctk.CTkButton(sidebar, text="Book popularity", font=font_1)
theme_button = ctk.CTkOptionMenu(
    sidebar,
    values=["System", "Light", "Dark"],
    command=switch_theme,
    anchor="center",
    font=font_1,
)

label_1.grid(row=0, sticky="nsew", padx=30, pady=(10, 2))
button_1.grid(row=1, sticky="nsew", padx=30, pady=2)
button_2.grid(row=2, sticky="nsew", padx=30, pady=2)
button_3.grid(row=3, sticky="nsew", padx=30, pady=2)
label_2.grid(row=4, sticky="nsew", padx=30, pady=2)
button_4.grid(row=5, sticky="nsew", padx=30, pady=2)
button_5.grid(row=6, sticky="nsew", padx=30, pady=2)
label_3.grid(row=7, sticky="nsew", padx=30, pady=2)
button_6.grid(row=8, sticky="nsew", padx=30, pady=2)
button_7.grid(row=9, sticky="nsew", padx=30, pady=2)
label_4.grid(row=10, sticky="nsew", padx=30, pady=2)
button_8.grid(row=11, sticky="nsew", padx=30, pady=2)
theme_button.grid(row=13, padx=30, sticky="nsew", pady=(2, 19))

# login frame for signing in
LoginFrame = ctk.CTkFrame(root)
LoginFrame.grid(row=0, column=0, columnspan=2, sticky="nsew")

# login frame grid configuration (7x3)
LoginFrame.columnconfigure(0, weight=3)
LoginFrame.columnconfigure(1, weight=2)
LoginFrame.columnconfigure(2, weight=3)

LoginFrame.rowconfigure(1, weight=2)
LoginFrame.rowconfigure(7, weight=5)


def login():
    # Validate the username and password
    global error_frame
    username = username_entry.get()
    password = password_entry.get()
    returned = check_credentials(username, password)
    if returned == 99:
        # Login successful
        LoginFrame.destroy()

    else:
        # Login failed
        # Display an error message
        try:
            error_frame.grid_remove()
        except:
            pass
        error_frame = ctk.CTkFrame(LoginFrame)
        error_frame.grid(row=7, column=0, columnspan=3, pady=20, sticky="n")
        if returned == 2:
            error_message = ctk.CTkLabel(
                error_frame, text="Error! Username not found", font=font_1
            )
        else:
            error_message = ctk.CTkLabel(
                error_frame, text="Error! Password invalid", font=font_1
            )
        error_message.grid(row=0, column=0, sticky="nsew", pady=7, padx=15)


# Create the login form
title_label = ctk.CTkLabel(LoginFrame, text="Login", font=font_3)
username_label = ctk.CTkLabel(LoginFrame, text="Username:", font=font_2)
username_entry = ctk.CTkEntry(LoginFrame, placeholder_text="username", font=font_1)
password_label = ctk.CTkLabel(LoginFrame, text="Password:", font=font_2)
password_entry = ctk.CTkEntry(
    LoginFrame, placeholder_text="password", show="*", font=font_1
)
login_button = ctk.CTkButton(LoginFrame, text="Login", command=login, font=font_1)

# Place the widgets on the frame
title_label.grid(row=0, column=1, sticky="nsew", pady=7)
username_label.grid(row=2, column=1, sticky="nsw", pady=7)
username_entry.grid(row=3, column=1, sticky="nsew", pady=7)
password_label.grid(row=4, column=1, sticky="nsw", pady=7)
password_entry.grid(row=5, column=1, sticky="nsew", pady=7)
login_button.grid(row=6, column=1, sticky="nsew", pady=7)

# run
root.mainloop()
