from main import app

def test_first_api_endpoint():
	keys = {
		"poster_name",
		"poster_avatar",
		"pic",
		"content",
		"views_count",
		"likes_count",
		"pk"
	}
	response = app.test_client().get('/api/posts')
	keys_set = set(response.json[0].keys())  # получаем только ключи из response. При использовании values получим только значения
	assert type(response.json) == list, "not list"  # проверка что возвращается список
	assert keys == keys_set, "keys do not match"  # проверка что у элементов есть нужные ключи

def test_second_api_endpoint():
	keys = {
		"poster_name",
		"poster_avatar",
		"pic",
		"content",
		"views_count",
		"likes_count",
		"pk"
	}
	response = app.test_client().get('/api/posts/1')
	keys_set = set(response.json.keys())  # получаем только ключи из response.
	assert type(response.json) == dict, "not dict"  # проверка что возвращается словарь
	assert keys == keys_set, "keys do not match"  # проверка что у элемента есть нужные ключи
