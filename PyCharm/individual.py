#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sp = []

    while True:
        inp = input(">>> ").lower()

        match inp:
            case 'add':
                punkt_naznachenia = input("Пункт назначения поезда: ")
                train_number = input("Номер поезда: ")
                time_otpravlenia = input("Время отправления: ")

                dictionary = {
                    'Пункт назначения ': punkt_naznachenia,
                    'Номер поезда: ': train_number,
                    'Время отправления:': time_otpravlenia
                }

                sp.append(dictionary)
                sp = sorted(sp, key=lambda x: x['Номер поезда: '])

            
            case inp.isdigit():
                for d in sp:
                    if inp in d.values():
                        print(d)
                    else: 
                        print('Поезда с таким номером нет')

