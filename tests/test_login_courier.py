import requests
import allure
import pytest
from data import DataUser
from url import Urls
from random_data_user import generate_random_string


class TestLoginCourier:

    @allure.title('Успешная авторизация с существующими данными')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_courier_login(self):
        response = requests.post(Urls.URL_login_courier, data=DataUser.my_courier_data)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Неуспешная авторизация при вводе невалидных данных')
    @allure.description('Проверка статус-кода и тела ответа')
    @pytest.mark.parametrize('random_fields', [
        {'login': generate_random_string(10), 'password': generate_random_string(10)},
        DataUser.my_courier_with_wrong_password
    ])
    def test_courier_login_with_random_fields_data(self, random_fields):
        response = requests.post(Urls.URL_login_courier, data=random_fields)
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Неуспешная авторизация при вводе не всех обязательных полей')
    @allure.description('Проверка статус-кода и тела ответа')
    @pytest.mark.parametrize('empty_fields', [
        {'login': '', 'password': generate_random_string(10)},
        {'login': DataUser.my_login, 'password': ''},
        {'login': '', 'password': ''}
    ])
    def test_courier_login_with_empty_fields(self, empty_fields):
        response = requests.post(Urls.URL_login_courier, data=empty_fields)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}