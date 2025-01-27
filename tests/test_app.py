import unittest
from my_project.database import Session, User, initialize_database, get_user_count
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Инициализация базы данных
        initialize_database()
        # Используем in-memory SQLite базу данных для тестов
        cls.engine = create_engine('sqlite:///:memory:')  # in-memory база данных
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        # Создаем таблицы
        User.metadata.create_all(cls.engine)

    def setUp(self):
        # Очистка базы данных перед каждым тестом
        self.session.query(User).delete()  # Удаляем всех пользователей
        self.session.commit()

    def test_add_user(self):
        # Тест добавления пользователя
        user = User(name="John Doe")
        self.session.add(user)
        self.session.commit()
        # Проверяем, что в базе данных 1 пользователь
        self.assertEqual(self.session.query(User).count(), 1)

    def test_get_user_count(self):
        # Тест подсчёта пользователей
        user1 = User(name="John Doe")
        user2 = User(name="Jane Doe")
        self.session.add(user1)
        self.session.add(user2)
        self.session.commit()
        # Проверяем, что количество пользователей равно 2
        self.assertEqual(get_user_count(self.session), 2)

    @classmethod
    def tearDownClass(cls):
        # Очищаем таблицы после выполнения всех тестов
        User.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
