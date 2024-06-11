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