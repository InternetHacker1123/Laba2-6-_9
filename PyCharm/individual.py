#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

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

            
            case 'choose':
                inp = input("Введите номер поезда: ")
                for d in sp:
                    if inp in d.values():
                        print(d)
                    else: 
                        print('Поезда с таким номером нет')
            
            case 'list':
                line = '+-{}-+-{}-+-{}-+-{}-+'.format(
               '-' * 4,
               '-' * 30,
               '-' * 20,
               '-' * 20
                )
                print(line)
                print(
               '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                   "№",
                   "Пункт назначения",
                   "Номер поезда",
                   "Время отправления"
                )
                )
                print(line)
                for idx, train in enumerate(sp, 1):
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                            idx,
                            train.get('Пункт назначения ', ''),
                            train.get('Номер поезда: ', ''),
                            train.get('Время отправления:', 0)
                   )
               )
                print(line)
            case 'exit':
                break

            case 'help':
                print("Список команд:\n")
                print("add - добавить поезд;")
                print("list - вывести список поездов;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

