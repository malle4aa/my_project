import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Загрузка конфигурации из config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Настройка базы данных
engine = create_engine(config['database_url'])
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Модель пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def get_uppercase_name(self):
        """Возвращает имя пользователя в верхнем регистре"""
        return self.name.upper()

# Функция подсчёта пользователей
def get_user_count(session):
    """Подсчитывает количество пользователей в базе"""
    return session.query(User).count()

# Инициализация базы данных
def initialize_database():
    Base.metadata.create_all(engine)
    print("Database initialized")
