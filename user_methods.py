import allure
import requests
from data import Url


class UserMethods:

    @staticmethod
    @allure.title('Создание пользователя')
    def created_user(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATED_USER}', json=body)

    @staticmethod
    @allure.title('Авторизация пользователем')
    def login_user(body):
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', json=body)

    @staticmethod
    @allure.title('Обновление данных пользователя')
    def update_user_data(body, token):
        header = { "Authorization": token }
        return requests.patch(f'{Url.BASE_URL}{Url.UPDATE_USER}', headers=header, json=body)

    @staticmethod
    @allure.title('Удаление пользователя')
    def delete_user(token):
        header = {"Authorization": token}
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER}', headers=header)
