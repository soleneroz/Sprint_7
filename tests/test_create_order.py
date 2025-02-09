import requests
import allure
import pytest
import json
from data import OrderData
from url import Urls


class TestCreateOrder:

    @allure.title('Проверка создания заказа при разных параметрах цвета')
    @allure.description('Проверка статус-кода и тела ответа')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_with_grey_color, OrderData.order_data_with_black_color,
        OrderData.order_data_with_two_colors, OrderData.order_data_without_colors
    ])
    def test_create_order_with_different_colors(self, order_data):
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.URL_create_order, data=order_data, headers=headers)
        assert response.status_code == 201 and 'track' in response.text