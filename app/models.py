# coding: utf-8
from . import db, login_manager
from flask_login import UserMixin# ,AnonymousUserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# from markdown import markdown

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20))
    tags = db.Column(db.String(20))
    date_time = db.Column(db.String(20))
    payable = db.Column(db.String(20))
    telephone = db.Column(db.String(20))
    content = db.Column(db.String(20))
    comment = db.Column(db.String(20))
    photo = db.Column(db.String(20))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    photo = db.relationship('BookPhoto', backref='b_photo')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class BookComment(db.Model):
    __tablename__ = 'book_comment'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(20))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class BookPhoto(db.Model):
    __tablename__ = 'book_photo'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(20))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))


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
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    photo = db.relationship('HousePhoto', backref='h_photo')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class HouseComment(db.Model):
    __tablename__ = 'house_comment'

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(20))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


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
    tags = db.Column(db.String(20))
    date_time = db.Column(db.String(20))
    payable = db.Column(db.String(20))
    telephone = db.Column(db.String(20))
    content = db.Column(db.String(20))
    comment = db.Column(db.String(20))
    photo = db.Column(db.String(20))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    photo = db.relationship('PhonePhoto', backref='p_photo')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PhoneComment(db.Model):
    __tablename__ = 'phone_comment'

    id = db.Column(db.Integer, primary_key=True)
    phone_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(20))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    phone_id = db.Column(db.Integer, db.ForeignKey('phone.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class PhonePhoto(db.Model):
    __tablename__ = 'phone_photo'

    id = db.Column(db.Integer, primary_key=True)
    phone_id = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(20))

    phone_id = db.Column(db.Integer, db.ForeignKey('phone.id'))


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    telephone = db.Column(db.String(11), unique=True)
    
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    house = db.relationship('House', backref='user_h')
    phone = db.relationship('Phone', backref='user_p')
    book = db.relationship('Book', backref='user_b')

    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        target.role = Role.query.filter_by(name='Guests').first()

    def __init__(self, username, password, email, telephone):
        self.username = username
        self.email = email
        self.telephone = telephone
        self.password = password

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password): #user login check password
        return check_password_hash(self.password_hash, password)

db.event.listen(User.username, 'set', User.on_created)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    users = db.relationship('User', backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
        db.session.commit()

