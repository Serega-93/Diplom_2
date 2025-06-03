import allure
from data import Ingredients
from order_methods import OrderMethods


class TestCreatingOrder:

    @allure.title('Успешное создание заказа')
    def test_successful_creating_order(self, creating_user):
        token, user_body = creating_user
        order_body = Ingredients.ingredients_body()
        response = OrderMethods.created_order(order_body, token )
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создания заказа без авторизации')
    def test_error_creating_order_without_authorization(self, creating_user):
        token = ''
        order_body = Ingredients.ingredients_body()
        response = OrderMethods.created_order(order_body, token)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_creating_order_without_ingredients(self, creating_user):
        token, user_body = creating_user
        order_body = { 'ingredients': []}
        response = OrderMethods.created_order(order_body, token)
        actual_body = response.json()
        expected_body = {"success": False,"message": "Ingredient ids must be provided"}

        assert response.status_code == 400
        assert actual_body == expected_body

    @allure.title('Создание заказа с невалидным хешом ингредиента')
    def test_creating_order_without_ingredients(self, creating_user):
        token, user_body = creating_user
        order_body = {'ingredients': ['61c0c5a71d1f82001bdaaa6c1']}
        response = OrderMethods.created_order(order_body, token)

        assert response.status_code == 500
