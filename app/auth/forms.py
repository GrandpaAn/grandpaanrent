# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField 
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Length, Required
from flask_babel import gettext as _


class LoginForm(Form):
	username = StringField(label=_(u'用户名/邮箱'), validators=[DataRequired()])
	password = PasswordField(label=_(u'密码'), validators=[DataRequired()])
	submit = SubmitField(label=_('Login'))

class RegistrationForm(Form):
	email = StringField(_(u'邮箱地址'), validators=[DataRequired(),
												Length(1, 64),
												Email()])

	username = StringField(_(u'用户名'), validators=[DataRequired(),
													Length(1, 64),
													Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
														_(u'用户名必须有字母、数字、下划线或 . 组成'))])

	telephone = StringField(_(u'手机号码'), validators=[DataRequired(),
													Length(1, 64)])

	password = PasswordField(_(u'密码'), validators=[DataRequired(),
													EqualTo('password2', 
													message='Passwords must match')])

	password2 = PasswordField(_(u'确认密码'), validators=[DataRequired()])
	
	submit = SubmitField(_(u'马上注册'))

class ChangePasswordForm(Form):
	old_password = PasswordField('Old password', validators=[Required()])
	password = PasswordField('New password', validators=[Required(), EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm new password', validators=[Required()])
	submit = SubmitField('Update Password')