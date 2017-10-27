"""Simulateur de Gargamel"""

__author__ = "Mehdi Laurent"

import Garga

def enter_input():
    return str(input("?> "))

if __name__ == "__main__":

    garga_out = False
    debut=True

    Garga.start()

    while not garga_out:
        garga_out = Garga.check_answer(enter_input(),debut)
        debut=False

    Garga.end(garga_out)
