import allure
from user_methods import UserMethods


class TestUpdateUser:

    @allure.title('Изменение поле email пользователя')
    def test_update_data_email_user(self, creating_user):
        token, user_body = creating_user
        new_email = f'q{user_body["email"]}'
        new_name = f'q{user_body["name"]}'
        update_body = {"email": new_email, "name": new_name}
        response = UserMethods.update_user_data(update_body, token)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["user"]["email"] == new_email
        assert actual_body["user"]["name"] == new_name

    @allure.title('Ошибка при изменении данных без авторизации')
    def test_update_data_without_authorization_user(self, creating_user):
        token, user_body = creating_user
        update_body = {"email": f'q{user_body["email"]}', "name": f'q{user_body["name"]}'}
        token = ''
        response = UserMethods.update_user_data(update_body, token)
        actual_body = response.json()
        expected_body = {"success": False,"message": "You should be authorised"}

        assert response.status_code == 401
        assert actual_body == expected_body
