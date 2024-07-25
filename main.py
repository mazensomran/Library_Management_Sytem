from library import Library
import uuid
def main():
    library = Library()

    while True: #Отображение вариантов консоли, позволяющих пользователю выбрать выполнение желаемой операции.
        print("\n**Список опций:**")
        print("1.Добавление книги")
        print("2.Удаление книги")
        print("3.Поиск книги")
        print("4.Отображение всех книг")
        print("5.Изменение статуса книги")
        print("6.удалить все")
        print("7.Выход")

        choice = input("Введите номер выбора: ")

        if choice == '1': #Номер 1: Процесс добавления книги требует ввода названия книги, имени автора и года публикации.
            title = input("Введите название книги")
            author = input("Введите имя автора")
            year = input("Введите год издания ")
            library.add_book(title, author, year)
        elif choice == '2': #Номер 2: Процесс удаления книги и требует от пользователя ввода идентификатора книги.
            book_id = input("Введите Идентификатор книги:")
            try: #Проверка существования идентификатора книги в базе данных библиотеки.
                book_id = uuid.UUID(book_id)
                library.delete_book(book_id)
            except ValueError: #Возникновение ошибки, если идентификатор книги неверен
                print("Идентификатор книги недействителен")
        elif choice == '3': #Номер 3 для процесса поиска книг
            query = input("Введите поисковый запрос: ")
            library.search_books(query)
        elif choice == '4': #Номер 4 для процесса отображения всех книг в библиотеке
            library.show_all_books()
        elif choice == '5': #Номер 5 для процесса изменения состояния книги
            book_id = input("Введите Идентификатор книги: ")
            new_status = input("Введите новый статус (в наличии/выдана):")
            try:
                book_id = uuid.UUID(book_id)
                library.change_book_status(book_id, new_status)
            except ValueError:
                print("Идентификатор книги недействителен")

        elif choice == '6': #Номер 6 для выхода из консоли
            break
        else:
            print("Неверный вариант, попробуйте еще раз.")

if __name__ == "__main__":
    main()