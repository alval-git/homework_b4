import uuid
import datetime
# импортируем библиотеку sqlalchemy и некоторые функции из нее
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
def connect_db():
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()
def request_data():
    print("Введите свои данные")
    first_name = input("Введите свое имя")
    last_name = input("Введите свою фамилию")
    gender = input("Введите свой пол")
    email = input("Введите свой email")
    birthdate  = input("Введите свою дату рождения")
    height = input("Введите свой рост")
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    session = connect_db()
    # проверяем режим
        # запрашиваем данные пользоватлея
    user = request_data()
        # добавляем нового пользователя в сессию
    session.add(user)
        # сохраняем все изменения, накопленные в сессии
    session.commit()
    print("Спасибо, данные сохранены!")
if __name__ == "__main__":
    main()



