import unittest
from main import create_one_to_many, query_1, query_2, query_3, bookstores, books, book_store_links

class TestBookstoreQueries(unittest.TestCase):

    def setUp(self):
        self.bookstores = bookstores
        self.books = books
        self.book_store_links = book_store_links
        self.one_to_many = create_one_to_many(self.bookstores, self.book_store_links, self.books)

    def test_query_1(self):
        expected = {
            'Альфа книги': ['Python для начинающих', 'Алгоритмы и структуры данных', 'Анализ данных', 'Машинное обучение'],
            'Академия знаний': ['Анализ данных', 'Основы программирования', 'Python для начинающих']
        }
        result = query_1(self.bookstores, self.one_to_many)
        self.assertEqual(result, expected)

    def test_query_2(self):
        expected = [
            ('Альфа книги', 1200),
            ('Бета книги', 1200),
            ('Академия знаний', 800)
        ]
        result = query_2(self.bookstores, self.one_to_many)
        self.assertEqual(result, expected)

    def test_query_3(self):
        expected = {
            'Альфа книги': ['Python для начинающих', 'Алгоритмы и структуры данных', 'Анализ данных', 'Машинное обучение'],
            'Бета книги': ['Машинное обучение', 'Алгоритмы и структуры данных'],
            'Академия знаний': ['Анализ данных', 'Основы программирования', 'Python для начинающих']
        }
        result = query_3(self.bookstores, self.book_store_links, self.books)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
