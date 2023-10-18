#Statie pentru masurarea calitatii aerului la interior
import socket
import network
import time
import utime as time

from machine import I2C
from machine import Pin

from utime import sleep_us
from time  import sleep

from A_Definitions import *
from B_Backlight import *
from C_Display_small_big_numbers import *
from E_Display_text_fix import *
from F_Web_site import *

from bme280 import BME280
from ds3231 import ds3231
from lib    import dps310
import pasco2 as sensor

#constant used to calcul the relative altitude with BME280 sensor:
pressure_sea_level=1013.25

#configure I2C interface between sensord and PSoC6:
i2c = I2C(0, scl='P6_0', sda='P6_1', freq=100000)
#configure I2C for BME280:
bme = BME280(i2c = i2c)
#configure I2C for DS3231 RTC:
rtc = ds3231(i2c = i2c)
#configure I2C for DPS310 sensor (used with DPS 368 sensor):
dps = dps310.DPS310(i2c)
#configure I2C for PAS CO2 sensor:
bus = i2c
pasco2 = sensor.PASCO2(bus)
init_status = pasco2.initialize()

num = None #variable used for display results on LCD Nokia 5110

#74HC595: set pins to output PIN objects for reset all 74HC505:
ResetPin_b = Pin('P6_2', Pin.OUT, None, value=Pin.STATE_HIGH)
ResetPin_d = Pin('P8_0', Pin.OUT, None, value=Pin.STATE_HIGH)

### Initializing all 74HC595 at startup
ResetPin_d.value(0); sleep_us(1);
ResetPin_d.value(1); sleep_us(1);

#reset 74HC595 backlight at startup:
ResetPin_b.value(0); sleep_us(1);
ResetPin_b.value(1); sleep_us(1);

#setup and activate network wlan:
ap = network.WLAN(network.AP_IF)
ap.active(True)            #activating
ap.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass
print('Connection is successful')
print(ap.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80)) # Legarea serverului la adresa și portul specificate
s.listen(1)      # Așteptarea pentru conexiune
s.settimeout(5) # Setarea unui timeout pentru accept() (de exemplu, 5 secunde)

### Functions used to in initialize the LCDs Nokia 5110:
def initialize_display_01():
    init_display(enabling_display_01,reseting_display_01,0x3c)
def initialize_display_02():
    init_display(enabling_display_02,reseting_display_02,0x3c)
def initialize_display_03():
    init_display(enabling_display_03,reseting_display_03,0x3c)
def initialize_display_04():
    init_display(enabling_display_04,reseting_display_04,0x3c)
def initialize_display_05():
    init_display(enabling_display_05,reseting_display_05,0x3c)
def initialize_display_06():
    init_display(enabling_display_06,reseting_display_06,0x3c)  
def initialize_display_07():
    init_display(enabling_display_07,reseting_display_07,0x3c) 
def initialize_display_08():
    init_display(enabling_display_08,reseting_display_08,0x3c)
def initialize_display_09():
    init_display(enabling_display_09,reseting_display_09,0x3c) 
def initialize_display_10():
    init_display(enabling_display_10,reseting_display_10,0x3c)
def initialize_display_11():
    init_display(enabling_display_11,reseting_display_11,0x3c)
def initialize_display_12():
    init_display(enabling_display_12,reseting_display_12,0x3c) 

### Calculus data displayed on each LCD Nokia 5110:
def calcul_temperatura():
    num = round( float(t), 0 )
    impartire_valoare_in_digiti(num)
    afisare_cifre_mari(0,2)
def calcul_umiditate():
    num = round( float(hi), 0 )
    impartire_valoare_in_digiti(num)
    afisare_cifre_mari(0,2)
def calcul_ITU():
    num = round( float(itu), 0 )
    impartire_valoare_in_digiti(num)
    afisare_cifre_mari(0,2)    
    num = round( float(itu), 0 )
    if num<=65:
        afisare_simbol_ITU_normal(64,2)
    elif 65<num<80:
        afisare_simbol_ITU_alerta(64,2)
    elif num>=80:
        afisare_simbol_ITU_disconfort(64,2)           
def calcul_presiune():    
    num = round( float(press), 0 )
    impartire_valoare_in_digiti(num)
    afisare_cifre_mari(0,2)
def calcul_punct_de_roua():
    num = round( float(Dewpoint), 0 )
    impartire_valoare_in_digiti(num)    
    afisare_cifre_mari(0,2)  
def calcul_altitudine():
    num = round( float(alt), 0 )
    if num<0:
        num=0
        impartire_valoare_in_digiti(num)    
        afisare_cifre_mari(0,2)
    elif num>=0:
        impartire_valoare_in_digiti(num)    
        afisare_cifre_mari(0,2)        
def calcul_data_si_ora():
    rtc.read_time()
    num = round( float(rtc.hour()), 0 )
    impartire_valoare_in_digiti(num)  
    afisare_cifre_mici(24,2)
    lcd.position(36, 2); lcd.data(Semnul_doua_puncte)
    num = round( float(rtc.minute()), 0 )
    impartire_valoare_in_digiti(num)   
    afisare_cifre_mici(44,2)
    num = round( float(rtc.day()), 0 )
    impartire_valoare_in_digiti(num) 
    afisare_cifre_mici(6,3)
    lcd.position(18, 3); lcd.data(Semnul_impartire)
    num = round( float(rtc.month()), 0 )
    impartire_valoare_in_digiti(num)   
    afisare_cifre_mici(26,3)
    lcd.position(38, 3); lcd.data(Semnul_impartire)
    lcd.position(46, 3); lcd.data(Cifra_2)
    lcd.position(52, 3); lcd.data(Cifra_0)
    num = round( float(rtc.year()), 0 )
    impartire_valoare_in_digiti(num) 
    afisare_cifre_mici(58,3)
    num = round( float(rtc.temperature()), 0 )
    impartire_valoare_in_digiti(num)
    afisare_cifre_mici(55,5)
def calcul_barometru():
    num = round( float(press), 0 )
    impartire_valoare_in_digiti(num)   
    if num<750:
        if 740<=num<745:
            num = 00; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,2)
            num = 50; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,3)
            num = 50; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,4)
            afisare_sageata_transparenta(0,2)
            afisare_simbol_sageata(0,3)
            afisare_simbol_sageata(0,4)
            num = round( float(press), 0 )
        elif 745<=num<750:
            num = 00; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,2)
            num = 10; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,3)
            num = 90; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,4)
            afisare_sageata_transparenta(0,2)
            afisare_sageata_transparenta(0,3)
            afisare_simbol_sageata(0,4)
            num = round( float(press), 0 )     
    elif 750<=num<760:
        if 750<=num<752:
            num = 00; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,2)
            num = 90; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,3)
            num = 10; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,4)
            afisare_sageata_transparenta(0,2)
            afisare_simbol_sageata(0,3)
            afisare_sageata_transparenta(0,4)
            num = round( float(press), 0 )
        elif 752<=num<755:
            num = 25; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,2)
            num = 50; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,3)
            num = 25; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,4)
            afisare_sageata_transparenta(0,2)
            afisare_simbol_sageata(0,3)
            afisare_sageata_transparenta(0,4)            
            num = round( float(press), 0 )                
        elif 755<=num<759:
            num = 90; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,2)
            num = 10; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,3)
            num = 00; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,4)
            afisare_simbol_sageata(0,2)
            afisare_sageata_transparenta(0,3)
            afisare_sageata_transparenta(0,4)            
            num = round( float(press), 0 )  
    elif num>=760:
        if 760<=num<765:
            num = 50; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,2)
            num = 50; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,3)
            num = 00; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,4)
            afisare_simbol_sageata(0,2)
            afisare_simbol_sageata(0,3)
            afisare_sageata_transparenta(0,4)            
            num = round( float(press), 0 )
        elif 765<=num:
            num = 90; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,2)
            num = 10; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,3)
            num = 00; impartire_valoare_in_digiti(num); lcd = pcd8544_mod.PCD8544(spi, DC); afisare_cifre_mici(58,4)
            afisare_simbol_sageata(0,2)
            afisare_sageata_transparenta(0,3)
            afisare_sageata_transparenta(0,4)             
            num = round( float(press), 0 ) 
def calcul_atm_press_Infineon():
    num = round( float(dps.pressure*0.75), 0 )
    impartire_valoare_in_digiti(num)
    afisare_cifre_mari(0,2)
def calcul_altitudine_Infineon():
    num = round( float(dps.altitude), 0 )
    impartire_valoare_in_digiti(num)
    afisare_cifre_mari(0,2)    
def calcul_co2_Infineon():
    co2value = co2ppm
    if co2value<0:
        num=000
    else:
        num = co2ppm
    impartire_valoare_in_digiti(num)
    afisare_cifre_mari(0,2)   
def sensor_init(): 
    if init_status != 0:
        print("[co2-module] : Sensor setup failed!")
        return -1
    else:
        print("[co2-module] : Sensor setup done successfully!")
        return pasco2
def read_sensor_data(co2Obj):
    global co2ppm
    co2ppm = co2Obj.get_co2_value()
    if co2ppm == -1:
        print("[co2-module] : Measurement not ready yet")
    else:
        print("[co2-module] : co2 ppm value: ", co2ppm)
           
### Display data in REPL console:  
def afisare_date_in_consola():
    print("Temperature:       {}".format(t), "°C")
    print("Humidity:          {}".format(hi), "%")
    print("Indice ITU:        {}".format(itu), "%")
    print("Presiune atm:      {}".format(press), "mmHg")
    print("Punct de roua DEW: {}".format(Dewpoint), "°C")
    print("Altitudine:        {}".format(alt), "meters")
    print(rtc.day(),"/",rtc.month(),"/20",rtc.year(),"  ",rtc.hour(),":",rtc.minute(),":",rtc.sec())
    print("RTC temp: ",rtc.temperature(), "°C")
    print("Presiune atm Infineon: {}".format(dps.pressure*0.75), "mmHg")
    print("Altitude rel Infineon: {}".format(dps.altitude), "meters")
    print("CO2 Infineon: ", co2ppm, "ppm")    

### Initializare display-uri:
def initializare_display_uri():
    initialize_display_01() #initializa display 01
    initialize_display_02() #initializa display 02
    initialize_display_03() #initializa display 03
    initialize_display_04() #initializa display 04
    initialize_display_05() #initializa display 05
    initialize_display_06() #initializa display 06
    initialize_display_07() #initializa display 07
    initialize_display_08() #initializa display 08
    initialize_display_09() #initializa display 00
    initialize_display_10() #initializa display 10
    initialize_display_11() #initializa display 11
    initialize_display_12() #initializa display 12

### Read all sensors:
def read_all_sensors():
    global t; global p; global h; global hi; global itu; global press; global Dewpoint; global alt; global press_I; global alt_I;
    t,p,h = bme.read_compensated_data()
    t = t / 100
    p = p // 256
    pi = p // 100
    pd = p - pi * 100    
    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    itu = (t*1.8 + 32) - (0.55 - 0.0055*hi) * ((t*1.8 + 32)-58)
    itu = round(float(itu), 0 )
    press=pi*0.75 #convert from hPa in mmHg
    Dewpoint = ((t)-(100-hi)/5)
    alt = (153.84*((t)+273.15))*(1-((p/100)/pressure_sea_level)**(1/5.257)) #calculus for relative altitude
    read_sensor_data(co2Obj)
    press_I = dps.pressure*0.75 # for web page display
    alt_I   = dps.altitude      # for web page display

def display_data_on_LCDs():
    select_or_reset_display(enabling_display_01); afisare_text_fix_Temperatura();           calcul_temperatura();         #show data on display 01:        
    select_or_reset_display(enabling_display_02); afisare_text_fix_Umiditate();             calcul_umiditate();           #show data on display 02:
    select_or_reset_display(enabling_display_03); afisare_text_fix_ITU();                   calcul_ITU();                 #show data on display 03:   
    select_or_reset_display(enabling_display_04); afisare_text_fix_Punct_de_roua_DEW();     calcul_punct_de_roua();       #show data on display 04:   
    select_or_reset_display(enabling_display_05); afisare_text_fix_Presiune_atm();          calcul_presiune();            #show data on display 05:      
    select_or_reset_display(enabling_display_06); afisare_text_fix_Altitudine();            calcul_altitudine();          #show data on display 06:     
    select_or_reset_display(enabling_display_07); afisare_text_fix_Barometru();             calcul_barometru();           #show data on display 07:   
    select_or_reset_display(enabling_display_08); afisare_text_fix_DATA_SI_ORA();           calcul_data_si_ora();         #show data on display 08:
    select_or_reset_display(enabling_display_09); afisare_text_fix_Presiune_atm_Infineon(); calcul_atm_press_Infineon();  #show data on display 09:
    select_or_reset_display(enabling_display_10); afisare_text_fix_Altitudine_Infineon();   calcul_altitudine_Infineon(); #show data on display 10:
    select_or_reset_display(enabling_display_11); afisare_text_fix_CO2_Infineon();          calcul_co2_Infineon();        #show data on display 11:
    select_or_reset_display(enabling_display_12); afisare_text_fix_connectivity();                                        #show data on display 12:
    
##################### MAIN PROGRAM: ######################
initializare_display_uri()
backlight_off_at_start()
co2Obj = sensor_init()
joc_la_pornire()

while True:
    try:        
        conn, addr = s.accept()                     # Socket accept() 
        print("Got connection from %s" % str(addr))
        print("Date cu conexiune la wlan AP!")    
        request=conn.recv(1024)                     # Socket receive()
        print("")
        print("Content %s" % str(request))
        request = str(request)                      # Socket send()
        update = request.find('/getData')
        if update == 6:
            read_all_sensors()                      # read all sensord 
            afisare_date_in_consola()               # display data in REPL console
            #create string with data to displat in web page:
            response = str(round(t))+"|"+str(round(hi))+"|"+str(round(itu))+"|"+str(round(Dewpoint))+"|"+str(round(press))+"|"+str(round(alt))+"|"+str(round(press_I))+"|"+str(round(alt_I))+"|"+str(round(co2ppm))
        else:
            response = web_page()       
        # Create a socket reply
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)    
        conn.close()                                # Socket close()
    except:
        print("Date fara conexiune la wlan AP!")
        read_all_sensors()                          # read all sensord 
        afisare_date_in_consola()                   # display data in REPL console
        display_data_on_LCDs()
        sleep(10)
s.close()
