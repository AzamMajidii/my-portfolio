
from mylibrary import Library

lib = Library()

lib.add_book("جای خالی سلوچ", "محمد دولت آبادی")
lib.add_book("قلعه مالویل", "روبر مرل")
lib.add_book("دیوان نمایش 1", "بهرام بیضایی")
lib.add_book("دیوان نمایش 2", "بهرام بیضایی")
lib.add_book("دیوان نمایش 3", "بهرام بیضایی")


lib.remove_book("دیوان نمایش 3")

lib.search_book("قلعه مالویل")

lib.show_books()


print(__name__)


def main():
    lib = Library()

    while True:
        print(">>>>>>>>>> Menu library <<<<<<<<<<")
        print("1- Add book")
        print("2- Delete book")
        print("3- Search")
        print("4- Exit")
        
        Select = input("Please Select: ")
    
        if Select == "1":
            title = input("Title: ")
            author = input("Outhor: ")
            lib.add_book(title, author)
            
        elif Select == "2":
            title = input("Title: ")
            lib.remove_book(title)
            
        elif Select == "3":
            title = input("Title: ")
            lib.search_book(title)
            
        elif Select == "4":
            print("Exit...")
            break
        
        else:
            break
        
        
 
if __name__ == "__main__":
    main()

