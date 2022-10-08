import json

def get_posts_all():
	""" возвращает все посты из json файла """
	with open('data/posts.json', 'r', encoding='utf-8') as file:
		return json.load(file)

def get_comments_all():
	"""# возвращает все комментарии из json файла """
	with open('data/comments.json', 'r', encoding='utf-8') as file:
		return json.load(file)

def get_posts_by_user(user_name):
	""" возвращает посты определенного пользователя """
	user_posts = [] # в этот список будем собирать посты конкретного пользователя
	all_posts = get_posts_all() # обращаемся к функции, которая покажет все посты
	user_exists = False  # эта булева переменная нужна чтобы проверить наличие пользователя и вызвать ошибку если его нет
	for post in all_posts:
		if user_name == post['poster_name']:
			user_posts.append(post) # добавляем в список если комментарий есть
			user_exists = True
	if not user_exists:
		raise ValueError # Функция должна вызывать ошибку ValueError если такого пользователя нет
	return user_posts

def get_comments_by_post_id(post_id):
	"""возвращает комментарии определенного поста"""
	comments_list = [] # в этот список будем собирать комментарии к конкретному посту
	all_comments = get_comments_all() # обращаемся к функции, которая покажет все комментарии
	post_exists = False # эта булева переменная нужна чтобы проверить наличие поста и вызвать ошибку если его нет
	for comment in all_comments:
		if post_id == comment['post_id']:
			post_exists = True
			comments_list.append(comment) # добавляем в список если комментарий есть
	# if not post_exists:
	# 	raise ValueError # Функция должна вызывать ошибку ValueError если такого поста нет
	return comments_list

def search_for_posts(query):
	""" возвращает список постов по ключевому слову """
	posts_list_by_word = []
	all_posts = get_posts_all()  # обращаемся к функции, которая покажет все посты
	for post in all_posts:
		if query.lower() in post['content'].lower():
			posts_list_by_word.append(post)
	return posts_list_by_word

def get_post_by_pk(pk):
	""" возвращает один пост по его идентификатору """
	all_posts = get_posts_all()  # обращаемся к функции, которая покажет все посты
	for post in all_posts:
		if pk == post['pk']:
			return post

