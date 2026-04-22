import pytest
from main import BooksCollector


class TestBooksCollector:

    # 1. add_new_book добавляет книги
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. add_new_book не добавляет книги с невалидным именем 
    @pytest.mark.parametrize('name', ['', 'Название_книги_которое_очень_длинное_и_больше_40_символов'])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # 3. set_book_genre устанавливает жанр существующей книге
    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    # 4. get_book_genre выводит жанр по имени
    def test_get_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 5. get_books_with_specific_genre список книг определённого жанра
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.set_book_genre('Книга 3', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert len(result) == 2 and 'Книга 1' in result and 'Книга 3' in result

    # 6. get_books_genre возвращает словарь книг
    def test_get_books_genre_returns_current_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.get_books_genre() == {'Война и мир': ''}

    # 7. get_books_for_children не возвращает книги с возрастным рейтингом 
    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_excludes_age_rating(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', genre)
        assert 'Страшная книга' not in collector.get_books_for_children()

    # 8. add_book_in_favorites добавляет книгу в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert collector.get_list_of_favorites_books() == ['Любимая книга']

    # 9. delete_book_from_favorites удаляет книгу из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')
        collector.delete_book_from_favorites('Книга для удаления')
        assert len(collector.get_list_of_favorites_books()) == 0

    # 10. add_book_in_favorites + get_list_of_favorites_books не добавляет дубликат
    def test_add_book_in_favorites_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Уникальная книга')
        collector.add_book_in_favorites('Уникальная книга')
        collector.add_book_in_favorites('Уникальная книга')
        assert collector.get_list_of_favorites_books().count('Уникальная книга') == 1
