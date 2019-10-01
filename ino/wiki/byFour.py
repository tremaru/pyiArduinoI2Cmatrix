# Данный пример выводит изображения myImage_1 и myImage_2.      #
                                                                 # Создаём изображение "смайлик".
myImage_1 = [ 0b00000000,                                #                        
              0b00000000, #* Посмотрите, изображение */  #                           
              0b11111111, #* можно увидеть прямо в   */  #                          
              0b11111100, #* коде!!!                 */  #                            
              0b11111101,                                #                          
              0b10000000,                                #                          
              0b10000000,                                #                           
              0b10000000 ]                               #                        
                                                                 # Создаём изображение "телевизор".
myImage_2 = [ 0b00000000,                                #                            
              0b00000000,                                #                            
              0b11111111,                                #                             
              0b00111111,                                #                      
              0b10111111,                                #                           
              0b00000001,                                #                           
              0b00000001,                                #                           
              0b00000001 ]                               #                      

myImage_3 = [ 0b10000000,                                #                            
              0b10000000,                                #                            
              0b10000000,                                #                             
              0b11011011,                                #                      
              0b11000011,                                #                           
              0b11111111,                                #                           
              0b00000000,                                #                           
              0b00000000 ]                               #                      

myImage_4 = [ 0b00000001,                                #                            
              0b00000001,                                #                            
              0b00000001,                                #                             
              0b11011011,                                #                      
              0b11000011,                                #                           
              0b11111111,                                #                           
              0b00000000,                                #                           
              0b00000000 ]                               #                      
from pyiArduinoI2Cmatrix import *                               # Подключаем библиотеку для работы с LED матрицей 8x8.
import sys
from time import sleep
disp = [
        pyiArduinoI2Cmatrix(10),
        pyiArduinoI2Cmatrix(11),
        pyiArduinoI2Cmatrix(12),
        pyiArduinoI2Cmatrix(13)
       ]
for i in disp:
    i.begin()
    sleep(.5)
    i.fillScr()
    sleep(.5)
    i.clrScr()
#disp = pyiArduinoI2Cmatrix(int(sys.argv[1]))                     # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                                                 #
                                                                 #
#while True:                                                      #
disp[0].drawImage(myImage_1)
disp[1].drawImage(myImage_2)
disp[2].drawImage(myImage_3)
disp[3].drawImage(myImage_4)

