from bookshelf.models import Book
book = Book()
updated_book=book.get(title=1984)
book.title='Nineteen Eighty-Four'
print(f'The book has been successfully updated to {updated_book.title}')
#The book has been successfully updated to Nineteen Eighty-Four 
