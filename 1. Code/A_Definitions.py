###############################################################
### Numbers, letters and signs that will be displayed on
### Nokia 5110 LCD displays
###############################################################

###############################################################
### SSID and PASS for WiFi AP::
###############################################################
ssid     = 'PSOC6'         #Set access point name 
password = '12345678'      #Set your access point password

###############################################################
### Definition of large numbers, 16 pixels height:
###############################################################
#Number 0:
Cifra_0_0 = bytearray(b'\xFC\xF9\xF3\xE7\x0F\x0F\x0F\x0F\x0F\x0F\xE7\xF3\xF9\xFC\x00\x00')
Cifra_0_1 = bytearray(b'\x7F\x3F\x1F\x0F\x00\x00\x00\x00\x00\x00\x0F\x1F\x3F\x7F\x00\x00')
Cifra_0_2 = bytearray(b'\xFE\xFC\xF8\xF0\x00\x00\x00\x00\x00\x00\xF0\xF8\xFC\xFE\x00\x00')
Cifra_0_3 = bytearray(b'\x3F\x9F\xCF\xE7\xF0\xF0\xF0\xF0\xF0\xF0\xE7\xCF\x9F\x3F\x00\x00')
#Number 1:
Cifra_1_0 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE0\xF0\xF8\xFC\x00\x00')
Cifra_1_1 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x1F\x3F\x7F\x00\x00')
Cifra_1_2 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xF0\xF8\xFC\xFE\x00\x00')
Cifra_1_3 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x0F\x1F\x3F\x00\x00')
#Number 2:
Cifra_2_0 = bytearray(b'\x00\x01\x03\x07\x0F\x0F\x0F\x0F\x0F\x0F\xE7\xF3\xF9\xFC\x00\x00')
Cifra_2_1 = bytearray(b'\x00\x00\x80\xC0\xC0\xC0\xC0\xC0\xC0\xC0\xCF\x9F\x3F\x7F\x00\x00')
Cifra_2_2 = bytearray(b'\xFE\xFC\xF9\xF3\x03\x03\x03\x03\x03\x03\x03\x01\x00\x00\x00\x00')
Cifra_2_3 = bytearray(b'\x3F\x9F\xCF\xE7\xF0\xF0\xF0\xF0\xF0\xF0\xE0\xE0\xC0\x80\x00\x00')
#Number 3:
Cifra_3_0 = bytearray(b'\x00\x01\x03\x07\x0F\x0F\x0F\x0F\x0F\x0F\xE7\xF3\xF9\xFC\x00\x00')
Cifra_3_1 = bytearray(b'\x00\x00\x80\xC0\xC0\xC0\xC0\xC0\xC0\xC0\xCF\x9F\x3F\x7F\x00\x00')
Cifra_3_2 = bytearray(b'\x00\x00\x01\x03\x03\x03\x03\x03\x03\x03\xF3\xF9\xFC\xFE\x00\x00')
Cifra_3_3 = bytearray(b'\x00\x80\xC0\xE0\xF0\xF0\xF0\xF0\xF0\xF0\xE7\xCF\x9F\x3F\x00\x00')
#Number 4:
Cifra_4_0 = bytearray(b'\xFC\xF8\xF0\xE0\x00\x00\x00\x00\x00\x00\xE0\xF0\xF8\xFC\x00\x00')
Cifra_4_1 = bytearray(b'\x7F\x3F\x9F\xCF\xC0\xC0\xC0\xC0\xC0\xC0\xCF\x9F\x3F\x7F\x00\x00')
Cifra_4_2 = bytearray(b'\x00\x00\x01\x03\x03\x03\x03\x03\x03\x03\xF3\xF9\xFC\xFE\x00\x00')
Cifra_4_3 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x0F\x1F\x3F\x00\x00')
#Number 5:
Cifra_5_0 = bytearray(b'\xFC\xF9\xF3\xE7\x0F\x0F\x0F\x0F\x0F\x0F\x0F\x07\x03\x01\x00\x00')
Cifra_5_1 = bytearray(b'\x7F\x3F\x9F\xCF\xC0\xC0\xC0\xC0\xC0\xC0\xC0\x80\x00\x00\x00\x00')
Cifra_5_2 = bytearray(b'\x00\x00\x01\x03\x03\x03\x03\x03\x03\x03\xF3\xF9\xFC\xFE\x00\x00')
Cifra_5_3 = bytearray(b'\x00\x80\xC0\xE0\xF0\xF0\xF0\xF0\xF0\xF0\xE7\xCF\x9F\x3F\x00\x00')
#Number 6:
Cifra_6_0 = bytearray(b'\xFC\xF9\xF3\xE7\x0F\x0F\x0F\x0F\x0F\x0F\x0F\x07\x03\x01\x00\x00')
Cifra_6_1 = bytearray(b'\x7F\x3F\x9F\xCF\xC0\xC0\xC0\xC0\xC0\xC0\xC0\x80\x00\x00\x00\x00')
Cifra_6_2 = bytearray(b'\xFE\xFC\xF9\xF3\x03\x03\x03\x03\x03\x03\xF3\xF9\xFC\xFE\x00\x00')
Cifra_6_3 = bytearray(b'\x3F\x9F\xCF\xE7\xF0\xF0\xF0\xF0\xF0\xF0\xE7\xCF\x9F\x3F\x00\x00')
#Number 7:
Cifra_7_0 = bytearray(b'\x00\x01\x03\x07\x0F\x0F\x0F\x0F\x0F\x0F\xE7\xF3\xF9\xFC\x00\x00')
Cifra_7_1 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x1F\x3F\x7F\x00\x00')
Cifra_7_2 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xF0\xF8\xFC\xFE\x00\x00')
Cifra_7_3 = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x0F\x1F\x3F\x00\x00')
#Number 8:
Cifra_8_0 = bytearray(b'\xFC\xF9\xF3\xE7\x0F\x0F\x0F\x0F\x0F\x0F\xE7\xF3\xF9\xFC\x00\x00')
Cifra_8_1 = bytearray(b'\x7F\x3F\x9F\xCF\xC0\xC0\xC0\xC0\xC0\xC0\xCF\x9F\x3F\x7F\x00\x00')
Cifra_8_2 = bytearray(b'\xFE\xFC\xF9\xF3\x03\x03\x03\x03\x03\x03\xF3\xF9\xFC\xFE\x00\x00')
Cifra_8_3 = bytearray(b'\x3F\x9F\xCF\xE7\xF0\xF0\xF0\xF0\xF0\xF0\xE7\xCF\x9F\x3F\x00\x00')
#Number 9:
Cifra_9_0 = bytearray(b'\xFC\xF9\xF3\xE7\x0F\x0F\x0F\x0F\x0F\x0F\xE7\xF3\xF9\xFC\x00\x00')
Cifra_9_1 = bytearray(b'\x7F\x3F\x9F\xCF\xC0\xC0\xC0\xC0\xC0\xC0\xCF\x9F\x3F\x7F\x00\x00')
Cifra_9_2 = bytearray(b'\x00\x00\x01\x03\x03\x03\x03\x03\x03\x03\xF3\xF9\xFC\xFE\x00\x00')
Cifra_9_3 = bytearray(b'\x00\x80\xC0\xE0\xF0\xF0\xF0\xF0\xF0\xF0\xE7\xCF\x9F\x3F\x00\x00')

Cifra_transparenta = bytearray(b'\x00')


###############################################################
### Definition of small numbers, 8 pixels height:
###############################################################
Cifra_0 = bytearray(b'\x3E\x41\x41\x41\x3E\x00') #Number 0
Cifra_1 = bytearray(b'\x00\x42\x7F\x40\x00\x00') #Number 1
Cifra_2 = bytearray(b'\x42\x61\x51\x49\x46\x00') #Number 2
Cifra_3 = bytearray(b'\x21\x41\x45\x4B\x31\x00') #Number 3
Cifra_4 = bytearray(b'\x18\x14\x12\x7F\x10\x00') #Number 4
Cifra_5 = bytearray(b'\x27\x45\x45\x45\x39\x00') #Number 5
Cifra_6 = bytearray(b'\x3C\x4A\x49\x49\x30\x00') #Number 6
Cifra_7 = bytearray(b'\x01\x71\x09\x05\x03\x00') #Number 7
Cifra_8 = bytearray(b'\x36\x49\x49\x49\x36\x00') #Number 8
Cifra_9 = bytearray(b'\x06\x49\x49\x29\x1E\x00') #Number 9


###############################################################
### Definition of capital letter, 8 pixels height:
###############################################################
Litera_A = bytearray(b'\x7E\x11\x11\x11\x7E\x00') #Letter A
Litera_B = bytearray(b'\x7F\x49\x49\x49\x36\x00') #Letter B
Litera_C = bytearray(b'\x3E\x41\x41\x41\x22\x00') #Letter C
Litera_D = bytearray(b'\x7F\x41\x41\x41\x3E\x00') #Letter D
Litera_E = bytearray(b'\x7f\x49\x49\x49\x41\x00') #Letter E
Litera_F = bytearray(b'\x7F\x09\x09\x09\x01\x00') #Letter F
#Litera_G = bytearray(b'\x7F\x09\x09\x09\x01\x00') #Letter FG
Litera_H = bytearray(b'\x7F\x08\x08\x08\x7F\x00') #Letter H
Litera_I = bytearray(b'\x41\x41\x7F\x41\x41\x00') #Letter I
#Litera_J = bytearray(b'\x41\x41\x7F\x41\x41\x00') #Letter IJ
#Litera_K = bytearray(b'\x41\x41\x7F\x41\x41\x00') #Letter IK
Litera_L = bytearray(b'\x7F\x40\x40\x40\x40\x00') #Letter L
Litera_M = bytearray(b'\x7F\x02\x0C\x02\x7F\x00') #Letter M
Litera_N = bytearray(b'\x7F\x04\x08\x10\x7F\x00') #Letter N
Litera_O = bytearray(b'\x3E\x41\x41\x41\x3E\x00') #Letter O
Litera_P = bytearray(b'\x7F\x09\x09\x09\x06\x00') #Letter P
#Litera_Q = bytearray(b'\x41\x41\x7F\x41\x41\x00') #Letter IQ
Litera_R = bytearray(b'\x7F\x09\x19\x29\x46\x00') #Letter R
Litera_S = bytearray(b'\x26\x49\x49\x49\x32\x00') #Letter S
Litera_T = bytearray(b'\x01\x01\x7F\x01\x01\x00') #Letter T
Litera_U = bytearray(b'\x3F\x40\x40\x40\x3F\x00') #Letter U
Litera_V = bytearray(b'\x1F\x20\x40\x20\x1F\x00') #Letter V
#Litera_X = bytearray(b'\x41\x41\x7F\x41\x41\x00') #Letter IX
Litera_Y = bytearray(b'\x03\x04\x78\x04\x03\x00') #Letter Y
Litera_W = bytearray(b'\x3F\x40\x38\x40\x3F\x00') #Letter W
#Litera_Z = bytearray(b'\x41\x41\x7F\x41\x41\x00') #Letter IZ


###############################################################
### Definition of lowercase letter, 8 pixels height:
###############################################################
Litera_p = bytearray(b'\xF8\x28\x28\x28\x10\x00') #Letter p
Litera_e = bytearray(b'\x38\x54\x54\x54\x18\x00') #Letter e
Litera_b = bytearray(b'\xF8\xA0\xA0\xA0\x40\x00') #Letter b
Litera_m = bytearray(b'\x7C\x04\x18\x04\x78\x00') #Letter m
Litera_g = bytearray(b'\x18\xA4\xA4\xA4\x78\x00') #Letter g
Litera_t = bytearray(b'\x04\x3F\x44\x40\x20\x00') #Letter t

###############################################################
### Definition of special characters, 8 & 16 pixels height:
###############################################################
Semnul_punct          = bytearray(b'\x60\x60') #Semnul "."
Semnul_doua_puncte    = bytearray(b'\x00\x00\x66\x66') #Semnul ":"
Semnul_procent_1      = bytearray(b'\x1E\x3F\x33\x33\x3F\x9E\xC0\x60\x30\x18\x0C\x06\x03\x01\x00') #sign %, upper part
Semnul_procent_2      = bytearray(b'\x30\x18\x0C\x06\x03\x01\x00\x00\x1E\x3F\x33\x33\x3F\x1E\x00') #sign %, lower part
Semn_grad_Celsius     = bytearray(b'\x00\x1E\x3F\x33\x33\x3F\x1E\x00') #Celsius degree sigh:
Semnul_procent        = bytearray(b'\x47\x25\x17\x08\x74\x52\x71\x00') #sigh %, 8 pixel height
Semn_sageata          = bytearray(b'\x08\x08\x08\x08\x08\x3E\x1C\x08') #sign horizontal arrow to right
Sageata_transparenta  = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00') #sign transparent arrow
Semnul_impartire      = bytearray(b'\x00\x40\x20\x10\x08\x04\x00\x00') #sign /, 8 pixel height
Semn_grad_Celsius_mic = bytearray(b'\x00\x00\x07\x05\x07\x00')         #sign degreee Celsius, 8 pixel height

Litera_grad_Celsius_1 = bytearray(b'\xFC\xFE\xFF\x0F\x07\x07\x07\x07\x0F\x1F\x1E\x1C') #Letter C, upper part
Litera_grad_Celsius_2 = bytearray(b'\x3F\x7F\xFF\xF0\xE0\xE0\xE0\xE0\xF0\xF8\x78\x38') #Letter C, lower part

Semn_picatura_1       = bytearray(b'\x00\x00\x00\x80\x60\x1C\x03\x1C\x60\x80\x00\x00')
Semn_picatura_2       = bytearray(b'\x00\x1E\x3D\x6C\xDC\xDC\xFC\xFC\xFC\x7C\x3D\x1E')

Semn_termometru_1     = bytearray(b'\x00\x00\xFE\x01\xFD\x01\xFE\x00\x00')
Semn_termometru_2     = bytearray(b'\x38\x44\x83\xB8\x3F\xB8\x83\x44\x38')
 
Semn_ITU_normal_1     = bytearray(b'\xE0\x10\x08\x24\x22\x21\x21\x21\x01\x21\x21\x21\x22\x24\x08\x10\xE0')
Semn_ITU_normal_2     = bytearray(b'\x07\x08\x10\x20\x40\x88\x90\x90\x90\x90\x90\x88\x40\x20\x10\x08\x07')

Semn_ITU_alerta_1     = bytearray(b'\xE0\x10\x08\x64\x92\x91\x61\x01\x01\x01\x61\x91\x92\x64\x08\x10\xE0')
Semn_ITU_alerta_2     = bytearray(b'\x07\x08\x10\x20\x40\x80\x90\x90\x90\x90\x90\x80\x40\x20\x10\x08\x07')

Semn_ITU_disconfort_1 = bytearray(b'\xE0\x10\x08\x44\x22\x11\x09\x01\x01\x01\x09\x11\x22\x44\x08\x10\xE0')
Semn_ITU_disconfort_2 = bytearray(b'\x07\x08\x10\x20\x40\x90\x88\x88\x88\x88\x88\x90\x40\x20\x10\x08\x07')

Semn_presiune_1       = bytearray(b'\x00\x00\xC0\x80\x00\x00\xC4\x4C\x5E\x4C\xC4\x00\x00\x80\xC0\x00')
Semn_presiune_2       = bytearray(b'\x00\x01\x07\x03\x01\x00\x47\x64\xF4\x64\x47\x00\x01\x03\x07\x01')

Semn_altitudine_1     = bytearray(b'\x00\x00\x00\x80\x60\x18\x87\x0C\x10\x60\x80\x00\x00\x00\x00\x04\x06\xFF\x06\x04')
Semn_altitudine_2     = bytearray(b'\xE0\xD8\xC6\xF1\xC8\xC6\xC1\xC3\xC4\xD8\xE0\xC3\xC6\xC8\xF0\xE0\x00\xFF\x00\x00')

Semn_CO2_1            = bytearray(b'\x00\x00\x00\x80\x10\x10\x38\x7C\xFF\x7C\x38\x10\x10\x00\x00\xC0\x00\x00\x00\x00')
Semn_CO2_2            = bytearray(b'\x04\x04\x0E\x3F\x0E\x04\x04\x00\x01\x00\x00\x02\x02\x07\x1F\x07\x02\x02\x00\x00')

###############################################################
### Strings used to enable each LCD display:
###############################################################
enabling_display_01            = "101111111111111111111111"
enabling_display_02            = "111011111111111111111111"
enabling_display_03            = "111110111111111111111111"
enabling_display_04            = "111111101111111111111111"
enabling_display_05            = "111111111011111111111111"
enabling_display_06            = "111111111110111111111111"
enabling_display_07            = "111111111111101111111111"
enabling_display_08            = "111111111111111011111111"
enabling_display_09            = "111111111111111110111111"
enabling_display_10            = "111111111111111111101111"
enabling_display_11            = "111111111111111111111011"
enabling_display_12            = "111111111111111111111110"

###############################################################
### Strings used to reset each LCD display:
###############################################################
reseting_display_01            = "011111111111111111111111"
reseting_display_02            = "110111111111111111111111"
reseting_display_03            = "111101111111111111111111"
reseting_display_04            = "111111011111111111111111"
reseting_display_05            = "111111110111111111111111"
reseting_display_06            = "111111111101111111111111"
reseting_display_07            = "111111111111011111111111"
reseting_display_08            = "111111111111110111111111"
reseting_display_09            = "111111111111111101111111"
reseting_display_10            = "111111111111111111011111"
reseting_display_11            = "111111111111111111110111"
reseting_display_12            = "111111111111111111111101"

enabling_reseting_display_none = "111111111111111111111111"

#variables used for On/Off background (b):
b01 = "0"; b02 = "0"; b03 = "0"; b04 = "0";
b05 = "0"; b06 = "0"; b07 = "0"; b08 = "0";
b09 = "0"; b10 = "0"; b11 = "0"; b12 = "0";

