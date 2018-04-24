# coding: utf-8
from . import db, login_manager
from flask_login import UserMixin# ,AnonymousUserMixin
from datetime import datetime
from markdown import markdown


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20))
    tags = db.Column(db.Enum(u'wenxue', u'tongshu', u'jiaoyu', u'renwen', u'shenghuo', u'kejijishu', u'other'), server_default=text("'other'"))
    date_time = db.Column(db.String(20))
    payable = db.Column(db.String(20))
    telephone = db.Column(db.String(20))
    content = db.Column(db.String(20))
    comment = db.Column(db.String(20))
    photo = db.Column(db.String(20))

    photo = db.relationship('BookPhoto', backref='photo')

    @staticmethod
    def on_content_changed(target, value, oldvalue, initiator):
        if value is None or (value is ''):
            target.content = ''
        else:
            target.content = markdown(value)


class BookComment(db.Model):
    __tablename__ = 'book_comment'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(20))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))



class BookPhoto(db.Model):
    __tablename__ = 'book_photo'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(20))


class House(db.Model):
    __tablename__ = 'house'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20))
    place = db.Column(db.String(20))
    date_time = db.Column(db.String(20))
    community = db.Column(db.String(20))
    payable = db.Column(db.String(20))
    telephone = db.Column(db.String(20))
    content = db.Column(db.String(20))
    comment = db.Column(db.String(20))
    photo = db.Column(db.String(20))

    photo = db.relationship('HousePhoto', backref='photo')



class HouseComment(db.Model):
    __tablename__ = 'house_comment'

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(20))


class HousePhoto(db.Model):
    __tablename__ = 'house_photo'

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(20))

    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))



class Phone(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20))
    tags = db.Column(db.Enum(u'xiaomi', u'huawei', u'samsung', u'chuizi', u'meizu', u'oppo', u'vivo', u'iphone', u'other'), server_default=text("'other'"))
    date_time = db.Column(db.String(20))
    payable = db.Column(db.String(20))
    telephone = db.Column(db.String(20))
    content = db.Column(db.String(20))
    comment = db.Column(db.String(20))
    photo = db.Column(db.String(20))

    photo = db.relationship('PhonePhoto', backref='photo')



class PhoneComment(db.Model):
    __tablename__ = 'phone_comment'

    id = db.Column(db.Integer, primary_key=True)
    phone_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(20))


class PhonePhoto(db.Model):
    __tablename__ = 'phone_photo'

    id = db.Column(db.Integer, primary_key=True)
    phone_id = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(20))

    phone_id = db.Column(db.Integer, db.ForeignKey('phone.id'))



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    users = db.relationship('User', backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    telephone = db.Column(db.String(120), unique=True)
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        target.role = Role.query.filter_by(name='Guests').first()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))