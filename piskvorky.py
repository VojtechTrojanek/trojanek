inp = set()
cisla = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
import time
import random
deska = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
hrac = "\033[31mX\033[0m"
vitez = None
stavHry = True

def hraci_pole(deska):
    print("")
    print(deska[0] + " | " + deska[1] + " | " + deska[2])
    print(deska[3] + " | " + deska[4] + " | " + deska[5])
    print(deska[6] + " | " + deska[7] + " | " + deska[8])
    
def hrac_input(deska):
    while True:
        inp = int(input("\nzadejte číslo 1-9: "))
        if inp <= 9 and inp >= 1 and deska[inp-1] not in ["\033[31mX\033[0m", "\033[34mO\033[0m"]:
            deska[inp-1] = hrac
            break
        else:
            print("\nchybný input, zadejte číslo 1-9")

def pocitac_input(deska, cisla):
    while True:
        pc = random.choice(cisla)
        pc = int(pc)
        if pc <= 9 and pc >= 1 and deska[pc-1] not in ["\033[31mX\033[0m", "\033[34mO\033[0m"]:
                deska[pc-1] = hrac
                return False
        else:
            return True
            
def kontrola_vyhry(deska):
    global vitez
    if deska[0] == deska[1] == deska[2] and deska[0] != "1":
        vitez = hrac
    elif deska[3] == deska[4] == deska[5] and deska[3] != "4":
        vitez = hrac
    elif deska[6] == deska[7] == deska[8] and deska[6] != "7":
        vitez = hrac
    elif deska[0] == deska[3] == deska[6] and deska[0] != "1":
        vitez = hrac
    elif deska[1] == deska[4] == deska[7] and deska[1] != "2":
        vitez = hrac
    elif deska[2] == deska[5] == deska[8] and deska[2] != "3":
        vitez = hrac
    elif deska[0] == deska[4] == deska[8] and deska[0] != "1":
        vitez = hrac
    elif deska[2] == deska[4] == deska[6] and deska[2] != "3":
        vitez = hrac
    if vitez != None:
        hraci_pole(deska)
        print("\nVyhrál hráč: " + vitez)
        stavHry = False

def kontrola_remizy(deska):
    plno = (deska[0] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and deska[1] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and deska[2] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and
            deska[3] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and deska[4] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and deska[5] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and
            deska[6] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and deska[7] in ["\033[31mX\033[0m", "\033[34mO\033[0m"] and deska[8] in ["\033[31mX\033[0m", "\033[34mO\033[0m"]
            )
    if plno == True:
        print("remíza")
        stavHry = False

def zmena_hrace():
    global hrac
    if hrac == "\033[31mX\033[0m":
        hrac = "\033[34mO\033[0m"
    else:
        hrac = "\033[31mX\033[0m"
        
def hra():
    while stavHry:
        if vitez != None:
            break
        hraci_pole(deska)
        if vitez != None:
            break
        hrac_input(deska)
        kontrola_vyhry(deska)
        if vitez != None:
            break
        kontrola_remizy(deska)
        zmena_hrace()
        
def hra_bot():
    while stavHry:
        if vitez != None:
            break
        hraci_pole(deska)
        if vitez != None:
            break
        hrac_input(deska)
        kontrola_vyhry(deska)
        if vitez != None:
            break
        kontrola_remizy(deska)
        zmena_hrace()
        pocitac_input(deska,cisla)
        kontrola_vyhry(deska)
        if vitez != None:
            break
        kontrola_remizy(deska)
        zmena_hrace()
        
    
    