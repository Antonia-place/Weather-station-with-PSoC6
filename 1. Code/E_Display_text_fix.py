
from D_Format_text_fix import *


#############################################################################
##### Afisare text fix pe fiecare display:  
#############################################################################
##### Function used to display text fix on each display:  
def afisare_text_fix_Temperatura():
    afiseaza_text_Temperatura(3,0)
    afiseaza_simbol_termometru(0,2)
    afiseaza_semn_grad_celsius(64,2)    
def afisare_text_fix_Umiditate():
    afiseaza_text_Umiditate(10, 0)
    afiseaza_picatura_umiditate(0,2)
    afiseaza_procent_RH(64,2)
def afisare_text_fix_ITU():
    afiseaza_text_Confort_factor(0,0)
    afiseaza_indice_ITU(64,5)
    afisare_simbol_ITU_normal(64,2)    
def afisare_text_fix_Presiune_atm():  
    afiseaza_text_Presiune_atm(0,0)
    afiseaza_text_mmHg(60,5)
    afisare_simbol_presiune(64,2)
def afisare_text_fix_Punct_de_roua_DEW():
    afiseaza_text_Punct_de_roua_DEW(0,0)
    afiseaza_text_DEW(64,5)
    afiseaza_simbol_termometru(0,2)
    afiseaza_semn_grad_celsius(64,2) 
def afisare_text_fix_Altitudine():
    afiseaza_text_Altitudine(0,0)
    afisare_simbol_altitudine(64,2)
def afisare_text_fix_Barometru():
    afiseaza_text_Barometru(0,0)
    afisare_simbol_procent(72,2)
    afiseaza_text_Senin(8,2)
    afiseaza_text_Nori(8,3)
    afiseaza_text_Ploaie(8,4)
def afisare_text_fix_DATA_SI_ORA():
    afiseaza_text_DATA_SI_ORA(0,0)
def afisare_text_fix_Presiune_atm_Infineon():  
    afiseaza_text_Presiune_atm_Infineon(0,0)
    afiseaza_text_mmHg(60,5)
    afisare_simbol_presiune(64,2)
def afisare_text_fix_Altitudine_Infineon():
    afiseaza_text_Altitudine_Infineon(0,0)
    afisare_simbol_altitudine(64,2)
def afisare_text_fix_CO2_Infineon():
    afiseaza_text_CO2_Infineon(0,0)
    afiseaza_simbol_CO2_Infineon(64,2)
    afiseaza_text_CO2_ppm_Infineon(64,5)
def afisare_text_fix_connectivity():
    afiseaza_text_connectivity(0,0)
    afiseaza_text_conectivity_SSID(0,2)
    afiseaza_text_conectivity_PASS(0,3)
    afiseaza_text_conectivity_IP(0,4)

