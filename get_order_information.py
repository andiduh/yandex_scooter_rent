import configuration
import requests
import data

# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

#Получение трека заказа
response = post_new_order(data.user_body)
track = str(response.json()["track"])

# Запрос на получение заказа по треку заказа
def get_order_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + track)

#Проверка теста
def test_get_order_information():
    assert get_order_track().status_code == 200
