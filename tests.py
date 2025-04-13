import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


# Тест add_new_book
@pytest.mark.parametrize("book_name", ["Краткая история времени", "Гарри Поттер", "A" * 40])
def test_add_new_book_valid(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre()
    assert collector.get_book_genre(book_name) == ''

@pytest.mark.parametrize("book_name", ["", "A" * 41])
def test_add_new_book_invalid_length(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name not in collector.get_books_genre()


# Тест set_book_genre
def test_set_book_genre_valid(collector):
    collector.add_new_book("Ночной дозор")
    collector.set_book_genre("Ночной дозор", "Фантастика")
    assert collector.get_book_genre("Ночной дозор") == "Фантастика"

def test_set_book_genre_invalid_genre(collector):
    collector.add_new_book("Ночной дозор")
    collector.set_book_genre("Ночной дозор", "Поэзия")
    assert collector.get_book_genre("Ночной дозор") == ""


# Тест get_books_with_specific_genre
def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.set_book_genre("Книга 1", "Фантастика")
    collector.set_book_genre("Книга 2", "Ужасы")
    assert collector.get_books_with_specific_genre("Фантастика") == ["Книга 1"]


# Тест get_books_for_children
def test_get_books_for_children(collector):
    collector.add_new_book("Детская книга")
    collector.add_new_book("Страшная книга")
    collector.set_book_genre("Детская книга", "Мультфильмы")
    collector.set_book_genre("Страшная книга", "Ужасы")
    assert collector.get_books_for_children() == ["Детская книга"]


# Тест add_book_in_favorites
def test_add_book_in_favorites(collector):
    collector.add_new_book("Любимая книга")
    collector.add_book_in_favorites("Любимая книга")
    assert "Любимая книга" in collector.get_list_of_favorites_books()

def test_add_book_in_favorites_only_once(collector):
    collector.add_new_book("Любимая книга")
    collector.add_book_in_favorites("Любимая книга")
    collector.add_book_in_favorites("Любимая книга")
    assert collector.get_list_of_favorites_books().count("Любимая книга") == 1


# Тест delete_book_from_favorites
def test_delete_book_from_favorites(collector):
    collector.add_new_book("Книга для удаления")
    collector.add_book_in_favorites("Книга для удаления")
    collector.delete_book_from_favorites("Книга для удаления")
    assert "Книга для удаления" not in collector.get_list_of_favorites_books()


# Тест get_list_of_favorites_books
def test_get_list_of_favorites_books(collector):
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.add_book_in_favorites("Книга 1")
    collector.add_book_in_favorites("Книга 2")
    assert collector.get_list_of_favorites_books() == ["Книга 1", "Книга 2"]

#Тест get_book_genre
def test_get_book_genre_returns_correct_genre():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

#Тест get_books_genre
def test_get_books_genre_returns_full_dict():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Шерлок Холмс")
    expected = {
        "Гарри Поттер": "",
        "Шерлок Холмс": ""
    }
    assert collector.get_books_genre() == expected
