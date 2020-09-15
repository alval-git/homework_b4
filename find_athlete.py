import uuid
import datetime
# импортируем библиотеку sqlalchemy и некоторые функции из нее
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
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
class Athelete(Base):
    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key=True)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.Text)
def connect_db():
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()
def find_user(user_id):
    session = connect_db()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user
def find_by_heigth(user_height):
    session = connect_db()
    atheletes = session.query(Athelete).filter(Athelete.height > 0).all()
    session.close()
    closest_by_height = atheletes[0]
    for athelete in atheletes:
        user_height_diff = abs(closest_by_height.height - user_height)
        athelete_diff = abs(athelete.height - user_height)
        if athelete_diff < user_height_diff:
            closest_by_height = athelete
    return closest_by_height
def find_by_birtday(user_birth_date):
    session = connect_db()
    atheletes = session.query(Athelete).all()
    users = session.query(User).all()
    session.close()
    closest_birth = atheletes[0]
    for athelete in atheletes:
        atlt_birth_date = athelete.birthdate.split("-")
        user_birth_date = athelete.birthdate.split("-")
        closest_birth_date = closest_birth.birthdate.split("-")
        closest_birth_year = int(closest_birth_date[0])
        closest_birth_month = int(closest_birth_date[1])
        closest_birth_day = int(closest_birth_date[2])
        birth_year_atlt = int(atlt_birth_date[0])
        birth_month_atlt = int(atlt_birth_date[1])
        birth_day_atlt = int(atlt_birth_date[2])
        birth_year_usr = int(user_birth_date[0])
        birth_month_usr = int(user_birth_date[1])
        birth_day_usr = int(user_birth_date[2])
        if abs(birth_year_atlt - birth_year_usr) < abs(birth_year_atlt - closest_birth_year) :
            if abs(birth_month_atlt - birth_month_usr) < abs(birth_month_atlt - closest_birth_month):
                if abs(birth_day_atlt - birth_day_usr) < abs(birth_day_atlt - closest_birth_day):
                    closest_birth = athelete.birthdate
        return closest_birth
def main():
    user_id = int(input("Введите id пользователя"))
    user = find_user(user_id)
    if user_id:
        athelete_close_height = find_by_heigth(user.height)
        athelete_close_birth = find_by_birtday(user.birthdate)
        print("Вот ближайший по росту атлет: ", athelete_close_height.name, athelete_close_height.height )
        print("Вот ближайший по возрасту атлет", athelete_close_birth.name, athelete_close_birth.birthdate)
    else:
        print("Пользователь не найден")
if __name__ == "__main__":
    main()