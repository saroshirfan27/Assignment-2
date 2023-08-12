# Assignment-2

# q1
temperatures = [25, 30, 27, 22, 28, 33, 29] 
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') 

list_new = { temperatures[0] : days[0] }
for i in range(0,len(temperatures) - 1):
    list_new[temperatures[i]] = days[i]
print(list_new)

temp = max( list_new )
print( str(temp) + " and " + str( list_new[temp] ) + " is the maximum temperature ")
print(str(sum(temperatures)/len(temperatures)) + " is the average temperature")

#q2
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
str(books[index]['author']) )
