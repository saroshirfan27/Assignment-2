books = { 'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }, 'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }, 'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } } 

books['book4'] = { 'title': 'Macbeth', 'author': 'William Shakespeare', 'year': 1623 }
print(books)
print( "\n\ntitles are\n")
index = 'book1'
for i in books:
    print(books[i]['title'])
    if (books[i]['year'] < books[index]['year']):
        index = i
print("\n the earliest publication was in " + str(books[index]['year']) + " title is " + str(books[index]['title']) + " author is " + 
str(books[index]['author']) 
