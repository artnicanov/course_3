from flask import Flask, render_template, request
import utils

app = Flask(__name__)

# вьюшка ленты со всем постами
@app.route('/')
def main_page():
	posts_data = utils.get_posts_all() # в эту переменную передаем все посты
	return render_template('index.html', posts=posts_data)

# вьюшка для одного поста
@app.route('/posts/<postid>')
def post_page(postid):
	postid = int(postid) # id поста обязательно привести к числу, иначе будет ошибка
	post_data = utils.get_post_by_pk(postid) # в эту переменную передаем конкретный пост по его идентификатору
	try:
		comments_data = utils.get_comments_by_post_id(postid)  # в эту переменную передаем все комментарии к выбранному посту
		comments_count = len(comments_data) # здесь колличество комментариев
	except ValueError:
		return "POST NOT FOUND" # покажем это сообщение если такого поста нет
	return render_template('post.html', post=post_data, comments=comments_data, comments_count=comments_count)

# вьюшка для поиска пока не работает приходится вручную прописывать ?s=
@app.route('/search/')
def search_page():
	search_query = request.args.get('s') # получаем значение из адресной строки через args
	posts_data = utils.search_for_posts(str(search_query)) # передаем функции, которая ищет слова, значение полученное строкой выше
	posts_count = len(posts_data)
	return render_template('search.html', query=search_query, posts=posts_data, posts_count=posts_count)

# вьюшка с выводом постов конкретного пользователя
@app.route('/users/<username>')
def user_posts(username):
	posts_data = utils.get_posts_by_user(username)
	return render_template('user-feed.html', posts=posts_data)


app.run()