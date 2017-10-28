
"""Fonctions du Simulateur de gargamel"""

__author__ = "Mehdi Laurent"

import psutil
import os
from PIL import Image
from random import randint
from time import sleep

import Sel

sel = Sel.Sel()

garga_out = False

garga_humor_lists = ["Normal","Déprimé"]
#garga_humeur = garga_humor_lists[randint(0,len(garga_humor_lists)-1)]
garga_humeur = "Déprimé"
if garga_humeur == "Déprimé":
	sel.sel = 3

garga_salutations = ["Bonjour","Salut","Hello","Hey"]
garga_adieux = ["Salut","Au revoir", "Bye", "À la prochaine"]
garga_not_understanding = ["J'ai pas compris...","Pas compris.","Hein ?", "Hein ?!", "Quoi mec ?","Excuse-moi ?",
                            "Pardon ?", "Sorry ?"]

garga_is_normal = ["Ça va","Ça va, ça va", "Ouais", "Yep", "Oui", "Ouais t'inquiètes"]
garga_is_depressed = ["Non...","Bof...","Mec, ma vie c'est de la merde...","Ma vie, c'est de la merde.",
                    "J'ai envie de me pendre...","Non, j'en ai vraiment marre...","J'en ai assez de la vie..."]

salutations_vocabulary = ["Bonjour","Salut","Hello","Hey","Hé","Yo","Oy","Coucou"]
adieux_vocabulary = ["Au revoir","Adieu","À la prochaine","Salut","J'y vais","Je m'en vais","Bye","À plus"]
how_is_it_vocabulary = ["Ça va","ca va","sa va","Tu vas bien","Tu va bien","Comment tu vas","Comment tu va","Comment vas-tu"
                        "Comment allez-vous","Bien ou quoi"]

sujets_facheux = ["Juliette","Noemie","Noëmie","Noémie","Gargamelette","Pote à la compote"]

good_talking = ["cs", "counter-strike", "biere", "bière"]


def clear_screen():
    """Nettoie l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_input():
    return str(input("?> "))

def show_all_right():
    """Affiche un Gargamel embarassé."""
    h = Image.open("all_right_garga.png")
    h.show()
    sleep(1)
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()

def start():
    """Première fonction exectuée au lancement du programme."""
    clear_screen()

    for i in range(3):
        print("$> Initialisation de votre Gargamel virtuel.")
        sleep(0.5)
        clear_screen()
        print('$> Initialisation de votre Gargamel virtuel..')
        sleep(0.5)
        clear_screen()
        print('$> Initialisation de votre Gargamel virtuel...')
        sleep(0.5)
        clear_screen()

    print("$> Initialisation de votre Gargamel virtuel terminée !")
    sleep(0.5)
    print("$> Saluez-le donc !")
    print()

def end(num):
    """Dernière fonction à être à priori exécutée par le programme.
    1. Terminaison ordinaire du programme"""
    clear_screen()

    print("$> Votre Gargamel s'en est allé !")
    sleep(2.8)
    clear_screen()

    for i in range(3):
        print("$> Terminaison de la simulation.")
        sleep(0.5)
        clear_screen()
        print('$> Terminaison de la simulation..')
        sleep(0.5)
        clear_screen()
        print('$> Terminaison de la simulation...')
        sleep(0.5)
        clear_screen()

def check_answer(my_input,debut):
    """Analyse les entrés de l'utilisateur et vérifie si elles font parties du
    vocabulaire de Gargamel."""

    garga_out = 0
    understand = False

    if check_sujets_facheux(my_input):
    	sel.sel += 10

    understand = check_salutations(my_input,debut)

    if not garga_out:
        understand = check_how_is_it(my_input)

    if not understand and not garga_out:
        garga_out = check_adieux(my_input,debut)
    #if not garga_out and not understand:
    #    print_not_understanding()

    print()
    print("Taux de sel: ", sel)
    if sel.sel >= sel.sel_max:
    	garga_out = True
    	show_all_right()

    return garga_out

def check_salutations(my_input,debut):
    """Analyse de la présence d'un terme saluant."""
    flag = False
    for i in range(len(salutations_vocabulary)):
        if (salutations_vocabulary[i] in my_input or \
        salutations_vocabulary[i].lower() in my_input) and flag == False:
            if not ((my_input=="Salut" or my_input=="salut") and not debut):
                flag = True
                print(garga_salutations[randint(0,len(garga_salutations)-1)],end='')
                if randint(0,1)==1:
                    print(" gros",end='')
                elif randint(0,1)==1:
                    print(" frère",end='')
                elif randint(0,1)==1:
                    print(" mec",end='')
                print('.')
    return flag

def check_how_is_it(my_input):
    """Analyse de présence de termes indiquant le souhait de savoir
    comment va le Gargamel."""

    flag = 0
    for i in range(len(how_is_it_vocabulary)):
        if (how_is_it_vocabulary[i] in my_input or \
        how_is_it_vocabulary[i].lower() in my_input) and flag == 0:
            flag = 1
            if garga_humeur=="Normal":
                print(garga_is_normal[randint(0,len(garga_is_normal)-1)],end='')
                if randint(0,1)==1:
                    print(" frère",end='')
                elif randint(0,1)==1:
                    print(" mec",end='')
                print('.')
            elif garga_humeur=="Déprimé":
                print(garga_is_depressed[randint(0,len(garga_is_normal)-1)]+'.')
    return flag

def check_adieux(my_input,debut):
    """Analyse de la présence d'un terme indiquant la fin de la discussion."""
    flag = 0
    for i in range(len(adieux_vocabulary)):
        if (adieux_vocabulary[i] in my_input or \
        adieux_vocabulary[i].lower() in my_input) and flag == 0:
                if debut and (my_input=="Salut" or my_input=="salut"):
                    pass
                else:
                    flag = 1
                    print(garga_adieux[randint(0,len(garga_adieux)-1)],end='')
                    if randint(0,1)==1:
                        print(" gros",end='')
                    elif randint(0,1)==1:
                        print(" frère",end='')
                    elif randint(0,1)==1:
                        print(" mec",end='')
                    print('.')
    if flag:
        sleep(1.2)
    return flag


def check_sujets_facheux(my_input):
    """Analyse de la présence d'un sujet facheux."""
    flag = 0
    for i in range(len(sujets_facheux)):
        if (sujets_facheux[i] in my_input or \
        sujets_facheux[i].lower() in my_input or \
        sujets_facheux[i].upper() in my_input) and flag == 0:
            flag = 1
    return flag


def print_not_understanding():
    """Impression dans le cas où l'analyse des entrées de l'utilisateur ne
    ne correspant à rien."""
    sel.sel += 1
    print(garga_not_understanding[randint(0,len(garga_not_understanding)-1)]+\
    " (Tu devrais peut-être appendre à écrire...)")
    print()
