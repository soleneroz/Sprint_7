import requests
import allure
import pytest
from data import DataUser
from url import Urls
from random_data_user import generate_random_string


class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_create_courier_with_valid_data(self):
        payload = {
            'login': generate_random_string(10),
            'password': generate_random_string(10),
            'firstName': generate_random_string(10)
        }
        response = requests.post(Urls.URL_create_courier, data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        response_login = requests.post(Urls.URL_login_courier, data=payload)
        assert requests.delete(f"{Urls.URL_delete_courier}/{response_login.json()['id']}")

    @allure.title('Создание курьера с уже существующим логином')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_create_courier_with_same_login(self):
        payload = {
            'login': DataUser.my_login,
            'password': generate_random_string(10),
            'firstName': generate_random_string(10)
        }
        response = requests.post(Urls.URL_create_courier, data=payload)
        assert response.status_code == 409
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Создание курьера без заполнения обязательных полей')
    @allure.description('Проверка статус-кода и тела ответа')
    @pytest.mark.parametrize('empty_fields', [
        {'login': '', 'password': generate_random_string(10), 'firstName': generate_random_string(10)},
        {'login': generate_random_string(10), 'password': '', 'firstName': generate_random_string(10)},
        {'login': '', 'password': '', 'firstName': generate_random_string(10)},
        {'login': generate_random_string(10), 'password': '', 'firstName': ''},
        {'login': '', 'password': '', 'firstName': ''}
    ])
    def test_create_courier_with_empty_fields(self, empty_fields):
        response = requests.post(Urls.URL_create_courier, data=empty_fields)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
