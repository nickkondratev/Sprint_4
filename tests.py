import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'Название_книги_которое_очень_длинное_и_больше_40_символов'])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_get_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга 1' in result
        assert 'Книга 2' not in result

    def test_get_books_with_specific_genre_returns_list_of_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 3', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert len(result) == 2

    def test_get_books_genre_returns_current_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.get_books_genre() == {'Война и мир': ''}

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_excludes_age_rating(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', genre)
        assert 'Страшная книга' not in collector.get_books_for_children()

    def test_get_books_for_children_includes_safe_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        collector.set_book_genre('Дюна', 'Фантастика')
        result = collector.get_books_for_children()
        assert 'Смешарики' in result
        assert 'Дюна' in result

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert collector.get_list_of_favorites_books() == ['Любимая книга']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')
        collector.delete_book_from_favorites('Книга для удаления')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Уникальная книга')
        collector.add_book_in_favorites('Уникальная книга')
        collector.add_book_in_favorites('Уникальная книга')
        assert collector.get_list_of_favorites_books().count('Уникальная книга') == 1