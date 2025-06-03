import allure
from order_methods import OrderMethods


class TestGetOrderUser:

    @allure.title('Получение заказов авторизованным пользователем')
    def test_receiving_orders_authorized_user(self, creating_user_and_order):
        token = creating_user_and_order
        response = OrderMethods.get_orders_user(token)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Получение заказов неавторизованным пользователем')
    def test_receiving_orders_authorized_user(self, creating_user_and_order):
        token = ''
        response = OrderMethods.get_orders_user(token)
        actual_body = response.json()
        expected_body = {"success": False,"message": "You should be authorised"}

        assert response.status_code == 401
        assert actual_body == expected_body
