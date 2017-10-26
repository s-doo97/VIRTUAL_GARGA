"""Fonctions du Simulateur de gargamel"""

__author__ = "Mehdi Laurent"

import psutil
import os
from PIL import Image
from random import randint
import time

garga_out = False

###global hello_nbr
###hello_nbr = 0

garga_salutations = ["Bonjour","Salut","Hello","Hey"]
garga_adieux = ["Salut","Au revoir", "Bye", "À la prochaine"]
garga_not_understanding = ["J'ai pas compris"]

salutations_vocabulary = ["Bonjour","Salut","Hello","Hey","Yo","Oy","Coucou"]
adieux_vocabulary = ["Au revoir","Adieu","À la prochaine","Salut","J'y vais","Je m'en vais","Bye"]

sujets_facheux = ["Juliette","Noemie","Noëmie","Noémie","Gargamelette","Pote à la compote"]

def clear_screen():
    """Nettoie l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_input():
    return str(input("?> "))

def show_all_right():
    """Affiche un Gargamel embarassé."""
    h = Image.open("all_right_garga.png")
    h.show()
    time.sleep(0.7)
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()

def start():
    """Première fonction exectuée au lancement du programme."""
    clear_screen()

    for i in range(3):
        print("$> Initialisation de votre Gargamel virtuel.")
        time.sleep(0.5)
        clear_screen()
        print('$> Initialisation de votre Gargamel virtuel..')
        time.sleep(0.5)
        clear_screen()
        print('$> Initialisation de votre Gargamel virtuel...')
        time.sleep(0.5)
        clear_screen()

    print("$> Initialisation de votre Gargamel virtuel terminée !")
    print("$> Saluez-le donc !")
    print()

def end(num):
    """Dernière fonction à être à priori exécutée par le programme.
    1. Terminaison ordinaire du programme"""
    clear_screen()
    print("$> Votre Gargamel s'en est allé !")
    time.sleep(1)
    clear_screen()


    for i in range(3):
        print("$> Terminaison de la simulation.")
        time.sleep(0.5)
        clear_screen()
        print('$> Terminaison de la simulation..')
        time.sleep(0.5)
        clear_screen()
        print('$> Terminaison de la simulation...')
        time.sleep(0.5)
        clear_screen()

def check_answer(my_input,debut):
    """Analyse les entrés de l'utilisateur et vérifie si elles font parties du
    vocabulaire de Gargamel."""

    garga_out = 0
    understand = False

    garga_out = check_sujets_facheux(my_input)

    understand = check_salutations(my_input,debut)
    ####hello_nbr+=1

    if not garga_out:
        garga_out = check_adieux(my_input,debut)

    #if not garga_out and not understand:
    #    print_not_understanding()

    print()
    return garga_out

def check_salutations(my_input,debut):
    """Analyse de la présence d'un terme saluant."""
    flag = False
    for i in range(len(salutations_vocabulary)):
        if (salutations_vocabulary[i] in my_input or salutations_vocabulary[i].lower() in my_input) and flag == False:
            if not ((my_input=="Salut" or my_input=="salut") and not debut):
                flag = True
                print(garga_salutations[randint(0,len(garga_salutations)-1)],end='')
                if randint(0,1)==1:
                    print(" gros",end='')
                elif randint(0,1)==1:
                    print(" frère",end='')
                print('.')
    return flag

def check_adieux(my_input,debut):
    flag = 0
    for i in range(len(adieux_vocabulary)):
        if (adieux_vocabulary[i] in my_input or adieux_vocabulary[i].lower() in my_input) and flag == 0:
                if debut and (my_input=="Salut" or my_input=="salut"):
                    pass
                else:
                    flag = 1
                    print(garga_adieux[randint(0,len(garga_adieux)-1)],end='')
                    if randint(0,1)==1:
                        print(" gros",end='')
                    elif randint(0,1)==1:
                        print(" frère",end='')
                    print('.')
    if flag:
        time.sleep(0.75)
    return flag


def check_sujets_facheux(my_input):
    """Analyse de la présence d'un sujet facheux."""
    flag = 0
    for i in range(len(sujets_facheux)):
        if (sujets_facheux[i] in my_input or sujets_facheux[i].lower() in my_input) and flag == 0:
            flag = 1
            show_all_right()
            print()
    return flag


def print_not_understanding():
    """Impression dans le cas où l'analyse des entrées de l'utilisateur ne
    ne comprendre rien."""
    print(garga_not_understanding[randint(0,len(garga_not_understanding)-1)]+'.')
    print()
