class Student:
    def __init__(self, name, age, group, liter):
        self.__name = name
        self.__age = age
        self.__group = group
        self.__liter = liter

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

    def get_group(self):
        return self.__group

    def set_group(self,group):
        self.__group = group

    def get_liter(self):
        return self.__liter

    def set_liter(self,liter):
        self.__liter = liter
        return sum(liter) / len(liter)

stud = Student("Владлен", "18", "АВД(23)-Б", "3,4,5,3,5,4,5,3,5,4,5,3,4,5")
print(Student.__liter)