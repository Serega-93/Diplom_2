class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATED_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    UPDATE_USER = '/api/auth/user'
    CREATED_ORDER = '/api/orders'
    GET_ORDERS_USER = '/api/orders'
    DELETE_USER = '/api/auth/user'

class Ingredients:

    @staticmethod
    def ingredients_body():
        bun = '61c0c5a71d1f82001bdaaa6c'
        main = '61c0c5a71d1f82001bdaaa6e'
        souse = '61c0c5a71d1f82001bdaaa73'
        return { 'ingredients': [bun, main, souse]}
