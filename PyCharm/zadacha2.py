#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dictionary = {
        1: 'Я',
        2: 'Люблю',
        3: 'Играть',
        4: 'В',
        5: 'Доту'
    }
     
    # Создаем словарь с ключами наоборот
    result = {value: key for key, value in dictionary.items()}

    # вывод результата
    print(f"Обратный словарь: {result}")