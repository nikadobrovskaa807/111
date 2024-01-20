class Book:
    def __init__(self, author, numbwepages, yearofrelese):
        self.__author = author
        self.__numbwepages = numbwepages
        self.__yearofrelese = yearofrelese

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_numbwepages(self):
        return self.__numbwepages

    def set_numbwepages(self, numbwepages):
        self.__numbwepages = numbwepages

    def get_yearofrelese(self):
        return self.__yearofrelese

    def set_yearofrelese(self, yearofrelese):
        self.__yearofrelese = yearofrelese


