# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, make_response, abort, flash, current_app, send_from_directory#, send_static_file
from flask_login import login_required, current_user, login_user, logout_user
from . import main
from .. import db
from ..models import * 
from .forms import CommentForm, PostForm, HouseForm, PhoneForm, BookForm#, UploadForm
from flask_babel import gettext as _
import os
from werkzeug import secure_filename
# from flask_wtf import FlaskForm



@main.route('/')
def index():
	# response = make_response(render_template('index.html', title="Welcome to Grandpaan's Blog", body='# Header1'))
	# response.set_cookie('username', '')
	# posts = Post.query.all()
	# print posts
	# page_index = request.args.get('page', 1, type=int)

	# # query = House.query.order_by(Post.created.desc())

	# pagination = query.paginate(page_index, per_page=20, error_out=False)

	# posts = pagination.items	
	return render_template('index.html', 
							title=u"Welcome to Grandpaan Rent")
							#pagination=pagination, posts=posts,

# house页面展示
@main.route('/house')
def house():
	# page_index = request.args.get('page', 1, type=int)

	# query = House.query.order_by(Post.created.desc())

	# pagination = query.paginate(page_index, per_page=20, error_out=False)

	# posts = pagination.items
	return render_template('house.html',
							title="House")

# phone页面展示
@main.route('/phone')
def phone():
	# page_index = request.args.get('page', 1, type=int)

	# query = Post.query.order_by(Post.created.desc())

	# pagination = query.paginate(page_index, per_page=20, error_out=False)

	# posts = pagination.items
	return render_template('phone.html',
							title="phone")
	#路由
# @main.route('/user/<regex("[a-z]{3}"):user_id>')
# def user(user_id):
# 	return 'User %s' % user_id


# book页面展示
@main.route('/books/')
@main.route('/books-page/')
def book():
	# page_index = request.args.get('page', 1, type=int)

	# query = Post.query.order_by(Post.created.desc())

	# pagination = query.paginate(page_index, per_page=20, error_out=False)

	# posts = pagination.items
	return render_template('book.html',
							title="Book")

@main.route('/chiose', methods=['GET', 'POST'])
@main.route('/chiose/<int:id>', methods=['GET', 'POST'])
@login_required
def chiose():
	return render_template('posts/chiose.html')

@main.route('/h_post/<int:id>', methods=['GET', 'POST'])
def houserent_post(id):
	post = House.query.get_or_404(id)
	comments = HouseComment.query.filter_by(house_id=post.id)
	user = User.query.filter_by(id=post.user_id).first()
	# c_user = User.query.get_or_404(id)
	# 评论窗体
	form = CommentForm()
	# 保存评论
	if form.validate_on_submit():
		comment = HouseComment(user_id = current_user.id, house_id = post.id, comment = form.body.data)#, post = post
		db.session.add(comment)
		db.session.commit()

	return render_template('posts/detail.html',
							form=form,
							post=post,
							user=user,
							comments=comments)#,c_user=c_user

@main.route('/p_post/<int:id>', methods=['GET', 'POST'])
def phonerent_post(id):
	post = Phone.query.get_or_404(id)
	comments = PhoneComment.query.filter_by(phone_id=post.id)
	user = User.query.filter_by(id=post.user_id).first()
	# c_user = User.query.get_or_404(id)
	# 评论窗体
	form = CommentForm()
	# 保存评论
	if form.validate_on_submit():
		comment = PhoneComment(user_id = current_user.id, phone_id = post.id, comment = form.body.data)#, post = post
		db.session.add(comment)
		db.session.commit()

	return render_template('posts/detail.html',
							form=form,
							post=post,
							user=user,
							comments=comments)

@main.route('/h_post/<int:id>', methods=['GET', 'POST'])
def bookrent_post(id):
	post = Book.query.get_or_404(id)
	comments = BookComment.query.filter_by(house_id=post.id)
	user = User.query.filter_by(id=post.user_id).first()
	# c_user = User.query.get_or_404(id)
	# 评论窗体
	form = CommentForm()
	# 保存评论
	if form.validate_on_submit():
		comment = BookComment(user_id = current_user.id, book_id = post.id, comment = form.body.data)#, post = post
		db.session.add(comment)
		db.session.commit()

	return render_template('posts/detail.html',
							form=form,
							post=post,
							user=user,
							comments=comments)


@main.route('/houserent', methods=['GET', 'POST'])
@main.route('/houserent/<int:id>', methods=['GET', 'POST'])
@login_required
def houserent(id=0):
	form = HouseForm()
	if id == 0:
		h_post = House(user_id=current_user.id)
	else:
		h_post = House.query.get_or_404(id)

	if form.validate_on_submit():
		h_post.title = form.title.data
		h_post.place = form.place.data
		h_post.date_time = form.date_time.data
		h_post.community = form.community.data
		h_post.payable = form.payable.data
		h_post.telephone = form.telephone.data
		h_post.content = form.content.data

		db.session.add(h_post)
		db.session.commit()
		return redirect(url_for('main.houserent_post', id=h_post.id))
	form.title.data = h_post.title
	form.content.data = h_post.content
	return render_template('posts/houserent.html',
							post=h_post,
							form=form)#,title=title

@main.route('/bookrent', methods=['GET', 'POST'])
@main.route('/bookrent/<int:id>', methods=['GET', 'POST'])
@login_required
def bookrent(id=0):
	# post = None
	form = BookForm()
	if id == 0:
		b_post = Book(user_id=current_user.id)
	else:
		b_post = Book.query.get_or_404(id)

	if form.validate_on_submit():
		b_post.title = form.title.data
		b_post.tags = form.tags.data
		b_post.date_time = form.date_time.data
		# b_post.community = form.community.data
		b_post.payable = form.payable.data
		b_post.telephone = form.telephone.data
		b_post.content = form.content.data
		print(form.title.data, form.content.data)

		db.session.add(b_post)
		db.session.commit()
		return redirect(url_for('main.bookrent_post', id=b_post.id))

	form.title.data = b_post.title
	form.content.data = b_post.content

	return render_template('posts/bookrent.html',
							post=b_post,
							form=form)
							# ,title=title,post=post

@main.route('/phonerent', methods=['GET', 'POST'])
@main.route('/phonerent/<int:id>', methods=['GET', 'POST'])
@login_required
def phonerent(id=0):
	# post = None
	form = PhoneForm()
	if id == 0:
		p_post = Phone(user_id=current_user.id)
	else:
		p_post = Phone.query.get_or_404(id)

	if form.validate_on_submit():
		p_post.title = form.title.data
		p_post.tags = form.tags.data
		p_post.date_time = form.date_time.data
		# p_post.community = form.community.data
		p_post.payable = form.payable.data
		p_post.telephone = form.telephone.data
		p_post.content = form.content.data
		print(form.title.data, form.content.data)

		db.session.add(p_post)
		db.session.commit()
		return redirect(url_for('main.phonerent_post', id=p_post.id))
	form.title.data = p_post.title
	form.content.data = p_post.content
	return render_template('posts/phonerent.html',
							post=p_post,
							form=form)
							# ,title=title,post=post

@main.errorhandler(404)
def page_not_found(error):
	return render_template('404.html')



@main.route('/user')
@login_required
def user():
	return render_template('user.html')



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1] in set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG'])

@main.route('/uploadfile')
def uploadfile():
	return render_template('uploadfile.html')

# Route that will process the file upload
@main.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		uploaded_files = request.files.getlist("file[]")
		filenames = []
		for file in uploaded_files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join('static', filename))
				filenames.append(filename)
				# for file in filenames:
				# 	print(file)
		return render_template('upload.html', filenames=filenames)

@main.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory('static', filename)

# @main.route('/<path>')
# def today(path):
#     base_dir = os.path.dirname(__file__)
#     resp = make_response(open(os.path.join(base_dir, path)).read())
#     resp.headers["Content-type"]="application/json;charset=UTF-8"
#     return resp






# @main.route('/upload', methods=['GET','POST'])
# def upload():
# 	if request.method == 'POST':
# 		f = request.files['file']
# 		basepath = os.path.dirname(__file__)
# 		upload_path = os.path.join(basepath, 'static\uploads',secure_filename(f.filename))
# 		f.save(upload_path)
# 		# return redirect(url_for('upload'))
# 	return render_template('upload.html')

# @main.route('/shutdown')
# def shutdown():
# 	if not current_app.testing:
# 		abort(404)

# 	shutdown = request.environ.get('werkzeug,server.shutdown')
# 	if not shutdown:
# 		abort(500)

# 	shutdown()
# 	return u'正在关闭服务器端进程......'
	# @app.template_filter('md')
	# def markdown_to_html(txt):
	# 	from markdown import markdown
	# 	return markdown(txt)

	# def read_md(filename):
	# 	with open(filename) as md_file:
	# 		content = reduce(lambda x, y: x + y, md_file.readlines())
	# 		return content.decode('utf-8')

	# @app.context_processor
	# def inject_methods():
	# 	return dict(read_md = read_md)