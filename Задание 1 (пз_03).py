class Book: #создаем класс
    def __init__(self, author, numbwepages, yearofrelese): #создаем конструктор класса с свойствами (author, numbwepages, yearofrelese)
        self.__author = author #приватный
        self.__numbwepages = numbwepages #приватный
        self.__yearofrelese = yearofrelese #приватный

    def get_author(self): #метод предоставляет доступ к значениям свойств объекта класса Book
        return self.__author

    def set_author(self, author): #метод предоставляет доступ к значениям свойств объекта класса Book
        self.__author = author

    def get_numbwepages(self): #метод предоставляет доступ к значениям свойств объекта класса Book
        return self.__numbwepages

    def set_numbwepages(self, numbwepages): #метод предоставляет доступ к значениям свойств объекта класса Book
        self.__numbwepages = numbwepages

    def get_yearofrelese(self): #метод предоставляет доступ к значениям свойств объекта класса Book
        return self.__yearofrelese

    def set_yearofrelese(self, yearofrelese): #метод предоставляет доступ к значениям свойств объекта класса Book
        self.__yearofrelese = yearofrelese

book1 = Book ('Евгений Замятин', '288', '1924')
print(f'Книга1: автор - {book1.get_author()}, количество страниц - {book1.get_numbwepages()}, год выпуска - {book1.get_yearofrelese()}')
#вывод всех значений
