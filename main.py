import sys
import os

# Добавляем корневую директорию проекта в путь поиска модулей
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from my_project.database import initialize_database, Session, User
from my_project.logging_config import configure_logging

# Конфигурация логирования
configure_logging()

# Инициализация базы данных
initialize_database()

# Основная логика приложения
def main():
    session = Session()

    # Добавим пользователей
    user1 = User(name="Alice")
    user2 = User(name="Bob")
    session.add_all([user1, user2])
    session.commit()

    print(f"Количество пользователей: {session.query(User).count()}")
    print(f"Имя первого пользователя в верхнем регистре: {user1.get_uppercase_name()}")

if __name__ == '__main__':
    main()

