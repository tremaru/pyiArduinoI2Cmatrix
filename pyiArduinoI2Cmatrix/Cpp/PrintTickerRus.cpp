// Данный пример выводит бегущую строку на Русском языке.        //
                                                                 //
#include "../iarduino_I2C_Matrix_8x8.h"                             // Подключаем библиотеку для работы с LED матрицей 8x8.
iarduino_I2C_Matrix_8x8 disp(0x0c);                              // Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                                                 //
int main(int argc, char** argv){                                                    //
    delay(500);                                                  // Ждём завершение переходных процессов связанных с подачей питания.
    disp = 9; //int(argv[1]);
    disp.begin();                                                // Инициируем работу с LED матрицей 8x8.
    disp.codingDetect("п");                                      // Выполняем автоопределение кодировки сценария.
    disp.print("Unknown coding");                                // Загружаем текст "Unknown coding" для бегущей строки.
    if (disp.getCoding() == X8_TXT_CP866){                       // Если данный сценарий использует кодировку CP866, то ...
        disp.print("Данный сценарий использует кодировку CP866");   // Меняем текст для бегущей строки.
    }                                                            //
    if (disp.getCoding() == X8_TXT_UTF8){                        // Если данный сценарий использует кодировку UTF8, то ...
        disp.print("Данный сценарий использует кодировку UTF-8");   // Меняем текст для бегущей строки.
    }                                                            //
    if (disp.getCoding() == X8_TXT_WIN1251){                     // Если данный сценарий использует кодировку WIN1251, то ...
        disp.print("Данный сценарий использует кодировку WIN1251"); // Меняем текст для бегущей строки.
    }                                                            //
//  Запускаем бегущую строку:                                    // До этого мы только загрузили текст бегущей строки, но не выводили её!
//    disp.autoScroll(240);                                        // Вывести (прокрутить) бегущую строку однократно со скоростью 240. Скорость указывается от 0 (стоп), до 255 (макс).
  disp.autoScroll(240, 1000);                                  // А так, та же бегущая строка будет постоянно прокручиваться, выдерживая паузу между прокрутками в 1 секунду.
}                                                                //
