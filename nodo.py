
# Classe Node para definiçao dos nodos
# Cada nodo possui coordenadas x e y, bem como o caracter que representa e a heurística

class Nodo:
    def __init__(self, x, y, char):
        self.m_x = x
        self.m_y = y
        self.m_char = char

    def __str__(self):
        return "(" + str(self.m_x) + "," + str(self.m_y) + ")"

    def __repr__(self):
        return self.m_char +  " (" + str(self.m_x) + "," + str(self.m_y) + ")"

    def getX(self):
        return self.m_x

    def getY(self):
        return self.m_y

    def getChar(self):
        return self.m_char

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.m_x == other.m_x and self.m_y == other.m_y  # são iguais se coords forem iguais

    def __hash__(self):
        return hash(self.m_x*0.5 + self.m_y*0.25)
