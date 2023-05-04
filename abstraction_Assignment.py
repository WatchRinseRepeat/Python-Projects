from abc import ABC, abstractmethod  #import the abstract method class

class Book(ABC):
    def write(self, writing, pageNumber):
        print("You add '{}' to the book on page {}.".format(writing,pageNumber))

    #add the abstract method
    @abstractmethod
    def tearPage(self, pageNumber):
        pass

class NoteBook(Book):
    #define how to implement the class from the parent class
    def tearPage(self, pageNumber):
        print('You tear out page number {}, but it\'s okay because this is a notebook.'.format(pageNumber))



book = NoteBook()
book.write('Hello World',3)
book.tearPage(3)
