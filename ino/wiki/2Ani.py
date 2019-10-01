# Данный пример заливает и стирает весь дисплей.                #
                                                                 #
from pyiArduinoI2Cmatrix import *       # Подключаем библиотеку для работы с LED матрицей 8x8.
from time import sleep                  #
disp = pyiArduinoI2Cmatrix(0x09)        # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                        #
while True:                             #
    disp.fillScr(X8_RIPPLES)            # Заливаем экран рябью (светодиоды включаются  хаотично и с задержками).
    sleep(1)                            #
    disp.clrScr (X8_RIPPLES)            # Чистим   экран рябью (светодиоды выключаются хаотично и с задержками).
    sleep(1)                            #
    disp.fillScr(X8_DOWN)               # Заливаем экран сверху вниз (светодиоды включаются  построчно сверху вниз).
    sleep(1)                            #
    disp.clrScr (X8_DOWN)               # Чистим   экран сверху вниз (светодиоды выключаются построчно сверху вниз).
    sleep(1)                            #
    disp.fillScr(X8_TOP)                # Заливаем экран снизу вверх (светодиоды включаются  построчно снизу вверх).
    sleep(1)                            #
    disp.clrScr (X8_TOP)                #    