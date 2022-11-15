# Импортируем данные по API из app.py для их тестирования и фикстуры из модуля pytest
from app import app
from pytest import fixture


# Создаём фикстуры для их использования в тестах
@fixture()
def client():
    return app.test_client()


@fixture()
def keys_should_be_post():
    return {"poster_name", "poster_avatar", "pic", "content", "pk", "likes_count", "views_count", "pk"}


def test_api_main(client):
    """Тест на API, тестирование эндпоинта GET /api/posts"""
    response = client.get("/api/posts/")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_api_post(client, keys_should_be_post):
    """Тест на API, тестирование эндпоинта GET /api/posts/<post_id>"""
    response = client.get("/api/posts/8")
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == keys_should_be_post
