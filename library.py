#Создание класса «Library», включающего в себя все методы, связанные с организацией работы консоли библиотеки.
import json
import uuid
from book import Book
import datetime
from datetime import datetime

class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    #Метод загрузки файла данных библиотеки из файла .json
    def load_data(self):
        try:
            with open('library.json', 'r') as f:
                data = json.load(f)
                for book_data in data:
                    book = Book(book_data['title'], book_data['author'], book_data['year'], book_data['status'])
                    self.books.append(book)
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Пустой файл или неверный JSON.

    #Метод сохранения данных библиотеки после выполнения с ней какой-либо операции.
    def save_data(self):
        data = []
        for book in self.books:
            data.append({
                'id' : book.id,
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'status': book.status
            })
        with open('library.json', 'w') as f:
            json.dump(data, f, indent=4)

    # Метод добавления книги в библиотеку.
    def add_book(self, title, author, year):
        try:
            assert title != ""
            assert author != ""
            assert int(year) <= int(datetime.now().year)
            assert int(year) > 0
            new_book = Book(title, author, year, "в наличии")
            self.books.append(new_book)
            self.save_data()
            print(f"Книга '{title}' успешно добавлена!")
        except:
            raise ValueError("Одно или несколько введенных значений недействительны.")

    # Метод для удалить книгу из библиотеки.
    def delete_book(self, book_id):
        ids = [book.id for book in self.books]
        for book in self.books:
            if (book_id in ids) and (book.id == book_id):
                self.books.remove(book)
                self.save_data()
                print(f"Книга '{book.title}' успешно удалена!")
                return
            else:
                raise ValueError("Идентификатор книги не найден")

    #Метод поиска книги в библиотеке
    def search_books(self, query):
        results = []
        if query == '':
            raise ValueError("Поисковый запрос пуст")
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        if results:
            print(f"Результаты поиска по '{query}':")
            for book in results:
                print(f"- {book.id} - {book.title} - {book.author} ({book.year}) - {book.status}")
        else:
            raise ValueError("Не найдено книг, соответствующих запросу")

    # Метод отображения всех книг в библиотеке
    def show_all_books(self):
        if self.books:
            print("Список книг:")
            for book in self.books:
                print(f"- {book.id} - {book.title} - {book.author} ({book.year}) - {book.status}")
        else:
            raise ValueError("Библиотека пуста!")
    #Метод изменения статуса книги в библиотеке
    def change_book_status(self, book_id, new_status):
        ids = [book.id for book in self.books]
        for book in self.books:
            if (book_id in ids) and (book.id == book_id) and (new_status in ('в наличии','выдана')):
                book.status = new_status
                self.save_data()
                print(f"Статус книги '{book.title}' успешно изменен на '{new_status}'!")
            else:
                raise ValueError("Идентификатор или новый статус недействителен.")
