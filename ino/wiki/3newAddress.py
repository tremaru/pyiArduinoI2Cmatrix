#encoding=utf-8
# Данный пример меняет адрес модуля на указанный в переменной «newAddress».
from pyiArduinoI2Cmatrix import *               # Подключаем библиотеку для работы с реле и силовыми ключами.
                                                #
newAddress = 9                               # Назначаемый модулю новый адрес (0x07 < адрес < 0x7F).
                                                #
disp = pyiArduinoI2Cmatrix()                    # Создаём объект relay для работы 
print(newAddress)                               # Если на шине несколько светодиодных матриц,
                                                # то нужно указать адрес той матрицы
                                                # которой требуется работать.
disp.changeAddress(newAddress)                  # Меняем адресс на значение из переменной newAddress
