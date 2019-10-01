# Данный пример выводит символы на Русском языке. 
                                        #
from pyiArduinoI2Cmatrix import *       # Подключаем библиотеку для работы с LED матрицей 8x8.
from time import sleep                  # Импортируем функцию ожидания
disp = pyiArduinoI2Cmatrix(0x09)        # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                        #
disp.setCoding(X8_TXT_UTF8)             # Устанавливаем кодировку UTF-8
                                        #
while True:                             #
    disp.print("П")                     # Выводим символ 'П'.
    sleep(.3)                           #
    disp.print("р")                     # Выводим символ 'р'.
    sleep(.3)                           #
    disp.print("и")                     # Выводим символ 'и'.
    sleep(.3)                           #
    disp.print("в")                     # Выводим символ 'в'.
    sleep(.3)                           #
    disp.print("е")                     # Выводим символ 'е'.
    sleep(.3)                           #
    disp.print("т")                     # Выводим символ 'т'
    sleep(.3)                           #
    disp.print(" ")                     # Выводим символ пробела.
    sleep(.5)                           #