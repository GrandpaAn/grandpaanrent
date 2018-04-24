# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField
from flask_babel import gettext as _

class PostForm(Form):
	title = StringField(label=_(u"标题"), validators=[DataRequired()])
	body = PageDownField(label=_(u"正文"), validators=[DataRequired()])
	submit = SubmitField(_(u"发表"))

class HouseForm(Form):
	title = StringField(label=_(u"标题"), validators=[DataRequired()])
	place = StringField(label=_(u"地址"), validators=[DataRequired()])
	date_time = StringField(label=_(u"出租时间"), validators=[DataRequired()])
	community = StringField(label=_(u"小区"), validators=[DataRequired()])
	payable = StringField(label=_(u"价格"), validators=[DataRequired()])
	telephone = StringField(label=_(u"电话"), validators=[DataRequired()])
	content = PageDownField(label=_(u"描述"), validators=[DataRequired()])
	submit = SubmitField(_(u"发表"))

class PhoneForm(Form):
	title = StringField(label=_(u"标题"), validators=[DataRequired()])
	tags = StringField(label=_(u"品牌"), validators=[DataRequired()])
	date_time = StringField(label=_(u"出租时间"), validators=[DataRequired()])
	payable = StringField(label=_(u"价格"), validators=[DataRequired()])
	telephone = StringField(label=_(u"电话"), validators=[DataRequired()])
	content = PageDownField(label=_(u"描述"), validators=[DataRequired()])
	submit = SubmitField(_(u"发表"))

class BookForm(Form):
	title = StringField(label=_(u"标题"), validators=[DataRequired()])
	tags = StringField(label=_(u"地址"), validators=[DataRequired()])
	date_time = StringField(label=_(u"出租时间"), validators=[DataRequired()])
	payable = StringField(label=_(u"价格"), validators=[DataRequired()])
	telephone = StringField(label=_(u"电话"), validators=[DataRequired()])
	content = PageDownField(label=_(u"描述"), validators=[DataRequired()])
	submit = SubmitField(_(u"发表"))

class CommentForm(Form):
	body = PageDownField(label=_(u'评论'), validators=[DataRequired()])
	submit = SubmitField(_(u'发表'))
	