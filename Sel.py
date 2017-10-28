"""Classe Sel du Simulateur de Gargamel"""

class Sel:
    """
        Classe représentant le taux de sel de Gargamel
    """
    def __init__(self):
        self.sel = 0
        self.sel_max = 10

    def __str__(self):
        """ Renvoie une jauge de sel
        """
        if self.sel > self.sel_max:
            self.sel = self.sel_max

        return "[" + self.sel*"*" + (self.sel_max - self.sel)*" " + "]"

    def __iadd__(self, a):
        self.sel += a

    def __isub__(self, a):
        self.sel -= a