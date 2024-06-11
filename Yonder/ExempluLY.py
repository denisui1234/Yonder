# test libyonder
from LIBYONDER import calc
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