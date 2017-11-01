"""Fichier test du simulateur de Gargamel"""

__author__ = "Dorian Hoet"

import Garga

from time import sleep

def enter_input():
    return str(input("?> "))

if __name__ == "__main__":

    garga = Garga.Garga()

    debut=True

    garga.start()

    print("<- salut")
    sleep(0.5)
    print("-> ", end = "")
    garga_out = garga.check_answer("salut",debut)
    sleep(2)
    debut=False

    checklist = ["ca va?", "cs", "au revoir"]

    for mots in checklist:
        print("\n<- " + mots)
        sleep(0.5)
        print("-> ", end = "")
        garga_out = garga.check_answer(mots, debut)
        sleep(2)

    sleep(4)

    garga.end(garga_out)

