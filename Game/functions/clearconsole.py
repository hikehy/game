import os
import platform

def clearconsole():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
