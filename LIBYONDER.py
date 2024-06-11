#LIBYONDER
import os
from PyQt5 import QtWidgets

def start():
    if os.path.isdir("data"):
        print('Pornire Yonder OS')
        exec(open("/Y_os/main.py").read())
def calc(type):
    def add(a,b):
        print(a+b)
    
    def multiply(a,b):
        print(a*b)
    
    def divide(a,b):
        print(a/b)
    
    def power(a,b):
        print(a**b)
    def subtract(a,b):
        print(a-b)
    if type == 'add':
        return add
    elif type == 'multiply':
        return multiply
    elif type == 'divide':
        return divide
    elif type == 'power':
        return power
    elif type == 'subtract':
        return subtract
    else:
        return None
def open_credits():
    Credits = [
        'Dezvoltat de Yonder Group '
        'Librării folosite: os '
        'Libyonder 0.1 '
        'Turrón? Turrón? Turrón! '
        'Turrón, cunoscut și sub numele de torró sau torrone, este o confecție de nuga originară din sud-vestul Europei și Maroc. Se prepară în mod tradițional din miere, zahăr și albuș de ou, cu migdale prăjite sau alte nuci, și are de obicei formă de tabletă dreptunghiulară sau prăjitură rotundă.'
    ]
    print(Credits)
