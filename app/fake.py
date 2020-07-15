from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from .import db
from .models import User, Article

def users(count=100):
    fake = Faker()
    i = 0
    while 1 < count:
        u = User(email=fake.email(),
                 username=fake.user_name(),
                 password='password',
                 confirmed=True,
                 name=fake.name(),
                 location=fake.city(),
                 about_me=fake.text()
                 )
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def articles(count=100):
    fake = Faker()
    user_count = User.query.count()
    for i in range(count):
        # u = User.query.offset(randint(0, user_count - 1)).first()
        a = Article(body=fake.text(),
                    url = fake.text(),
                    title = fake.text(),
                    subject = "News",
                    published = "July 14, 2020",
                    fake = True,
                    searched_by = 10)
        db.session.add(a)
    db.session.commit()