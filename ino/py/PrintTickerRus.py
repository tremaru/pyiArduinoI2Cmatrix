# Данный пример выводит бегущую строку на Русском языке.        #
                                                                 #
from pyiArduinoI2Cmatrix import *                               # Подключаем библиотеку для работы с LED матрицей 8x8.
import sys
from time import sleep
disp = pyiArduinoI2Cmatrix(int(sys.argv[1]))                     # Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                                                 #
sleep(.5)                                                   # Ждём завершение переходных процессов связанных с подачей питания.
disp.begin()                                                 # Инициируем работу с LED матрицей 8x8.
sleep(.5)
disp.fillScr()
sleep(.5)
disp.clrScr()
disp.codingDetect("п")                                       # Выполняем автоопределение кодировки скетча.
disp.print("Unknown coding")                                 # Загружаем текст "Unknown coding" для бегущей строки.
if disp.getCoding() == X8_TXT_CP866:                       # Если данный скетч использует кодировку CP866, то ...
    disp.print("Данный сценарий использует кодировку CP866")    # Меняем текст для бегущей строки.
if disp.getCoding() == X8_TXT_UTF8:                        # Если данный скетч использует кодировку UTF8, то ...
    disp.print("Данный сценарий использует кодировку UTF-8")    # Меняем текст для бегущей строки.
if disp.getCoding() == X8_TXT_WIN1251:                     # Если данный скетч использует кодировку WIN1251, то ...
    disp.print("Данный сценарий использует кодировку WIN1251")  # Меняем текст для бегущей строки.
#  Запускаем бегущую строку:                                    # До этого мы только загрузили текст бегущей строки, но не выводили её!
disp.autoScroll(240)                                         # Вывести (прокрутить) бегущую строку однократно со скоростью 240. Скорость указывается от 0 (стоп), до 255 (макс).
#  disp.autoScroll(240, 1000)                                   # А так, та же бегущая строка будет постоянно прокручиваться, выдерживая паузу между прокрутками в 1 секунду.
