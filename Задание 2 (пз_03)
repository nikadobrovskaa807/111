#Задание2
class Book: #создан класс
    def __init__(self, author: str, pages: int, year: int, title: str): #создан конструктор класса и его свойства
        self.__author = ""
        self.author = author #св-во автор
        self.__pages = 0
        self.pages = pages #св-во количество страниц
        self.__year = 0
        self.year = year #св-во год выпуска книги
        self.__title = ""
        self.title = title #св-во название книги

    def author(self): #метод для доступа к значениям свойств класса Book
        return self.__author

    def author(self, value): #метод с циклом показывающий, что в имени автора может использоватся "." и только буквы
        if all(char.isalpha() or char == "." for char in value):
            self.__author = value
        else:
            raise ValueError("Инициалы указаны не верно") #выводится сообщение об ошибке если инициалы указаны не верно

    def pages(self): #метод для доступа к значениям свойств класса Book
        return self.__pages

    def pages(self, value): #метод показывающий что страницы в книге должны быть не менее 5 и не более 2000 страниц
        if 5 >= value <= 2000:
            self._pages = value
        else:
            raise ValueError("Номер страницы указан не верно") #выводится сообщение об ошибке если номер страницы указан не верно

    def year(self): #метод для доступа к значениям свойств класса Book
        return self.__year

    def year(self, value): #метод с циклом показвающий что год издания книги не может быть больше текущего
        if value <= 'Текущий год':
            self.__year = value
        else:
            raise ValueError("Неверно указан год") #если год указан не верно - сообщение об ошибке

    def title(self): #метод для доступа к значениям свойств класса Book
        return self.__title

    def title(self, value): #метод с циклом указывающий то из скольки символов должно состоять название книги
        if len(value) <= 100 and value[0].isupper() and all(value[i - 1] == "." or value[i].isupper() for i in range(1, len(value))):
            self.__title = value
        else:
            raise ValueError("Не верно название книги") #если название указано не верно - сообщение об ошибке

#присваевание значений
book1 = Book("Стивин Кинг", 1248, 1986, "Оно")
book2 = Book("Павел Санаев", 576, 2013, "Хроники раздолбая")
book3 = Book("Дж. Кэмпбелл", 544, 1949, "Тысячеликий герой")
book4 = Book("Агата Кристи", 282, 1939, "Десять негритят")
book5 = Book("Евгений Замятин", 288, 1924, "Мы")
#вывод всех значений
print("Книга 1:")
print("Автор:", book1.author)
print("Количество страниц:", book1.pages)
print("Год выпуска:", book1.year)
print("Название:", book1.title)

print("\nКнига 2:")
print("Автор:", book2.author)
print("Количество страниц:", book2.pages)
print("Год выпуска:", book2.year)
print("Название:", book2.title)

print("\nКнига 3:")
print("Автор:", book3.author)
print("Количество страниц:", book3.pages)
print("Год выпуска:", book3.year)
print("Название:", book3.title)

print("\nКнига 4:")
print("Автор:", book4.author)
print("Количество страниц:", book4.pages)
print("Год выпуска:", book4.year)
print("Название:", book4.title)

print("\nКнига 5:")
print("Автор:", book5.author)
print("Количество страниц:", book5.pages)
print("Год выпуска:", book5.year)
print("Название:", book5.title)
