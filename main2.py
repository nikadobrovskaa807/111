class Book:
# свойства title, self, author, isbn
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):
        return self.__title

    def set_title(self,title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self,author):
        self.__author= author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self,isbn):
        self.__isbn = isbn
# Методы выше (пр. get_title) предоставляют доступ к значениям свойств объекта класса Book
book1 = Book("Вино из одуванчиков", "Рей Бредбери", "111111111111111")
print(book1._get.title())
print(book1.get_author())
print(book1.get_isbn())
book1.set_title("Рей Бредбери")
print(book1.get_title())

#####################################################################

