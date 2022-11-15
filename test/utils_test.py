# Импортируем функции из utils.py для их тестирования юнит-тестами и стандартный модуль pytest
from utils import *
import pytest

# Задаем, какие ключи ожидаем получать из файлов posts.json и comments.json
keys_should_be_post = {"poster_name", "poster_avatar", "pic", "content", "pk", "likes_count", "views_count", "pk"}
keys_should_be_comment = {"post_id", "commenter_name", "comment", "pk"}


def test_get_posts_all():
    """ Проверяем, верный ли список кандидатов возвращается """
    posts = get_posts_all()
    assert type(posts) == list, "возвращается не список"
    assert len(posts) > 0, "возвращается пустой список"
    assert set(posts[0].keys()) == keys_should_be_post, "неверный список ключей"


def test_get_comments_all():
    """ Проверяем, верный ли список комментариев к постам возвращается """
    comments = get_comments_all()
    assert type(comments) == list, "возвращается не список"
    assert len(comments) > 0, "возвращается пустой список"
    assert set(comments[0].keys()) == keys_should_be_comment, "неверный список ключей"


def test_get_posts_by_user():
    """ Проверяем получение постов определённого пользователя"""
    post = get_posts_by_user(user_name="leo")
    assert type(post) == list, "возвращается не список"


def test_comments_by_post_id():
    """ Проверяем получение комментариев определённого поста"""
    comment = get_comments_by_post_id(post_id=1)
    assert type(comment) == list, "возвращается не список"


def test_search_for_posts():
    """ Проверяем получение списка постов по ключевому слову"""
    post = search_for_posts(query="Квадратная")
    assert type(post) == list, "возвращается не список"


def test_get_post_by_pk():
    """ Проверяем получение поста по его идентификатору"""
    post = get_post_by_pk(pk=1)
    assert type(post) == dict, "возвращается не словарь"
