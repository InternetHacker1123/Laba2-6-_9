#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        '1a': 11,
        '1б': 12,
        '2б': 13,
        '6а': 14,
        '7в': 15,
        '8в': 16,
        '9в': 17,
        '10в': 18,
        '11в': 19,
    }

    # Меняем кол-во учащихся
    school['11в'] = 1
    
    # Добавляем новый класс
    school['5а'] = 23

    # Удаляем один класс
    del school['10в']

    # Сумма учеников
    vse_studenty = sum(school.values())

    print(f"Общее количество учащихся в школе: {vse_studenty}")
    