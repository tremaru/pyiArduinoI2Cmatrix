# Данный пример постоянно поворачивает дисплей на 90°.          #
                                                                 # Создаём изображение "капля".
image = [0b00111100,                               #                         
                       0b01111110, #* Посмотрите, изображение */ #                       
                       0b11001111, #* можно увидеть прямо в   */ #                       
                       0b10000110, #* коде!!!                 */ #                          
                       0b10000000,                               #                            
                       0b10000000,                               #                            
                       0b01000000,                               #                            
                       0b00100000]                               #                            
image2 = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
import sys
from pyiArduinoI2Cmatrix import *
from time import sleep
disp = pyiArduinoI2Cmatrix(int(sys.argv[1]))
#disp = pyiArduinoI2Cmatrix(0x0c)
#iarduino_I2C_Matrix_8x8 disp(0x09)                               # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                                                 #
disp.bright(255)
try:
    while True:
        i = 0
        disp.drawImage(image, 102)                                        # Выводим на дисплей изображение массива image.
        while i < 10:                                                      #
            disp.angle(0)  , sleep(.1)                                  # Поворачиваем дисплей на 0°   и ждём 0.1 секунду.
            disp.angle(90) , sleep(.1)                                  # Поворачиваем дисплей на 90°  и ждём 0.1 секунду.
            disp.angle(180), sleep(.1)                                  # Поворачиваем дисплей на 180° и ждём 0.1 секунду.
            disp.angle(270), sleep(.1)                                  # Поворачиваем дисплей на 270° и ждём 0.1 секунду.
            i += 1
        disp.drawImage(image2, 100)                                        # Выводим на дисплей изображение массива image.
        sleep(1)
except KeyboardInterrupt:
    disp.angle(0)
