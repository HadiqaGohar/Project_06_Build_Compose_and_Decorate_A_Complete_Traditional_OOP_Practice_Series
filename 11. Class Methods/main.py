# 11. Class Methods

# Assignment:
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.


# ************************ Old Code ************************


# class Book:
#     total_books = 0
      
#     @classmethod
#     def increment_book_count(cls):
#         cls.total_books += 1
#         print(f"Total books: {cls.total_books}")
#         # Example usage
#     @classmethod
#     def add_book(cls):
#         cls.increment_book_count()
#         print("A new book has been added.")

# # Example usage
# book1 = Book()
# book1.add_book()  # Output: Total books: 1
# book2 = Book()
# book2.add_book()  # Output: Total books: 2
# book3 = Book()
# book3.add_book()  # Output: Total books: 3


# ************************ Updated Code ************************


class Book:
    total_books = 0

    def __init__(self, name):
        self.name = name
        print(f"📚 Book '{self.name}' created.")

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"🔢 Total books: {cls.total_books}")

    @classmethod
    def add_book(cls, name):
        book = cls(name)
        cls.increment_book_count()
        return book

# Start the loop
print("📖 Welcome to the Book Manager!")
print("Type 'exit' to stop adding books.\n")

while True:
    book_name = input("Enter book name: ")
    if book_name.lower() == "exit":
        print("\n Final book count:", Book.total_books)
        print("\n🚪 Exiting...")
        break
    Book.add_book(book_name)
