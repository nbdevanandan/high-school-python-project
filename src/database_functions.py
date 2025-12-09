from rapidfuzz.fuzz import (
    partial_ratio,
    partial_token_set_ratio,
    WRatio,
    token_set_ratio,
)
from mysql.connector import connect
from datetime import date, timedelta

connection = connect(user="root", password="8235", host="127.0.0.1", database="library")
cursor = connection.cursor()

###############
# credentials #
###############
def check_credentials(username, password):
    username_exists = False
    password_correct = False
    cursor.execute("SELECT * FROM credentials;")
    for row in cursor:
        if username == row[0]:
            username_exists = True
            if password == row[1]:
                password_correct = True

    if not username_exists:
        out = 2
    elif not password_correct:
        out = 1
    else:
        out = 99

    return out


# print(check_credentials('devanandan','kakakaka'))
# print(check_credentials('sd','65'))

####################
# common functions #
####################


def similarity(str1, str2):
    lstr1 = "".join([*filter(str.isalnum, str1.lower())])
    lstr2 = "".join([*filter(str.isalnum, str2.lower())])
    r1 = partial_ratio(lstr1, lstr2)
    r2 = partial_token_set_ratio(lstr1, lstr2)
    r3 = WRatio(lstr1, lstr2)
    r4 = token_set_ratio(lstr1, lstr2)
    return max([r1, r2, r3, r4])


def out(array, error):
    if len(array) != 0:
        out = array
    else:
        out = error

    return out

def search_book_by_title(title):
    BIDs = []
    cursor.execute("SELECT title, bid FROM books;")
    for row in cursor:
        if similarity(row[0], title) >= 71:
            BIDs.append(row[1])
    #    print(BIDs)
    return out(BIDs, 0)


# title = input("title: ")
# print(search_book_by_title(title))

def search_book_by_author(author):
    BIDs = []
    AIDs = []
    cursor.execute("SELECT name, aid FROM authors;")
    for row in cursor:
        if similarity(row[0], author) >= 71:
            AIDs.append(row[1])
    for AID in AIDs:
        cursor.execute(f"SELECT bid FROM books WHERE aid = {AID};")
        for row in cursor:
            BIDs.append(row[0])

    return out(BIDs, 0)


# author = input("author: ")
# print(search_book_by_author(author))

def search_book_by_description(description):
    BIDs = []
    cursor.execute("SELECT description, bid FROM books;")
    for row in cursor:
        if similarity(row[0], description) >= 71:
            BIDs.append(row[1])

    return out(BIDs, 0)


# description = input("description: ")
# print(search_book_by_description(description))

def search_author_by_name(name):
    AIDs = []
    cursor.execute("SELECT name, aid FROM authors;")
    for row in cursor:
        if similarity(row[0], name) >= 70:
            AIDs.append(row[1])

    return out(AIDs, 0)


# name = input("name: ")
# print(search_author_by_name(name))

def search_publisher_by_name(name):
    PIDs = []
    cursor.execute("SELECT name, pid FROM publishers;")
    for row in cursor:
        if similarity(row[0], name) >= 70:
            PIDs.append(row[1])

    return out(PIDs, 0)


# name = input("name: ")
# print(search_publisher_by_name(name))

def get_book_info(BID):
    details = {}
    cursor.execute(f"SELECT * FROM books WHERE bid = {BID};")
    for row in cursor:
        details["aid"] = row[1]
        details["pid"] = row[2]
        details["title"] = row[3]
        details["genre"] = row[4]
        details["type"] = row[5]
        details["isbn"] = row[6]
        details["availability"] = row[7]
        details["edition"] = row[8]
        details["no_of_copies"] = row[9]
        details["description"] = row[10]
        details["location"] = row[11]
    return out(details, 0)


# print(get_book_info(1))
# print(get_book_info(6))

def get_member_info(MID):
    details = {}
    cursor.execute(f"SELECT * FROM members WHERE mid = {MID};")
    for row in cursor:
        details["name"] = row[1]
        details["address"] = row[2]
        details["phone"] = row[3]
        details["gender"] = row[4]
        details["class"] = row[5]
        details["no_of_books_rented"] = row[6]
    return out(details, 0)

# print(get_member_info(1))
# print(get_member_info(11))

def get_author_info(AID):
    details = {}
    cursor.execute(f"SELECT * FROM authors WHERE aid = {AID};")
    for row in cursor:
        details["name"] = row[1]
        details["gender"] = row[2]
        details["dob"] = str(row[3])
        details["country"] = row[4]
        details["info"] = row[5]
        details["phone"] = str(row[6])
        details["contact"] = row[7]
    return out(details, 0)

def get_publisher_info(PID):
    details = {}
    cursor.execute(f"SELECT * FROM publishers WHERE pid = {PID};")
    for row in cursor:
        details["name"] = row[1]
        details["contact"] = row[2]
        details["details"] = row[3]
    return out(details, 0)


def display_books(limit, offset, aid="'%'", pid="'%'"):
    books = []

    if "'%'" not in [aid, pid]:
        error = 0
    else:
        error = 1

    cursor.execute(f"SELECT bid, title, genre, type, isbn, availability, edition, no_of_copies, location, description FROM books WHERE aid LIKE {aid} AND pid LIKE {pid} LIMIT {limit} OFFSET {offset};")
    for row in cursor:
        books.append(row)

    return out(books, error)


#print(display_books(2,2))
# print(display_books(0,0,2))
# print(display_books(0,0,5))
#print(display_books(10, 5))

def display_members(limit, offset):
    members = []
    cursor.execute(f"SELECT * FROM members LIMIT {limit} OFFSET {offset};")
    for row in cursor:
        members.append(row)

    return out(members, 1)


# print(display_members(2,0))


def display_authors(limit, offset):
    authors = []
    cursor.execute(f"SELECT * FROM authors LIMIT {limit} OFFSET {offset};")
    for row in cursor:
        row = list(row)
        row[3] = str(row[3])
        authors.append(row)

    return out(authors, 1)


# print(display_authors(2,0))

def display_publishers(limit, offset):
    publishers = []
    cursor.execute(f"SELECT * FROM publishers LIMIT {limit} OFFSET {offset};")
    for row in cursor:
        publishers.append(row)

    return out(publishers, 1)


# print(display_publishers(2,1))

def lend(bid, mid, timespan, date_obj=date.today()):
    book_info = get_book_info(bid)
    member_info = get_member_info(mid)
    date = str(date_obj)
    date = "'" + date + "'"
    return_date = str(date_obj + timedelta(days=timespan))
    return_date = "'" + return_date + "'"
    if book_info != 0 and member_info != 0:
        if book_info["availability"] > 0:
            if member_info["no_of_books_rented"] < member_info["class"]:
                cursor.execute(
                    f"INSERT INTO loan VALUES({bid}, {mid}, {date}, {return_date});"
                )
                cursor.execute(
                    f"UPDATE books SET availability = availability - 1 WHERE bid = {bid};"
                )
                cursor.execute(
                    f"UPDATE members SET no_of_books_rented = no_of_books_rented + 1 WHERE mid = {mid};"
                )
                cursor.execute(
                    f"UPDATE statistics SET no_of_loans = no_of_loans + 1 WHERE bid = {bid};"
                )
                cursor.execute(
                    f"UPDATE statistics SET month = {date} WHERE bid = {bid};"
                )
                connection.commit()
                out = 99
            else:
                out = 4
        else:
            out = 5
    else:
        out = 0

    return out


# print(lend(54,54,54))
# print(lend(2,2,30))

def calculate_fine(bid, mid, fee_per_day):
    book_info = get_book_info(bid)
    member_info = get_member_info(mid)
    if book_info != 0 and member_info != 0:
        loans = []
        cursor.execute(f"SELECT due_date FROM loan WHERE bid = {bid} AND mid = {mid};")
        out = None
        for row in cursor:
            loans.append(row)
        if len(loans) == 0:
            out = 7
        else:
            for loan in loans:
                today = date.today()
                due_date = str(loan[0]).split("-")
                due_date = date(int(due_date[0]), int(due_date[1]), int(due_date[2]))
                delta_date = today - due_date
                try:
                    delta_date = int(str(delta_date)[0:2])
                except:
                    delta_date = int(str(delta_date)[0:3])
                if delta_date > 0:
                    out = str(delta_date * fee_per_day)
                elif type(out) != str:
                    out = 99
                else:
                    out = int(out)
                    if delta_date * fee_per_day > out:
                        out = str(delta_date * fee_per_day)
    else:
        out = 0

    return out


# print(calculate_fine(4,8,10))

def return_book(bid, mid, fee_per_day):
    fine = calculate_fine(bid, mid, fee_per_day)
    if fine != 0:
        cursor.execute(f"DELETE FROM loan WHERE bid={bid} AND mid = {mid};")
        cursor.execute(
            f"UPDATE books SET availability = availability + 1 WHERE bid = {bid};"
        )
        cursor.execute(
            f"UPDATE members SET no_of_books_rented = no_of_books_rented - 1 WHERE mid = {mid};"
        )
        connection.commit()
        out = fine
    else:
        out = fine

    return out


# print(return_book(4,8,10))

def reserve_book(bid, mid, timespan, date_obj=date.today()):
    member_info = get_member_info(mid)
    book_info = get_book_info(bid)
    date = str(date_obj)
    date = "'" + date + "'"
    rs_date = str(date_obj + timedelta(days=timespan))
    rs_date = "'" + rs_date + "'"
    if member_info != 0 and book_info != 0:
        if book_info["availability"] > 0:
            if member_info["class"] > 1:
                if member_info["no_of_books_rented"] < member_info["class"]:
                    cursor.execute(
                        f"INSERT INTO reservation VALUES({bid}, {mid}, {date}, {rs_date});"
                    )
                    cursor.execute(
                        f"UPDATE books SET availability = availability - 1 WHERE bid = {bid};"
                    )
                    cursor.execute(
                        f"UPDATE members SET no_of_books_rented = no_of_books_rented + 1 WHERE mid = {mid};"
                    )
                    cursor.execute(
                        f"UPDATE statistics SET no_of_loans = no_of_loans + 1 WHERE bid = {bid};"
                    )
                    cursor.execute(
                        f"UPDATE statistics SET month = {date} WHERE bid = {bid};"
                    )
                    out = 99
                else:
                    out = 4
            else:
                out = 8
        else:
            out = 5
    else:
        out = 0
    return out


# print(reserve_book(9, 5, 10))

def add_member(details):
    try:
        data = (
            details["name"],
            details["address"],
            details["phone"],
            details["gender"],
            details["class"],
        )

        query = (
            "INSERT INTO members (name, address, phone, gender, class) VALUES"
            + "('"
            + data[0]
            + "','"
            + data[1]
            + "',"
            + str(data[2])
            + ",'"
            + data[3]
            + "',"
            + str(data[4])
            + ");"
        )
        cursor.execute(query)
        connection.commit()
        out = 99
    except:
        out = 9
    return out


# print(add_member({'name':'devanandan', 'address':'kavadithala manikandeswaram po', 'phone':94001063800, 'gender':'Male', 'class':1}))
# print(add_member({'name':'yadunandan', 'address':'peroorkada manikandeswaram po', 'phone':9400106380, 'gender':'Male', 'class':1}))
# print(add_member({'name': 'Devanandan N. Byju', 'address': 'Vazhayila, Manikandeswaram P. O. TVPM', 'phone': 9400106380, 'gender': 'Male', 'class': 3}))

def del_member(mid):
    names = []
    cursor.execute(f"SELECT name FROM members WHERE mid={mid};")
    for name in cursor:
        names.append(name)
    if len(names) != 0:
        details = get_member_info(mid)
        if details["no_of_books_rented"] > 0:
            out = 10
        else:
            cursor.execute(f"DELETE FROM members WHERE mid = {mid};")
            out = 99
    else:
        out = 0
    connection.commit()
    return out


# print(del_member(29))
# print(del_member(11))

def get_book_types():
    types = []
    cursor.execute("SELECT DISTINCT type FROM books;")
    for book_type in cursor:
        types.append(book_type[0])

    return out(types, [])

def get_author_names():
    names = []
    cursor.execute("SELECT DISTINCT name FROM authors;")
    for name in cursor:
        names.append(name[0])

    return out(names, [])

def get_publishers():
    publishers = []
    cursor.execute("SELECT DISTINCT name FROM publishers;")
    for publisher in cursor:
        publishers.append(publisher[0])

    return out(publishers, [])

def add_book(details):
    try:
        author_name = "'"+details["author"]+"'"
        cursor.execute(f"SELECT aid FROM authors WHERE name LIKE {author_name};")
        aid = cursor.fetchone()
        publisher_name = "'"+details["publisher"]+"'"
        cursor.execute(f"SELECT pid FROM publishers WHERE name LIKE {publisher_name};")
        pid = cursor.fetchone()
        pid, aid = pid[0], aid[0]

        data = (
            aid,
            pid,
            details["title"],
            details["genre"],
            details["type"],
            details["isbn"],
            1,
            details["edition"],
            1,
            details["description"],
            details["location"]
        )

        query = (
            "INSERT INTO books (aid, pid, title, genre, type, isbn, availability, edition, no_of_copies, description, location) VALUES"
            + "("
            + str(data[0])
            + ","
            + str(data[1])
            + ",'"
            + data[2]
            + "','"
            + data[3]
            + "','"
            + data[4]
            + "',"
            + str(data[5])
            + ","
            + str(data[6])
            + ","
            + str(data[7])
            + ","
            + str(data[8])
            + ",'"
            + data[9]
            + "','"
            + data[10]
            + "');"
        )
        cursor.execute(query)
        connection.commit()
        out = 99
    except:
        out = 9
    return out

#print(add_book({"title":"Harry Potter and the deathly hallows", "genre":"fiction - magic", "type":"Fiction", "isbn":5231568955566, "edition":1, "description":"harry potter book", "location":"Library shelf C", "author": "Harper Lee", "publisher": "Scholastic Press" }))

def delete_book(BID):
    book_details = get_book_info(BID)
    if book_details != 0:
        cursor.execute(f"DELETE FROM books WHERE bid = {BID};")
        connection.commit()
        out = book_details
    else:
        out = 0
    return out

def decrement_book(BID):
    book_details = get_book_info(BID)
    if book_details != 0:
        if book_details["no_of_copies"] > 1:
            cursor.execute(f"UPDATE books SET no_of_copies = no_of_copies - 1 WHERE bid = {BID};")
            connection.commit()
            out = 99
        else:
            out = 11
    else: out = 0

    return out