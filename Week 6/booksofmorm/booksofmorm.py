with open("C:/Users/jaj2k/Downloads/books (1).txt") as books:
    books = books.readlines()
    length = len(books)
    for i in range(length):
        print(books[i], end = '')

