from machine import SPI
from machine import Pin
from utime   import sleep_us 

import pcd8544_mod

spi = SPI(0, baudrate = 100000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck='P9_2', mosi='P9_0', miso='P9_1')
spi.init()

DC = Pin('P5_7')     #Data/Commands - specific for LCD Nokia 5110 display
DC.init(Pin.OUT, None, value=Pin.STATE_HIGH)

contrast = 0xff      #used for set contrast for LCD Nokia 5110 display; default value is 0xff

from A_Definitions import *
from D_Format_text_fix import *


#definire variabile folosita la impartirea valorior senzorilor in digiti:
mii     = None #folosita global
sute    = None #folosita global
zeci    = None #folosita global
unitati = None #sfolosita global
#################### Start 74HC595 pins setup - ######################
dataPIN_d   =  Pin('P9_4', Pin.OUT)
latchPIN_d  =  Pin('P9_5', Pin.OUT)
clockPIN_d  =  Pin('P9_6', Pin.OUT)
enablePIN_d =  Pin('P9_7', Pin.OUT)

dataPIN_display     = dataPIN_d
latchPIN_display    = latchPIN_d
clockPIN_display    = clockPIN_d
EnablePin_display   = enablePIN_d

### Impartire in digiti a numerelor de afisat:
def impartire_valoare_in_digiti(num):
    global mii;     mii     = num // 1000
    global sute;    sute    = (num % 1000) // 100
    global zeci;    zeci    = (num % 100) // 10
    global unitati; unitati = (num % 10)
    return

##### Display big numbers on display:  
def afisare_cifre_mari(x_pos, y_pos):
#display digit thousand:
    if (mii == 0):           afiseaza_cifra_zero_transparenta(x_pos+0,y_pos)
    elif mii == 1:           afiseaza_cifra_unu(x_pos+0,y_pos)        
    elif mii == 2:           afiseaza_cifra_doi(x_pos+0,y_pos)    
    elif mii == 3:           afiseaza_cifra_trei(x_pos+0,y_pos)    
    elif mii == 4:           afiseaza_cifra_patru(x_pos+0,y_pos)
    elif mii == 5:           afiseaza_cifra_cinci(x_pos+0,y_pos)        
    elif mii == 6:           afiseaza_cifra_sase(x_pos+0,y_pos)    
    elif mii == 7:           afiseaza_cifra_sapte(x_pos+0,y_pos)
    elif mii == 8:           afiseaza_cifra_opt(x_pos+0,y_pos)    
    elif mii == 9:           afiseaza_cifra_noua(x_pos+0,y_pos)

#display digit hundreds:
    if ( mii > 0):
        if sute == 0:        afiseaza_cifra_zero(x_pos+16,y_pos)
        else:
            if sute == 1:    afiseaza_cifra_unu(x_pos+16,y_pos)     
            elif sute == 2:  afiseaza_cifra_doi(x_pos+16,y_pos)    
            elif sute == 3:  afiseaza_cifra_trei(x_pos+16,y_pos)    
            elif sute == 4:  afiseaza_cifra_patru(x_pos+16,y_pos)
            elif sute == 5:  afiseaza_cifra_cinci(x_pos+16,y_pos)        
            elif sute == 6:  afiseaza_cifra_sase(x_pos+16,y_pos)    
            elif sute == 7:  afiseaza_cifra_sapte(x_pos+16,y_pos)
            elif sute == 8:  afiseaza_cifra_opt(x_pos+16,y_pos)    
            elif sute == 9:  afiseaza_cifra_noua(x_pos+16,y_pos)
    if (mii == 0):
        if (sute == 0):      afiseaza_cifra_zero_transparenta(x_pos+16,y_pos)
        else:
            if sute == 1:    afiseaza_cifra_unu(x_pos+16,y_pos)     
            elif sute == 2:  afiseaza_cifra_doi(x_pos+16,y_pos)    
            elif sute == 3:  afiseaza_cifra_trei(x_pos+16,y_pos)    
            elif sute == 4:  afiseaza_cifra_patru(x_pos+16,y_pos)
            elif sute == 5:  afiseaza_cifra_cinci(x_pos+16,y_pos)        
            elif sute == 6:  afiseaza_cifra_sase(x_pos+16,y_pos)    
            elif sute == 7:  afiseaza_cifra_sapte(x_pos+16,y_pos)
            elif sute == 8:  afiseaza_cifra_opt(x_pos+16,y_pos)    
            elif sute == 9:  afiseaza_cifra_noua(x_pos+16,y_pos)           
#display digit tens:
    if zeci == 0:            afiseaza_cifra_zero(x_pos+32,y_pos) 
    elif zeci == 1:          afiseaza_cifra_unu(x_pos+32,y_pos)        
    elif zeci == 2:          afiseaza_cifra_doi(x_pos+32,y_pos)    
    elif zeci == 3:          afiseaza_cifra_trei(x_pos+32,y_pos)    
    elif zeci == 4:          afiseaza_cifra_patru(x_pos+32,y_pos)
    elif zeci == 5:          afiseaza_cifra_cinci(x_pos+32,y_pos)        
    elif zeci == 6:          afiseaza_cifra_sase(x_pos+32,y_pos)    
    elif zeci == 7:          afiseaza_cifra_sapte(x_pos+32,y_pos)
    elif zeci == 8:          afiseaza_cifra_opt(x_pos+32,y_pos)    
    elif zeci == 9:          afiseaza_cifra_noua(x_pos+32,y_pos)
#display digit units:
    if unitati == 0:         afiseaza_cifra_zero(x_pos+48,y_pos) 
    elif unitati == 1:       afiseaza_cifra_unu(x_pos+48,y_pos)        
    elif unitati == 2:       afiseaza_cifra_doi(x_pos+48,y_pos)    
    elif unitati == 3:       afiseaza_cifra_trei(x_pos+48,y_pos)    
    elif unitati == 4:       afiseaza_cifra_patru(x_pos+48,y_pos)
    elif unitati == 5:       afiseaza_cifra_cinci(x_pos+48,y_pos)        
    elif unitati == 6:       afiseaza_cifra_sase(x_pos+48,y_pos)    
    elif unitati == 7:       afiseaza_cifra_sapte(x_pos+48,y_pos)
    elif unitati == 8:       afiseaza_cifra_opt(x_pos+48,y_pos)    
    elif unitati == 9:       afiseaza_cifra_noua(x_pos+48,y_pos)
    return

### Function used to update data into 74HC595:
def shift_update_display(input_d,data,clock,latch):
#put latch down to start data sending:
    clockPIN_display.value(0)
    latchPIN_display.value(0)
    clockPIN_display.value(1)
#load data in reverse order:
    for j in range(23, -1, -1):
        clockPIN_display.value(0)
        dataPIN_display.value(int(input_d[j]))
        clockPIN_display.value(1)
#put latch up to store data on register:
    clockPIN_display.value(0)
    latchPIN_display.value(1)
    clockPIN_display.value(1)
    return

### Function used to activate, deactivare and/or reset display LCD Nokia 5110:
def select_or_reset_display(string_display):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    EnablePin_display.value(1)    
    shift_update_display(string_display,dataPIN_d,clockPIN_d,latchPIN_d)
    EnablePin_display.value(0)    
    return

### Function used to initialize the display LCD Nokia 5110:
def init_display(enable_disp_nr, reset_disp_nr, contrast):
    select_or_reset_display(reset_disp_nr)
    sleep_us(10)
    select_or_reset_display(enabling_reseting_display_none)
    sleep_us(10)
    select_or_reset_display(enable_disp_nr)
    lcd = pcd8544_mod.PCD8544(spi, DC)      #set comunication between MCU and display using SPI and set DC pin:
    lcd.init(True, contrast, 0x14, 0x06)    #initialize LCD display:
    lcd.clear                               #clear LCD display:
    select_or_reset_display(enable_disp_nr)    
    return

### Display small number on display LCD Nokia 5110:
def afisare_cifre_mici(x_pos,y_pos):
#display digit thousand: nothing special will be displayed; it is hardcoded number 2 RTC, year (from year 20xx)
#display digit hundreds: nothing special will be displayed; it is hardcoded number 0 RTC, year (from year 20xx)

#display digit tens:
    if zeci == 0:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_0)
    elif zeci == 1:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_1)        
    elif zeci == 2:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_2)   
    elif zeci == 3:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_3)    
    elif zeci == 4:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_4)
    elif zeci == 5:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_5)        
    elif zeci == 6:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_6)
    elif zeci == 7:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_7)
    elif zeci == 8:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_8)   
    elif zeci == 9:
        lcd.position(x_pos+00, y_pos);    lcd.data(Cifra_9)

#display digit units:
    if unitati == 0:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_0)
    elif unitati == 1:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_1)
    elif unitati == 2:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_2)
    elif unitati == 3:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_3)
    elif unitati == 4:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_4)
    elif unitati == 5:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_5)
    elif unitati == 6:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_6)
    elif unitati == 7:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_7)
    elif unitati == 8:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_8)
    elif unitati == 9:
        lcd.position(x_pos+06, y_pos);    lcd.data(Cifra_9)    

### Display the big numbers on LCD Nokia 5110 (from four parts):
def afiseaza_cifra_zero(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_0_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_0_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_0_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_0_3)
    return
def afiseaza_cifra_unu(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_1_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_1_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_1_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_1_3)
    return
def afiseaza_cifra_doi(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_2_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_2_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_2_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_2_3)
    return
def afiseaza_cifra_trei(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_3_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_3_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_3_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_3_3)
    return
def afiseaza_cifra_patru(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_4_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_4_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_4_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_4_3)
    return
def afiseaza_cifra_cinci(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_5_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_5_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_5_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_5_3)
    return
def afiseaza_cifra_sase(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_6_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_6_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_6_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_6_3)
    return
def afiseaza_cifra_sapte(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_7_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_7_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_7_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_7_3)
    return
def afiseaza_cifra_opt(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_8_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_8_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_8_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_8_3)
    return
def afiseaza_cifra_noua(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_9_0)
    lcd.position(x_position, y_position+1);    lcd.data(Cifra_9_1)
    lcd.position(x_position, y_position+2);    lcd.data(Cifra_9_2)
    lcd.position(x_position, y_position+3);    lcd.data(Cifra_9_3)
    return
def afiseaza_cifra_zero_transparenta(x_position, y_position):
    lcd = pcd8544_mod.PCD8544(spi, DC)
    lcd.position(x_position, y_position+0);    lcd.data(Cifra_transparenta)
    return