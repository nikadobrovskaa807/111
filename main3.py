class Book:
    def __init__(self, author: str, numbwepages: int, yearofrelese: int = None):
        self._author = None
        self._numbwepages = None
        self._apartment = None
        self.author = author
        self.numbwepages = numbwepages
        self.yearofrelese = yearofrelese


    def author(self):
        return self._author


    def author(self, value):
        if value.startswith('И. О. Фамилия'):
            self._author = 'И. О. Фамилия'
        else:
            raise ValueError('Неверно введены инициалы')


    def numbwepages(self):
        return self._numbwepages


    def numbwepages(self, value):
        if self._author == 'И. О. Фамилия' and (value < 10 or value > 50):
            raise ValueError('Инициалы автора должены быть от 10 до 50 символов')
        elif self._numbwepages == 'Количество страниц' and (value < 1 or value > 100):
            raise ValueError('Номер дома на улице должен быть от 5 до 2000')
        elif self._yearofrelese == 'Год выпуска' and (value < 1500 or value > 2024):
            raise ValueError('Год выпуска должен быть от 1500 до 2024')
        else:
            self._numbwepages = value

