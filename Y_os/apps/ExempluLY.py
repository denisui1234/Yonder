# test libyonder
from LIBYONDER import calc, open_credits
import time
print('Exemplu 1. Calculator')
#Alegere numere
a = int(input("Număr a= "))
b = int(input("Număr b= "))
f = open('cont.txt', 'r')
#citire opțiuni si printează
def eread():
    file_contents = f.read()
    print(file_contents)
    file_contents = f.read()
eread()
tip = input('Introdu operație: ')
#Calcul cu tip si a b
v = calc(tip)
if v:
    v(a,b)
time.sleep(1)
print('Exemplu 2. Credite')
open_credits()
p = input('Enter ca să continui')
 

