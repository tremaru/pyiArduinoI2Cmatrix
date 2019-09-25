# distutils: language = c++
# cython: language_level = 3
#encoding = utf-8
DEF_CHIP_ID_FLASH   =   0x3C
DEF_CHIP_ID_METRO   =   0xC3
DEF_MODEL_8X8       =   0x08
#Адреса регистров модуля:   
REG_FLAGS_0         =   0x00
REG_BITS_0          =   0x01
REG_FLAGS_1         =   0x02
REG_BITS_1          =   0x03
REG_MODEL           =   0x04
REG_VERSION         =   0x05
REG_ADDRESS         =   0x06
REG_CHIP_ID         =   0x07
REG_FREQUENCY       =   0x08
REG_BRIGHTNESS      =   0x09
REG_8X8_DATA        =   0x10
REG_8X8_SAVE_AS     =   0x19
REG_8X8_SYMBOL_INPUT=   0x1A
REG_8X8_TEXT_INPUT  =   0x1B
REG_8X8_STEP_LEN    =   0x1C
REG_8X8_TIME_STEP   =   0x1E
REG_8X8_TIME_PAUSE  =   0x1F
REG_8X8_TIME_START  =   0x20
REG_8X8_TIME_STOP   =   0x21
REG_8X8_FUNCTIONS   =   0x22
#Функций анимации ряби:     
X8_EMPTY_RIPPLES    =   100 
X8_RIPPLES          =   101 
X8_FILLED_RIPPLES   =   102 
#Функций анимации сверху-вниз
X8_EMPTY_DOWN       =   104 
X8_DOWN             =   105 
X8_FILLED_DOWN      =   106 
#Функций анимации снизу-вверх
X8_EMPTY_TOP        =   108 
X8_TOP              =   109 
X8_FILLED_TOP       =   110 
#Виды памяти для хранения изо
X8_IMG_RAM          =   0   
X8_IMG_ROM          =   1   
#Виды поддерживаемых кодирово
X8_TXT_CP866        =   0   
X8_TXT_UTF8         =   1   
X8_TXT_WIN1251      =   2   

from iarduino_I2C_Matrix_8x8 cimport iarduino_I2C_Matrix_8x8

cdef class pyiArduinoI2Cmatrix:
    cdef iarduino_I2C_Matrix_8x8 c_matrix

    def __cinit__(self, address=None):
        if address is not None:
            self.c_matrix = iarduino_I2C_Matrix_8x8(address)
            self.c_matrix.begin()
        else:
            self.c_matrix = iarduino_I2C_Matrix_8x8()
            self.c_matrix.begin()

    def begin(self):
        return self.c_matrix.begin()

    def changeAddress(self, unsigned char newAddr):
        return self.c_matrix.changeAddress(newAddr)

    def reset(self):
        return self.c_matrix.reset()

    def getAddress(self):
        return self.c_matrix.getAddress()

    def getVersion(self):
        return self.c_matrix.getVersion()

    def getCoding(self):
        return self.c_matrix.getCoding()

    def setCoding(self, name):
        self.c_matrix.setCoding(name)

    def codingDetect(self, letter_p):
        if isinstance(letter_p, str) and len(letter_p) is 1:
            self.c_matrix.codingDetect(str.encode(letter_p))
        else:
            print("ошибка: функция принимет только букву 'п'")

    def clrScr(self, ani = None):
        if ani is not None:
            self.c_matrix.clrScr(ani)
        else:
            self.c_matrix.clrScr(0)

    def fillScr(self, ani = None):
        if ani is not None:
            self.c_matrix.fillScr(ani)
        else:
            self.c_matrix.fillScr(0)

    def invScr(self):
        self.c_matrix.invScr()

    def drawImage(self, array):
        if isinstance(array, list):
            b = bytearray(array)
            self.c_matrix.drawImage(b, 0, 0)
        else:
            print("функция поддерживает только списки")

    def getImage(self):
        image = []
        b = bytearray(image)
        self.c_matrix.getImage(b)
        return b
