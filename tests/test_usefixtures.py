import pytest


@pytest.fixture()
def clear_books_database() -> None:
    print("[Fixture] Удаляем все данные из базы данных")

@pytest.fixture()
def fill_books_database() -> None:
    print("[Fixture] Создаем новые данные в базы данных")

@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print("Reading all books")


@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...
    def test_delate_book_from_library(self):
        ...