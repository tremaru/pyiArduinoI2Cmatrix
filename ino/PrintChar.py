# Данный пример выводит символы.                                #
                                                                 #
from pyiArduinoI2Cmatrix import *                               # Подключаем библиотеку для работы с LED матрицей 8x8.
import sys
from time import sleep
disp = pyiArduinoI2Cmatrix(int(sys.argv[1]))                     # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                                                 #
                                                                 #
while True:                                                      #
    disp.print('i')                                              # Выводим символ 'i'.
    sleep(.300)                                                   #
    disp.print('A')                                              # Выводим символ 'A'.
    sleep(.300)                                                   #
    disp.print('r')                                              # Выводим символ 'r'.
    sleep(.300)                                                   #
    disp.print('d')                                              # Выводим символ 'd'.
    sleep(.300)                                                   #
    disp.print('u')                                              # Выводим символ 'u'.
    sleep(.300)                                                   #
    disp.print('i')                                      # Выводим символ 'i', по коду этого символа.
    sleep(.300)                                                   #
    disp.print('n')                                              # Выводим символ 'n'.
    sleep(.300)                                                   #
    disp.print('o')                                              # Выводим символ 'o'.
    sleep(.300)                                                   #
    disp.print(' ')                                              # Выводим символ пробела.
    sleep(.500)                                                   #
