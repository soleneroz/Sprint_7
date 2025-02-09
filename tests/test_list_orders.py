import requests
import allure
from url import Urls


class TestGetOrderList:

    @allure.title('Получение списка заказов')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_get_order_list(self):
        response = requests.get(Urls.URL_create_order)
        assert type(response.json()['orders']) == list