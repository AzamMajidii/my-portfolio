
class Library:
    def __init__(self):
        self.books = []
        
        
    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)
        print(f"ثبت شد: {title}, {author}")
        
        
    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"کتاب {title} حذف شد.")
                return
        print(f"{title} در کتابخانه موجود نیست!")
        return 

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                print(f"{title}")
                return book
        print(f"{title} یافت نشد!")
        return
    
    
    def show_books(self):
        print("لیست کتابها:")
        for book in self.books:
            print(f"{book["title"]}, {book["author"]}")
            
    
print(__name__)