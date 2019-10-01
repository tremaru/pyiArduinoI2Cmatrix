# Данный пример выводит символы.                                #
                                                                 #
from pyiArduinoI2Cmatrix import *       # Подключаем библиотеку для работы с LED матрицей 8x8.
from time import sleep                  # Импортируем функцию ожидания
disp = pyiArduinoI2Cmatrix(0x09)        # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                        #
while True:                             #
    disp.print('i')                     # Выводим символ
    sleep(.300)                         #
    disp.print('A')                     # Выводим символ
    sleep(.300)                         #
    disp.print('r')                     # Выводим символ
    sleep(.300)                         #
    disp.print('d')                     # Выводим символ
    sleep(.300)                         #
    disp.print('u')                     # Выводим символ
    sleep(.300)                         #
    disp.print('i')                     # Выводим символ
    sleep(.300)                         #
    disp.print('n')                     # Выводим символ
    sleep(.300)                         #
    disp.print('o')                     # Выводим символ
    sleep(.300)                         #
    disp.print(' ')                     # Выводим символ
    sleep(.500)                         #
