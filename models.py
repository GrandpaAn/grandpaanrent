# coding: utf-8
from sqlalchemy import Column, Enum, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    tags = Column(Enum(u'wenxue', u'tongshu', u'jiaoyu', u'renwen', u'shenghuo', u'kejijishu', u'other'), server_default=text("'other'"))
    date_time = Column(String(20))
    payable = Column(String(20))
    telephone = Column(String(20))
    content = Column(String(20))
    comment = Column(String(20))
    photo = Column(String(20))


class BookComment(Base):
    __tablename__ = 'book_comment'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    comment_id = Column(Integer)


class BookPhoto(Base):
    __tablename__ = 'book_photo'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    photo = Column(String(20))


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment = Column(String(20))


class House(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    place = Column(String(20))
    date_time = Column(String(20))
    community = Column(String(20))
    payable = Column(String(20))
    telephone = Column(String(20))
    content = Column(String(20))
    comment = Column(String(20))
    photo = Column(String(20))


class HouseComment(Base):
    __tablename__ = 'house_comment'

    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, nullable=False)
    comment_id = Column(Integer)


class HousePhoto(Base):
    __tablename__ = 'house_photo'

    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, nullable=False)
    photo = Column(String(20))


class Phone(Base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    tags = Column(Enum(u'xiaomi', u'huawei', u'samsung', u'chuizi', u'meizu', u'oppo', u'vivo', u'iphone', u'other'), server_default=text("'other'"))
    date_time = Column(String(20))
    payable = Column(String(20))
    telephone = Column(String(20))
    content = Column(String(20))
    comment = Column(String(20))
    photo = Column(String(20))


class PhoneComment(Base):
    __tablename__ = 'phone_comment'

    id = Column(Integer, primary_key=True)
    phone_id = Column(Integer, nullable=False)
    comment_id = Column(Integer)


class PhonePhoto(Base):
    __tablename__ = 'phone_photo'

    id = Column(Integer, primary_key=True)
    phone_id = Column(Integer, nullable=False)
    photo = Column(String(20))


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(20))
    email = Column(String(20))
    hid = Column(Integer, nullable=False)
    pid = Column(Integer, nullable=False)
    bid = Column(Integer, nullable=False)
    roles_id = Column(Integer)
