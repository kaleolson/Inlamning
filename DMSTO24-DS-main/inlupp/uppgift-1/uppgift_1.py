# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(number: int): #-> bool:
    
    return number % 2 == 1

#python -m pytest test_uppgift-1.py
#cd C:\Users\Karl1\Desktop\TUC\Data-Science\Inlamning\DMSTO24-DS-main\inlupp\uppgift-1