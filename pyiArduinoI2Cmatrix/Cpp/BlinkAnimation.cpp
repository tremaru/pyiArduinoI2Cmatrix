// Данный пример заливает и стирает весь дисплей с анимацией.    //
                                                                 //
#include "../iarduino_I2C_Matrix_8x8.h"                             // Подключаем библиотеку для работы с LED матрицей 8x8.
iarduino_I2C_Matrix_8x8 disp(0x0c);                              // Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                                                 //
void loop(void);

int main(){                                                    //
    delay(500);                                                  // Ждём завершение переходных процессов связанных с подачей питания.
    disp.begin();                                                // Инициируем работу с LED матрицей 8x8.
    for(;;) {
        loop();
    }
}                                                                //
                                                                 //
void loop(){                                                     //
    disp.fillScr(X8_RIPPLES); delay(1000);                       // Заливаем экран рябью.
    disp.clrScr (X8_RIPPLES); delay(1000);                       // Чистим   экран рябью.
    disp.fillScr(X8_DOWN   ); delay(1000);                       // Заливаем экран сверху-вниз.
    disp.clrScr (X8_DOWN   ); delay(1000);                       // Чистим   экран сверху-вниз.
    disp.fillScr(X8_TOP    ); delay(1000);                       // Заливаем экран снизу-вверх.
    disp.clrScr (X8_TOP    ); delay(1000);                       // Чистим   экран снизу-вверх.
}                                                                //
