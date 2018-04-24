# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename
from os import path
from flask_bootstrap import Bootstrap
# from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy

# import mysql.connector

from flask_login import LoginManager, current_user
from flask_pagedown import PageDown
from flask_gravatar import Gravatar
from flask_babel import Babel, gettext as _
from config import config

class RegexConverter(object):
	"""docstring for RegexConverter"""
	def __init__(self, url_map, *items):
		super(RegexConverter,self).__init__()
		self.regex=items[0]


basedir = path.abspath(path.dirname(__file__))
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
pagedown=PageDown()
babel = Babel()

def create_app(config_name='default'):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	app.url_map.converters['regex'] = RegexConverter
	app.config.from_pyfile('config')
	app.config['BABEL_DEFAULT_LOACLE'] = 'zh'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:anye19951203@localhost/test?charset=utf8'
	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
	gravatar = Gravatar(app,
                    size=38,
                    rating='g',
                    default='retro',
                    force_default=False,
                    use_ssl=False,
                    base_url=None)#头像
	# Gravatar(app, size=64)

	db.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)
	pagedown.init_app(app)
	babel.init_app(app)


	from auth import auth as auth_blueprint
	from main import main as main_blueprint

	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	app.register_blueprint(main_blueprint, static_folder='static')

	@app.template_test('current_link')
	def is_current_link(link):
		return link == request.path
	return app
