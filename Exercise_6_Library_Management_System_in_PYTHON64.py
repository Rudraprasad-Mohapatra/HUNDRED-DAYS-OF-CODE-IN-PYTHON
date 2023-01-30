"""
Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!
"""


class Library:
    books = []
    no_of_books = 0
    
    # def CountingBooks(fx):
    #     def mfx(*args,**kwargs):
    #         fx(*args,**kwargs)
    #         print("Your Total Book is:",len(list(args[0])))
    #         print("Thanks for using our libraray!")
    #     return mfx
    # def length(self,listBook):
    #     return len(listBook)
    # @CountingBooks
    def __init__(self, pbooks):
        for i in pbooks:
            self.books.append(i)
    
    # @CountingBooks
    def AddaNewBook(self, NewBook):
        self.books.append(NewBook)
        print()
        print(f'We have added "{NewBook}" to your library book list.')

    
    @property
    def PrintBooks(self):
        print("Your books are:",end=" ")
        for i in range(0, len(self.books)):
            print(self.books[i] ,end=" , ")
    @property        
    def total_no_of_books(self):
        print(f'You have total "{len(self.books)}" books')            

    

lib = Library(["Mathematics", "Physics","Thory Of Computation", "Compiler Design"])
lib.PrintBooks
lib.total_no_of_books
lib.AddaNewBook("PYTHON")
lib.PrintBooks
lib.total_no_of_books
