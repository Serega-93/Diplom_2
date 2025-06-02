import allure
import requests
from data import Url


class OrderMethods:

    @staticmethod
    @allure.title('Создание заказа')
    def created_order(body, token):
        return requests.post(f'{Url.BASE_URL}{Url.CREATED_ORDER}', auth=token, json=body)

    @staticmethod
    @allure.title('Получение заказов пользователя')
    def get_orders_user(token):
        return requests.get(f'{Url.BASE_URL}{Url.GET_ORDERS_USER}', auth=token)