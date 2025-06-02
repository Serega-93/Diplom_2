import random


class DataCreatedUser:

    @staticmethod
    def generate_body():
        return {"email": f'qatest-{random.randint(1000, 9999)}@yandex.ru',
                "password": f'{random.randint(10000, 99999)}a',
                "name": f'serega{random.randint(100, 999)}'
                }
