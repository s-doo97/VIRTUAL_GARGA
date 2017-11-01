"""Simulateur de Gargamel"""

__author__ = "Mehdi Laurent"

import Garga

def enter_input():
    return str(input("?> "))

if __name__ == "__main__":

    garga = Garga.Garga()

    debut=True

    garga.start()

    while not garga.is_out():
        garga_out = garga.check_answer(enter_input(),debut)
        debut=False

    garga.end(garga_out)

