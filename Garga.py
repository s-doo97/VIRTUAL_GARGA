
"""Fonctions du Simulateur de gargamel"""

__author__ = "Mehdi Laurent"

import psutil
import os
from PIL import Image
from random import randint
from time import sleep

import Sel

class Garga:
    def __init__(self):
        self.sel = Sel.Sel()

        self.garga_out = False

        self.garga_humor_lists = ["Normal","Déprimé"]
        self.garga_humeur = self.garga_humor_lists[randint(0,len(self.garga_humor_lists)-1)]
        self.garga_humeur = "Déprimé"
        if self.garga_humeur == "Déprimé":
            self.sel.sel = 3

        self.garga_salutations = ["Bonjour","Salut","Hello","Hey"]
        self.garga_adieux = ["Salut","Au revoir", "Bye", "À la prochaine"]
        self.garga_not_understanding = ["J'ai pas compris...","Pas compris.","Hein ?", "Hein ?!", "Quoi mec ?","Excuse-moi ?",
                                    "Pardon ?", "Sorry ?"]
        self.garga_jouissance = ["Trop bi1 mac!", "stylé", "swagg", "HHooo whaw, trop bon"]

        self.garga_is_normal = ["Ça va","Ça va, ça va", "Ouais", "Yep", "Oui", "Ouais t'inquiètes"]
        self.garga_is_depressed = ["Non...","Bof...","Mec, ma vie c'est de la merde...","Ma vie, c'est de la merde.",
                            "J'ai envie de me pendre...","Non, j'en ai vraiment marre...","J'en ai assez de la vie..."]

        self.salutations_vocabulary = ["Bonjour","Salut","Hello","Hey","Hé","Yo","Oy","Coucou"]
        self.adieux_vocabulary = ["Au revoir","Adieu","À la prochaine","Salut","J'y vais","Je m'en vais","Bye","À plus"]
        self.how_is_it_vocabulary = ["Ça va","ca va","sa va","Tu vas bien","Tu va bien","Comment tu vas","Comment tu va","Comment vas-tu"
                                "Comment allez-vous","Bien ou quoi"]

        self.sujets_facheux = ["Juliette","Noemie","Noëmie","Noémie","Gargamelette","Pote à la compote"]

        self.good_talking = ["cs", "counter-strike", "biere", "bière"]

    def is_out(self):
        return self.garga_out

    def clear_screen(self):
        """Nettoie l'écran."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def enter_input(self):
        return str(input("?> "))

    def show_all_right(self):
        """Affiche un Gargamel embarassé."""
        h = Image.open("all_right_garga.png")
        h.show()
        sleep(1)
        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()

    def start(self):
        """Première fonction exectuée au lancement du programme."""
        self.clear_screen()

        for i in range(3):
            print("$> Initialisation de votre Gargamel virtuel.")
            sleep(0.5)
            self.clear_screen()
            print('$> Initialisation de votre Gargamel virtuel..')
            sleep(0.5)
            self.clear_screen()
            print('$> Initialisation de votre Gargamel virtuel...')
            sleep(0.5)
            self.clear_screen()

        print("$> Initialisation de votre Gargamel virtuel terminée !")
        sleep(0.5)
        print("$> Saluez-le donc !")
        print()

    def end(self, num):
        """Dernière fonction à être à priori exécutée par le programme.
        1. Terminaison ordinaire du programme"""
        self.clear_screen()

        print("$> Votre Gargamel s'en est allé !")
        sleep(2.8)
        self.clear_screen()

        for i in range(3):
            print("$> Terminaison de la simulation.")
            sleep(0.5)
            self.clear_screen()
            print('$> Terminaison de la simulation..')
            sleep(0.5)
            self.clear_screen()
            print('$> Terminaison de la simulation...')
            sleep(0.5)
            self.clear_screen()

    def check_answer(self, my_input,debut):
        """Analyse les entrés de l'utilisateur et vérifie si elles font parties du
        vocabulaire de Gargamel."""

        self.garga_out = 0
        self.understand = False

        if self.check_sujets_facheux(my_input):
            self.sel.sel += 4
            self.understand = True

        elif self.check_salutations(my_input,debut):
            self.understand = True

        elif self.check_how_is_it(my_input):
            self.understand = True

        elif self.check_adieux(my_input,debut):
            self.garga_out = True
            self.understand = True

        elif self.check_good_talking(my_input):
            self.understand = True
            self.sel.sel -= 1

        else:
            self.print_not_understanding()
            self.sel.sel += 1

        print()
        print("Taux de sel: ", self.sel)
        if self.sel.sel >= self.sel.sel_max:
            self.garga_out = True
            self.show_all_right()

        return self.garga_out

    def check_good_talking(self, my_input):
        """ Analyse de la présence d'un terme saluant
        """
        flag = False
        for mot in self.good_talking:
            if mot in my_input.lower():
                flag = True
                print(self.garga_jouissance[ randint(0, len(self.garga_jouissance)-1) ])
        return flag

    def check_salutations(self, my_input, debut):
        """Analyse de la présence d'un terme saluant."""
        flag = False
        for i in range(len(self.salutations_vocabulary)):
            if (self.salutations_vocabulary[i] in my_input or \
            self.salutations_vocabulary[i].lower() in my_input) and flag == False:
                if not ((my_input=="Salut" or my_input=="salut") and not debut):
                    flag = True
                    print(self.garga_salutations[randint(0,len(self.garga_salutations)-1)],end='')
                    if randint(0,1)==1:
                        print(" gros",end='')
                    elif randint(0,1)==1:
                        print(" frère",end='')
                    elif randint(0,1)==1:
                        print(" mec",end='')
                    print('.')
        return flag

    def check_how_is_it(self, my_input):
        """Analyse de présence de termes indiquant le souhait de savoir
        comment va le Gargamel."""

        flag = 0
        for i in range(len(self.how_is_it_vocabulary)):
            if (self.how_is_it_vocabulary[i] in my_input or \
            self.how_is_it_vocabulary[i].lower() in my_input) and flag == 0:
                flag = 1
                if self.garga_humeur=="Normal":
                    print(self.garga_is_normal[randint(0,len(self.garga_is_normal)-1)],end='')
                    if randint(0,1)==1:
                        print(" frère",end='')
                    elif randint(0,1)==1:
                        print(" mec",end='')
                    print('.')
                elif self.garga_humeur=="Déprimé":
                    print(self.garga_is_depressed[randint(0,len(self.garga_is_normal)-1)]+'.')
        return flag

    def check_adieux(self, my_input,debut):
        """Analyse de la présence d'un terme indiquant la fin de la discussion."""
        flag = 0
        for i in range(len(self.adieux_vocabulary)):
            if (self.adieux_vocabulary[i] in my_input or \
            self.adieux_vocabulary[i].lower() in my_input) and flag == 0:
                    if debut and (my_input=="Salut" or my_input=="salut"):
                        pass
                    else:
                        flag = 1
                        print(self.garga_adieux[randint(0,len(self.garga_adieux)-1)],end='')
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


    def check_sujets_facheux(self, my_input):
        """Analyse de la présence d'un sujet facheux."""
        flag = 0
        for i in range(len(self.sujets_facheux)):
            if (self.sujets_facheux[i] in my_input or \
            self.sujets_facheux[i].lower() in my_input or \
            self.sujets_facheux[i].upper() in my_input) and flag == 0:
                flag = 1
        return flag


    def print_not_understanding(self):
        """Impression dans le cas où l'analyse des entrées de l'utilisateur ne
        ne correspant à rien."""
        print(self.garga_not_understanding[randint(0,len(self.garga_not_understanding)-1)]+\
        " (Tu devrais peut-être appendre à écrire...)")
        print()
