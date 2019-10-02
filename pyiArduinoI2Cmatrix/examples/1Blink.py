# Данный пример заливает и стирает весь дисплей.
                                        #
from pyiArduinoI2Cmatrix import *       # Подключаем библиотеку (модуль python) для работы с LED матрицей 8x8.
from time import sleep                  # Импортируем функцию ожидания
disp = pyiArduinoI2Cmatrix(0x09)        # Объявляем объект disp для работы 
                                        # с LED матрицей 8x8, указывая её адрес на шине I2C.
try:                                    # Входим в блок исключений
    while True:                         # Входим в бесконечный цикл
         disp.fillScr()                 # Заливаем экран (включаем  все светодиоды).
         sleep(1)                       #
         disp.clrScr()                  # Чистим экран (выключаем все светодиоды).
         sleep(1)                       # 
except:                                 # Если поднято исключение (например, 
                                        # выполнение сценария прервано с клавиатуры) 
    disp.reset()                        # Сбрасываем все параметры матрицы