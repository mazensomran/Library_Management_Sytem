#Создание класса «Book», включающиго все параметры книги в библиотеке.
import uuid
class Book:
    def __init__(self,title, author, year, status):
        self.id =str(uuid.uuid4()) #Сгенерируйте случайный идентификационный номер для каждой книги с помощью модуля uuid
        self.title = title
        self.author = author
        self.year = year
        self.status=status
