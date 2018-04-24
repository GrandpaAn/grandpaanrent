# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from . import auth
from .forms import LoginForm, RegistrationForm, ChangePasswordForm
from ..models import User
from .. import db
from flask_login import login_user, logout_user, current_user, login_required
from flask_babel import gettext as _


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password.')
	# flash(u'登录成功')
	return render_template('login.html',title=_(u'用户登录'), form=form) # method=request.method

@auth.route('/logout')
def logout():
	if current_user.is_authenticated():
		logout_user()
	return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(username=form.username.data,
					password=form.password.data,
					email=form.email.data,
					telephone=form.telephone.data)

		db.session.add(user)
		db.session.commit()
		return redirect(url_for('auth.login'))

	return render_template('register.html',
							title=_(u'用户注册'),
							form=form)

@auth.route('/changepwd', methods=['GET', 'POST'])
@login_required
def changepwd():
	form = ChangePasswordForm()
	if form.validate_on_submit():
		if current_user.verify_password(form.old_password.data):
			current_user.password = form.password.data
			db.session.add(current_user)
			db.session.commit()
			flash('Your password has been updated.')
			return redirect(url_for('auth.logout'))
		else:
			flash('Invalid password.')
	return render_template("change_passwd.html",
							title = u'修改用户密码',
							form=form)
