import pcd8544_mod
from C_Display_small_big_numbers import *
lcd = pcd8544_mod.PCD8544(spi, DC) 
##### Format text and simbol for Temperature: 
def afiseaza_text_Temperatura(x_pos, y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_M)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_P)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+42,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+48,y_pos);    lcd.data(Litera_U)
    lcd.position(x_pos+54,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+60,y_pos);    lcd.data(Litera_E)
def afiseaza_semn_grad_celsius(x_pos, y_pos):
    lcd.position(x_pos+0,y_pos+0);   lcd.data(Semn_grad_Celsius)
    lcd.position(x_pos+8,y_pos+0);   lcd.data(Litera_grad_Celsius_1)
    lcd.position(x_pos+8,y_pos+1);   lcd.data(Litera_grad_Celsius_2)
def afiseaza_simbol_termometru(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_termometru_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_termometru_2)
##### Format text si simbol for Humidity:   
def afiseaza_text_Umiditate(x_pos, y_pos): 
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_H)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_U)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_M)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_D)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+42,y_pos);    lcd.data(Litera_Y) 
def afiseaza_picatura_umiditate(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_picatura_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_picatura_2)
def afiseaza_procent_RH(x_pos,y_pos):
    lcd.position(x_pos+0,y_pos+0);   lcd.data(Semnul_procent_1)
    lcd.position(x_pos+0,y_pos+1);   lcd.data(Semnul_procent_2)
    lcd.position(x_pos+4,y_pos+3);   lcd.data(Litera_R)
    lcd.position(x_pos+10,y_pos+3);  lcd.data(Litera_H)   
##### Format text and simbol for Atm Presssure:  
def afiseaza_text_Presiune_atm(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_M)
    lcd.position(x_pos+22,y_pos);    lcd.data(Litera_P)
    lcd.position(x_pos+28,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+34,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+40,y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+46,y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+52,y_pos);    lcd.data(Litera_U)
    lcd.position(x_pos+58,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+64,y_pos);    lcd.data(Litera_E)  
def afiseaza_text_mmHg(x_pos,y_pos):   
    lcd.position(x_pos+0,y_pos);     lcd.data(Litera_m)
    lcd.position(x_pos+6,y_pos);     lcd.data(Litera_m)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_H)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_g)
def afisare_simbol_presiune(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_presiune_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_presiune_2) 
##### Format text and simbol for DEW point:  
def afiseaza_text_Punct_de_roua_DEW(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_D)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_W)
    lcd.position(x_pos+22,y_pos);    lcd.data(Litera_P)
    lcd.position(x_pos+28,y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+34,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+40,y_pos);    lcd.data(Litera_N)
    lcd.position(x_pos+46,y_pos);    lcd.data(Litera_T)
def afiseaza_text_DEW(x_pos,y_pos):   
    lcd.position(x_pos+0,y_pos);     lcd.data(Litera_D)
    lcd.position(x_pos+6,y_pos);     lcd.data(Litera_E)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_W)
##### Format text and simbol for Confort factor:  
def afiseaza_text_Confort_factor(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_N)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_F)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+46,y_pos);    lcd.data(Litera_F)
    lcd.position(x_pos+52,y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+58,y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+64,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+70,y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+76,y_pos);    lcd.data(Litera_R)
def afiseaza_indice_ITU(x_pos,y_pos):   
    lcd.position(x_pos+0,y_pos);     lcd.data(Litera_I)
    lcd.position(x_pos+6,y_pos);     lcd.data(Litera_T)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_U)
def afisare_simbol_ITU_normal(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_ITU_normal_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_ITU_normal_2) 
def afisare_simbol_ITU_alerta(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_ITU_alerta_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_ITU_alerta_2)       
def afisare_simbol_ITU_disconfort(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_ITU_disconfort_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_ITU_disconfort_2)       
##### Format text and simbol for Altitudine:  
def afiseaza_text_Altitudine(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_L)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_U)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_D)
    lcd.position(x_pos+42,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+52,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+58,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+64,y_pos);    lcd.data(Litera_L)
    lcd.position(70,5);              lcd.data(Litera_m)
def afisare_simbol_altitudine(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_altitudine_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_altitudine_2)       
##### Format text fix and simbol for Barometer:  
def afiseaza_text_Barometru(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_B)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_M)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+42,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+48,y_pos);    lcd.data(Litera_R)
def afiseaza_text_Senin(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_L)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_R)
def afiseaza_text_Ploaie(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_N)
def afiseaza_text_Nori(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_L)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_U)
    lcd.position(x_pos+24, y_pos);   lcd.data(Litera_D)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_L)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_Y)
def afisare_simbol_procent(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semnul_procent)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semnul_procent)
    lcd.position(x_pos,y_pos+2);     lcd.data(Semnul_procent)
def afisare_simbol_sageata(x_pos,y_pos):
    lcd.position(x_pos,y_pos);       lcd.data(Semn_sageata)
def afisare_sageata_transparenta(x_pos,y_pos):
    lcd.position(x_pos,y_pos);       lcd.data(Sageata_transparenta)
##### Format text fix and simbol for Date and Time:  
def afiseaza_text_DATA_SI_ORA(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_D)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+28,y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+34,y_pos);    lcd.data(Litera_N)
    lcd.position(x_pos+40,y_pos);    lcd.data(Litera_D)
    lcd.position(x_pos+50,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+56,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+62,y_pos);    lcd.data(Litera_M)
    lcd.position(x_pos+68,y_pos);    lcd.data(Litera_E)        
    lcd.position(x_pos+0, y_pos+5);  lcd.data(Litera_R)
    lcd.position(x_pos+6, y_pos+5);  lcd.data(Litera_T)
    lcd.position(x_pos+12,y_pos+5);  lcd.data(Litera_C)
    lcd.position(x_pos+22,y_pos+5);  lcd.data(Litera_t)
    lcd.position(x_pos+28,y_pos+5);  lcd.data(Litera_e)
    lcd.position(x_pos+34,y_pos+5);  lcd.data(Litera_m)
    lcd.position(x_pos+40,y_pos+5);  lcd.data(Litera_p) 
    lcd.position(x_pos+67,y_pos+5);  lcd.data(Semn_grad_Celsius_mic)
    lcd.position(x_pos+73,y_pos+5);  lcd.data(Litera_C)   
##### Format text and simbol for ATM Presssure:  (sensor DPS368 Infineon)  
def afiseaza_text_Presiune_atm_Infineon(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_M)
    lcd.position(x_pos+22,y_pos);    lcd.data(Litera_P)
    lcd.position(x_pos+28,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+34,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+40,y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+46,y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+52,y_pos);    lcd.data(Litera_U)
    lcd.position(x_pos+58,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+64,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+74,y_pos);    lcd.data(Litera_I)    
def afiseaza_text_mmHg(x_pos,y_pos):   
    lcd.position(x_pos+0,y_pos);     lcd.data(Litera_m)
    lcd.position(x_pos+6,y_pos);     lcd.data(Litera_m)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_H)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_g)
def afisare_simbol_presiune(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_presiune_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_presiune_2) 
##### Format text and simbol for Altitude : (sensor DPS368 Infineon)
def afiseaza_text_Altitudine_Infineon(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_L)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_U)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_D)
    lcd.position(x_pos+42,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+74,y_pos);    lcd.data(Litera_I) 
    lcd.position(x_pos+52,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+58,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+64,y_pos);    lcd.data(Litera_L)
    lcd.position(70,5);              lcd.data(Litera_m)
def afisare_simbol_altitudine(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_altitudine_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_altitudine_2)       
##### Format text fix and simbol for CO2: (sensor PAS CO2 Infineon) 
def afiseaza_text_CO2_Infineon(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_R)
    lcd.position(x_pos+22,y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+28,y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+34,y_pos);    lcd.data(Cifra_2)
    lcd.position(x_pos+74,y_pos);    lcd.data(Litera_I) 
def afiseaza_simbol_CO2_Infineon(x_pos,y_pos):
    lcd.position(x_pos,y_pos+0);     lcd.data(Semn_CO2_1)
    lcd.position(x_pos,y_pos+1);     lcd.data(Semn_CO2_2)     
def afiseaza_text_CO2_ppm_Infineon(x_pos,y_pos):
    lcd.position(x_pos+0,y_pos);     lcd.data(Litera_p)
    lcd.position(x_pos+6,y_pos);     lcd.data(Litera_p)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_m)
##### Format text fix for connectivity display:
def afiseaza_text_connectivity(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_N)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_N)
    lcd.position(x_pos+24,y_pos);    lcd.data(Litera_E)
    lcd.position(x_pos+30,y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+36,y_pos);    lcd.data(Litera_T)
    lcd.position(x_pos+42,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+48,y_pos);    lcd.data(Litera_V)
    lcd.position(x_pos+54,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+60,y_pos);    lcd.data(Litera_T) 
    lcd.position(x_pos+66,y_pos);    lcd.data(Litera_Y)    
def afiseaza_text_conectivity_SSID(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_D)
    lcd.position(x_pos+24,y_pos);    lcd.data(Semnul_doua_puncte)
    lcd.position(x_pos+34,y_pos);    lcd.data(Litera_P)
    lcd.position(x_pos+40,y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+46,y_pos);    lcd.data(Litera_O)
    lcd.position(x_pos+52,y_pos);    lcd.data(Litera_C)
    lcd.position(x_pos+58,y_pos);    lcd.data(Cifra_6)
def afiseaza_text_conectivity_PASS(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_P)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_A)
    lcd.position(x_pos+12,y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+18,y_pos);    lcd.data(Litera_S)
    lcd.position(x_pos+24,y_pos);    lcd.data(Semnul_doua_puncte)
    lcd.position(x_pos+34,y_pos);    lcd.data(Cifra_1)
    lcd.position(x_pos+40,y_pos);    lcd.data(Cifra_2)
    lcd.position(x_pos+46,y_pos);    lcd.data(Cifra_3)
    lcd.position(x_pos+52,y_pos);    lcd.data(Cifra_4)
    lcd.position(x_pos+58,y_pos);    lcd.data(Cifra_5)
    lcd.position(x_pos+64,y_pos);    lcd.data(Cifra_6)
    lcd.position(x_pos+70,y_pos);    lcd.data(Cifra_7)
    lcd.position(x_pos+76,y_pos);    lcd.data(Cifra_8)
def afiseaza_text_conectivity_IP(x_pos,y_pos):
    lcd.position(x_pos+0, y_pos);    lcd.data(Litera_I)
    lcd.position(x_pos+6, y_pos);    lcd.data(Litera_P)
    lcd.position(x_pos+14,y_pos);    lcd.data(Cifra_1)
    lcd.position(x_pos+20,y_pos);    lcd.data(Cifra_9)
    lcd.position(x_pos+26,y_pos);    lcd.data(Cifra_2)
    lcd.position(x_pos+32,y_pos);    lcd.data(Semnul_punct)
    lcd.position(x_pos+34,y_pos);    lcd.data(Cifra_1)
    lcd.position(x_pos+40,y_pos);    lcd.data(Cifra_6)
    lcd.position(x_pos+46,y_pos);    lcd.data(Cifra_8)
    lcd.position(x_pos+52,y_pos);    lcd.data(Semnul_punct)
    lcd.position(x_pos+55,y_pos);    lcd.data(Cifra_0)
    lcd.position(x_pos+61,y_pos);    lcd.data(Semnul_punct)
    lcd.position(x_pos+64,y_pos);    lcd.data(Cifra_4)