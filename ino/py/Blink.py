# Данный пример заливает и стирает весь дисплей.                #
                                                                 #
from pyiArduinoI2Cmatrix import *       # Подключаем библиотеку для работы с LED матрицей 8x8.
from time import sleep                  #
disp = pyiArduinoI2Cmatrix(0x09)        # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                        #
while True:                             #
    disp.fillScr()                      # Заливаем экран (включаем  все светодиоды).
    sleep(1)                            #
    disp.clrScr()                       # Чистим   экран (выключаем все светодиоды).
    sleep(1)                            # 
