# Данный пример выводит символы с анимацией до и после слова.   #
                                        #
from pyiArduinoI2Cmatrix import *       # Подключаем библиотеку (модуль python) для работы с LED матрицей 8x8.
from time import sleep                  # Импортируем функцию ожидания
disp = pyiArduinoI2Cmatrix(0x09)        # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                        #
                                        #
while True:                             #
    disp.print('i', X8_FILLED_TOP)      # Выводим символ 'i', с анимацией появления снизу-вверх из закрашенного фона.
    sleep(.3)                           #
    disp.print('A')                     # Выводим символ 'A'.
    sleep(.3)                           #
    disp.print('r')                     # Выводим символ 'r'.
    sleep(.3)                           #
    disp.print('d')                     # Выводим символ 'd'.
    sleep(.3)                           #
    disp.print('u')                     # Выводим символ 'u'.
    sleep(.3)                           #
    disp.print('i')                     # Выводим символ 'i', по коду этого символа.
    sleep(.3)                           #
    disp.print('n')                     # Выводим символ 'n'.
    sleep(.3)                           #
    disp.print('o')                     # Выводим символ 'o'.
    sleep(.3)                           #
    disp.fillScr(X8_TOP)                # Заливаем дисплей снизу-вверх.
