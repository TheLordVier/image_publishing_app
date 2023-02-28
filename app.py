# Импортируем фреймворк Flask и его функции
from flask import Flask, render_template, jsonify, request
# Импортируем logger
import logger

# Импортируем функции из utils.py, которые будем использовать
from utils import *
# Импортируем конфигурацию из файла config.py
from config import Config
from db import db

# Создаём логгер для дальнейшей работы с ним
log = logger.get_logger("api")


# Инициализируем приложение
# app = Flask(__name__)
# app.config.from_object(config)
# db.init_app(app)

def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    return app


app: Flask = create_app(Config)


@app.route("/")
def page_main():
    """Главная страница со всеми постами"""
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:pk>")
def page_post(pk):
    """Страница с постом по его идентификатору"""
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search/")
def page_search_post():
    """" Страница с выводом постов по ключевому слову"""
    word = request.args.get("s", "").lower()
    posts = search_for_posts(query=word)
    return render_template("search.html", posts=posts)


@app.route("/users/<user_name>")
def page_post_by_user_name(user_name):
    """Страница с выводом постов по пользователю"""
    posts = get_posts_by_user(user_name=user_name)
    return render_template("user-feed.html", posts=posts)


@app.route("/api/posts/")
def api_main():
    """
    Представление, которое обрабатывает запрос GET /api/posts
    и возвращает полный список постов в виде JSON-списка
    """
    posts = get_posts_all()
    log.info(f"api_main - > {len(posts)}")
    return jsonify(posts)


@app.route("/api/posts/<int:pk>")
def api_post(pk):
    """
    Представление, которое обрабатывает запрос GET /api/posts/<post_id>
    и возвращает один пост в виде JSON-словаря
    """
    post = get_post_by_pk(pk)
    log.info(f"api_post - > {pk}")
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(e):
    """
    Обработчик запросов при обращении к несуществующим
    страницам
    """
    return "Извините, но страница не найдена. Ошибка - 404"


@app.errorhandler(500)
def page_not_found(e):
    """
    Обработчик ошибок, возникающих на стороне сервера
    """
    return "Приносим наши извинения, произошла внутренняя ошибка сервера. Ошибка - 500"


@app.route("/test_db", methods=["GET"])
def db_page():
    result = db.session.execute(
       '''
       SELECT 1;
       '''
    ).scalar()
    return jsonify({'result': result})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0', port=8080)
