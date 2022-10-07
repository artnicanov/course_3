from flask import Flask, render_template, request
import utils

app = Flask(__name__)

# вьюшка ленты со всем постами
@app.route('/')
def main_page():
	posts_data = utils.get_posts_all() # в эту переменную передаем все посты
	comments_data = utils.get_comments_all()# в эту переменную передаем все комментарии
	return render_template('index.html', posts=posts_data, comments=comments_data)

# вьюшка для одного поста
@app.route('/posts/<postid>')
def post_page(postid):
	post_data = utils.get_post_by_pk(postid)
	return render_template('post.html', post=post_data)

app.run()