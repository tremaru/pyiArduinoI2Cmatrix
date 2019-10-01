# Данный пример выводит цифры 0-9 каждую секунду.               #
                                        #
from pyiArduinoI2Cmatrix import *       # Подключаем библиотеку для работы с LED матрицей 8x8.
from time import sleep                  # 
disp = pyiArduinoI2Cmatrix(0x09)        # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                        #
while True:                             # Входим в бесконечный цикл
    for i in range(10):                 # 
        disp.print(i)                   # Выводим цифру на матрицу 
        sleep(1)                        # Ждём секунду
