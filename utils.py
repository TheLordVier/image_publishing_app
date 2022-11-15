# Импортируем стандартный модуль JSON
import json


def get_posts_all():
    """
    Чтение данных из JSON файла с постами
    """
    with open('data/posts.json', 'r', encoding='utf=8') as file:
        data = json.load(file)
        return data


def get_comments_all():
    """
    Чтение данных из JSON файла с комментариями к постам
    """
    with open('data/comments.json', 'r', encoding='utf=8') as file:
        data = json.load(file)
        return data


def get_posts_by_user(user_name):
    """
    Функция, которая возвращает посты определённого пользователя
    """
    posts = get_posts_all()
    try:
        result = []
        for post in posts:
            if user_name.lower() == post['poster_name'].lower():
                result.append(post)
    except ValueError:
        return "Ошибка значения"
    else:
        return result


def get_comments_by_post_id(post_id):
    """
    Функция, которая возвращает комментарии определённого поста
    """
    comments = get_comments_all()
    try:
        result = []
        for comment in comments:
            if int(post_id) == comment['post_id']:
                result.append(comment)
    except ValueError:
        return "Ошибка значения"
    else:
        return result


def search_for_posts(query):
    """
    Функция, которая возвращает список постов по ключевому слову (подстроке)
    """
    posts = get_posts_all()
    result = []
    for post in posts:
        if query.lower() in post['content'].lower():
            result.append(post)
    return result


def get_post_by_pk(pk):
    """
     Функция, которая возвращает один пост по его идентификатору
     """
    posts = get_posts_all()
    for post in posts:
        if pk == post['pk']:
            return post
    return None
