import pytest
import uuid
from library import Library
from book import Book
@pytest.fixture() #Для создания многоразовых тестовых данных
def setup_library():
    library = Library()
    library.books.clear()
    library.add_book("Тестовая книга", "Тестовой автор", 2024)
    return library
# Метод тестирования функции добавления новых книг в базу данных библиотеки
def test_add_book_valid_data(setup_library):
    library= setup_library
    library.add_book("Новая книга", "Новый автор", 2023)
    books = library.books
    assert len(books) == 2
    assert books[1].title == "Новая книга"
    assert books[1].author == "Новый автор"
    assert books[1].year == 2023
    assert books[1].status == "в наличии"

# Метод тестирования функции добавления книги без названия
def test_add_book_empty_title(setup_library):
    library= setup_library
    with pytest.raises(ValueError):
        library.add_book("", "Новый автор", 2023)
# Метод тестирования функции добавления книги с неверной датой публикации
def test_add_book_negative_year(setup_library):
    library= setup_library
    with pytest.raises(ValueError):
        library.add_book("Новая книга", "Новый автор", -2023)
# Метод тестирования функции удаления книги, которой не существует
def test_delete_book_nonexistent_id(setup_library):
    library= setup_library
    nonexistent_id = uuid.uuid4()
    with pytest.raises(ValueError):
        library.delete_book(nonexistent_id)

# Метод тестирования функции поиска книги без названия поиска
def test_search_books_empty_query(setup_library):
    library = setup_library
    with pytest.raises(ValueError):
        library.search_books("")

# Метод тестирования функции поиска книги, не соответствующей содержимому базы данных
def test_search_books_no_matching_results(setup_library):
    library = setup_library
    with pytest.raises(ValueError):
        library.search_books("Термин не найден")

# Метод тестирования функции отображения пустых библиотечных книг
def test_show_all_books_empty_library(setup_library):
    library = setup_library
    library.books.clear()
    with pytest.raises(ValueError):
        library.show_all_books()

# Метод тестирования функции изменения статуса книги
def test_change_book_status_valid_id_and_status(setup_library):
    library = setup_library
    book_id = library.books[0].id
    new_status = "выдана"
    library.change_book_status(book_id, new_status)
    assert library.books[0].status == new_status

# Метод тестирования функции изменения статуса книги с неверным идентификатором
def test_change_book_status_invalid_id(setup_library):
    library = setup_library
    invalid_id = uuid.uuid4()
    new_status = "выдана"
    with pytest.raises(ValueError):
        library.change_book_status(invalid_id, new_status)
# Метод тестирования функции изменения статуса книги с недопустимым статусом
def test_change_book_status_invalid_status(setup_library):
    library = setup_library
    book_id = library.books[0].id
    invalid_status = "недействительный"
    with pytest.raises(ValueError):
        library.change_book_status(book_id, invalid_status)
#Метод тестирования функции изменения статуса книги на "в наличии"
def test_change_book_status_to_available(setup_library):
    library = setup_library
    book_id = library.books[0].id
    new_status = "в наличии"
    library.change_book_status(book_id, new_status)
    assert library.books[0].status == new_status

if __name__ == "__main__":
    setup_library = setup_library()
    test_add_book_valid_data(setup_library)
    test_add_book_empty_title(setup_library)
    test_add_book_negative_year(setup_library)
    test_delete_book_nonexistent_id(setup_library)
    test_search_books_empty_query(setup_library)
    test_search_books_no_matching_results(setup_library)
    test_show_all_books_empty_library(setup_library)
    test_change_book_status_valid_id_and_status(setup_library)
    test_change_book_status_invalid_id(setup_library)
    test_change_book_status_invalid_status(setup_library)
    test_change_book_status_to_available(setup_library)
