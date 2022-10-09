import logging
from flask import Flask, render_template, request, jsonify
import utils


logging.basicConfig(filename="api.log", filemode='w', level=logging.INFO)
api_logger = logging.getLogger()  # Создаем логгер
file_handler = logging.FileHandler("api.log")  # Cоздаем ему обработчик для записи в файл
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  # Создаем новое форматирование
api_logger.addHandler(file_handler)  # Добавляем обработчик к журналу
file_handler.setFormatter(formatter)  # Применяем форматирование к обработчику

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # задаем конфигурацию чтобы контент с кириллицей читался в любом браузере

# вьюшка ленты со всем постами
@app.route('/')
def main_page():
	posts_data = utils.get_posts_all()  # в эту переменную передаем все посты
	return render_template('index.html', posts=posts_data)


# вьюшка для одного поста
@app.route('/posts/<int:postid>')  # id поста обязательно привести к числу, иначе будет ошибка
def post_page(postid):
	post_data = utils.get_post_by_pk(postid)  # в эту переменную передаем конкретный пост по его идентификатору
	try:
		comments_data = utils.get_comments_by_post_id(postid)  # в эту переменную передаем все комментарии к выбранному посту
		comments_count = len(comments_data)  # здесь колличество комментариев
	except ValueError:
		return "POST NOT FOUND"  # покажем это сообщение если такого поста нет
	return render_template('post.html', post=post_data, comments=comments_data, comments_count=comments_count)


# вьюшка для поиска
@app.route('/search/')
def search_page():
	search_query = request.args.get('s')  # получаем значение из адресной строки через args
	posts_data = utils.search_for_posts(search_query)  # передаем функции, которая ищет слова, значение полученное строкой выше
	posts_count = len(posts_data)
	return render_template('search.html', posts=posts_data, posts_count=posts_count)


# вьюшка с выводом постов конкретного пользователя
@app.route('/users/<username>')
def user_posts(username):
	try:
		posts_data = utils.get_posts_by_user(username)
	except ValueError:
		return "USER NOT FOUND"  # покажем это сообщение если такого пользователя нет

	return render_template('user-feed.html', posts=posts_data)


# вьюшка для обработки запросов к несуществующим страницам
@app.errorhandler(404)
def no_such_page(error):
	return "NO SUCH PAGE"

# вьюшка для обработки ошибок на сервере
@app.errorhandler(500)
def server_mistake(error):
	return "SERVER MISTAKE"


# вьюшка для тестов API, возвращает полный список постов в виде JSON-списка
@app.route('/api/posts')
def first_api_endpoint():
	posts_data = utils.get_posts_all()  # в эту переменную передаем все посты
	logging.info("Запрос /api/posts")  # сообщение для логгера
	return jsonify(posts_data)

# вьюшка для тестов API, возвращает один пост в виде JSON-словаря
@app.route('/api/posts/<int:postid>')
def second_api_endpoint(postid):
	post_data = utils.get_post_by_pk(postid)  # в эту переменную передаем конкретный пост по его идентификатору
	logging.info(f"Запрос /api/posts/{postid}")  # сообщение для логгера
	return jsonify(post_data)

if __name__ == "__main__":
	app.run()
