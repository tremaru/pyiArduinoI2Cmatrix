# Данный пример выводит изображения myImage_1 и myImage_2.      #
                                                                 # Создаём изображение "смайлик".
myImage_1 = [ 0b00111100,                                #                        
                      0b01000010, #* Посмотрите, изображение */  #                           
                      0b10100101, #* можно увидеть прямо в   */  #                          
                      0b10000001, #* коде!!!                 */  #                            
                      0b10100101,                                #                          
                      0b10011001,                                #                          
                      0b01000010,                                #                           
                      0b00111100 ]                               #                        
                                                                 # Создаём изображение "телевизор".
myImage_2 = [ 0b01000100,                                #                            
                      0b00101000,                                #                            
                      0b00010000,                                #                             
                      0b11111111,                                #                      
                      0b10000011,                                #                           
                      0b10000011,                                #                           
                      0b10000011,                                #                           
                      0b11111111 ]                               #                      
from pyiArduinoI2Cmatrix import *                               # Подключаем библиотеку для работы с LED матрицей 8x8.
import sys
from time import sleep
disp = pyiArduinoI2Cmatrix(int(sys.argv[1]))                     # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
sleep(.5)
disp.begin()
#sleep(.5)
#disp.fillScr()
sleep(.5)
disp.clrScr()
                                                                 #
                                                                 #
while True:                                                      #
    disp.drawImage(myImage_1),  sleep(2)                       # Выводим на дисплей изображение массива myImage_1 и ждём пару секунд.
    disp.drawImage(myImage_2),  sleep(2)                       # Выводим на дисплей изображение массива myImage_2 и ждём пару секунд.
