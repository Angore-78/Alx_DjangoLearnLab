from bookshelf.models import Book
book=Book()
deleted_book=book.get(title='1984')
print(f'{deleted_book} has been deleted from our inventory')
deleted_book.delete.()
# 1984 has been deleted from our inventory