import allure

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
        element_expected_body = 'success'

        assert response.status_code == 200
        assert element_expected_body in actual_body
