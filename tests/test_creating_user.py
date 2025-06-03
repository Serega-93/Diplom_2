import allure
import pytest
from generator import DataCreatedUser
from user_methods import UserMethods


class TestCreatingUser:

    @allure.title('Создание уникального пользователя')
    def test_creating_unique_user(self, delete_user, request):
        user_body = DataCreatedUser.generate_body()
        response = UserMethods.created_user(user_body)
        token = response.json()["accessToken"]
        request.node.funcargs["delete_user"] = token
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создание уже зарегистрированного пользователя')
    def test_creating_registered_user(self, creating_user):
        token, user_body = creating_user
        response = UserMethods.created_user(user_body)
        expected_body = {"success": False,"message": "User already exists"}
        actual_body = response.json()

        assert response.status_code == 403
        assert actual_body == expected_body

    @pytest.mark.parametrize('email, password, name', [['', 555555, 'serega'],['qatest-11@yandex.ru', '', 'serega'],
                                                      ['qatest-11@yandex.ru', 555555, '']])
    @allure.title('Создание пользователя без заполненного поля')
    def test_creating_user_without_filled_field(self, email, password, name):
        user_body = {"email": email, "password": password, "name": name}
        response = UserMethods.created_user(user_body)
        expected_body ={"success": False, "message": "Email, password and name are required fields"}
        actual_body = response.json()

        assert response.status_code == 403
        assert actual_body == expected_body
