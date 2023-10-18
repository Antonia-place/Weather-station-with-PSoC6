
from machine import Pin
from utime import sleep_us
from time  import sleep

import time

from A_Definitions import *

string_backlight = None


#################### Start 74HC595 pins setup - ######################
dataPIN_b   = Pin('P12_0', Pin.OUT)
latchPIN_b  = Pin('P12_3', Pin.OUT)
clockPIN_b  = Pin('P13_4', Pin.OUT)
enablePIN_b = Pin('P13_6', Pin.OUT)

dataPIN_backlight     = dataPIN_b
latchPIN_backlight    = latchPIN_b
clockPIN_backlight    = clockPIN_b
EnablePin_backlight   = enablePIN_b


#define shift register update function for 74HC595 used for backlight On/Off::
def shift_update_backlight(input_b,data,clock,latch):
#put latch down to start data sending
    clockPIN_backlight.value(0)
    latchPIN_backlight.value(0)
    clockPIN_backlight.value(1)   
#load data in reverse order
    for i in range(11, -1, -1):
        clockPIN_backlight.value(0)
        dataPIN_backlight.value(int(input_b[i]))
        clockPIN_backlight.value(1)
#put latch up to store data on register
    clockPIN_backlight.value(0)
    latchPIN_backlight.value(1)   
    clockPIN_backlight.value(1)   
    return

#function used to create a string for activate backlight:
#def create_string():
#    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])

def backlight_on_off(string_backlight):
#    create_string()
    EnablePin_backlight.value(1)
    shift_update_backlight(string_backlight,dataPIN_b,clockPIN_b,latchPIN_b)
    EnablePin_backlight.value(0)

def backlight_off_at_start():   
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
        
def joc_la_pornire():
    print("Joc la pornire")
    b01 = "1"; b02 = "0"; b03 = "0"; b04 = "0";
    b05 = "0"; b06 = "0"; b07 = "0"; b08 = "0";
    b09 = "0"; b10 = "0"; b11 = "0"; b12 = "0";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)

    b01 = "1"; b02 = "1"; b03 = "0"; b04 = "0";
    b05 = "1"; b06 = "0"; b07 = "0"; b08 = "0";
    b09 = "0"; b10 = "0"; b11 = "0"; b12 = "0";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)

    b01 = "1"; b02 = "1"; b03 = "1"; b04 = "0";
    b05 = "1"; b06 = "1"; b07 = "0"; b08 = "0";
    b09 = "1"; b10 = "0"; b11 = "0"; b12 = "0";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)

    b01 = "0"; b02 = "1"; b03 = "1"; b04 = "1";
    b05 = "1"; b06 = "1"; b07 = "1"; b08 = "0";
    b09 = "1"; b10 = "1"; b11 = "0"; b12 = "0";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)   

    b01 = "0"; b02 = "0"; b03 = "1"; b04 = "1";
    b05 = "0"; b06 = "1"; b07 = "1"; b08 = "1";
    b09 = "1"; b10 = "1"; b11 = "1"; b12 = "0";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)    

    b01 = "0"; b02 = "0"; b03 = "0"; b04 = "1";
    b05 = "0"; b06 = "0"; b07 = "1"; b08 = "1";
    b09 = "0"; b10 = "1"; b11 = "1"; b12 = "1";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza fucntia de On/Off backgroung
    time.sleep(0.5)   

    b01 = "0"; b02 = "0"; b03 = "0"; b04 = "0";
    b05 = "0"; b06 = "0"; b07 = "0"; b08 = "1";
    b09 = "0"; b10 = "0"; b11 = "1"; b12 = "1";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)    

    b01 = "0"; b02 = "0"; b03 = "0"; b04 = "0";
    b05 = "0"; b06 = "0"; b07 = "0"; b08 = "0";
    b09 = "0"; b10 = "0"; b11 = "0"; b12 = "1";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)    

    b01 = "0"; b02 = "0"; b03 = "0"; b04 = "0";
    b05 = "0"; b06 = "0"; b07 = "0"; b08 = "0";
    b09 = "0"; b10 = "0"; b11 = "0"; b12 = "0";
    string_backlight = "".join([b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12])
    backlight_on_off(string_backlight)		#apeleaza functia de On/Off backgroung
    time.sleep(0.5)
    