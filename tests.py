import pytest
from main import BooksCollector

@pytest.fixture(scope="session")
def collector():
    return BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Отцы и дети')
        assert 'Отцы и дети' in collector.get_books_genre()

    def test_add_new_book_with_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    def test_add_new_book_with_name_longer_than_40_chars(self):
        collector = BooksCollector()
        collector.add_new_book('Тайны забытого мира: Путешествие во времени')
        assert 'Тайны забытого мира: Путешествие во времени' not in collector.get_books_genre()

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_with_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы для детей')
        assert collector.get_book_genre('Оно') == ''

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Обитаемый остров')
        collector.set_book_genre('Обитаемый остров', 'Фантастика')
        assert collector.get_book_genre('Обитаемый остров') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert 'Дюна' in collector.get_books_genre()

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Шрэк')
        collector.set_book_genre('Шрэк', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Шрэк']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Шрэк')
        collector.add_book_in_favorites('Шрэк')
        assert 'Шрэк' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Шрэк')
        collector.add_book_in_favorites('Шрэк')
        collector.add_book_in_favorites('Шрэк')
        assert 'Шрэк' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Шрэк')
        collector.add_book_in_favorites('Шрэк')
        collector.delete_book_from_favorites('Шрэк')
        assert 'Шрэк' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шрэк')
        collector.add_book_in_favorites('Шрэк')
        assert 'Шрэк' in collector.get_list_of_favorites_books()
