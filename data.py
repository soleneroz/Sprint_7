class DataUser:
    my_login = 'bravado'
    my_courier_data = {'login': 'bravado', 'password': '123456', 'firstName': 'nick'}
    my_courier_with_wrong_password = {'login': 'bravado', 'password': '12345678'}


class OrderData:
    order_data_with_grey_color = {
        'firstName': 'Тайлер',
        'lastName': 'Дёрден',
        'address': 'Мыльная, 23',
        'metroStation': 3,
        'phone': '+79999999999',
        'rentTime': 2,
        'deliveryDate': '2025-02-11',
        'comment': 'Я полная невозмутимость Джека',
        'color': [
            'GREY'
        ]
    }

    order_data_with_black_color = {
        'firstName': 'Аурелиано',
        'lastName': 'Буэндиа',
        'address': 'Макондо',
        'metroStation': 5,
        'phone': '+79666666666',
        'rentTime': 5,
        'deliveryDate': '2025-02-12',
        'comment': 'И родился ребёнок, который был сам себе дедушкой',
        'color': [
            'BLACK'
        ]
    }

    order_data_with_two_colors = {
        'firstName': 'Мистер',
        'lastName': 'Розовый',
        'address': 'Big Kahuna Burger',
        'metroStation': 11,
        'phone': '+79998887766',
        'rentTime': 6,
        'deliveryDate': '2025-02-13',
        'comment': 'Чаевых не будет',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_without_colors = {
        'firstName': 'Адам',
        'lastName': 'Кешер',
        'address': 'Малхолланд Драйв',
        'metroStation': 18,
        'phone': '+79876543211',
        'rentTime': 9,
        'deliveryDate': '2025-02-14',
        'comment': 'Это мой фильм',
        'color': []
    }