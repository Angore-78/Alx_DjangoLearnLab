from bookshelf.models import Book
Book.object.get(title='1984')
print(f'Retrieved {Book.object}) 

#Retrieved 1984