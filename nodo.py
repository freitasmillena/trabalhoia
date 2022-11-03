
# Classe Node para definiçao dos nodos
# Cada nodo possui coordenadas x e y, bem como o caracter que representa e a heurística

class Node:
    def __init__(self, x, y, char):
        self.m_x = x
        self.m_y = y
        self.m_char = char
        self.m_h = 0 #heuristica no nodo ou fora?

    def __str__(self):
        return "Node: " + self.m_char + " Coords: " + "(" + str(self.m_x) + "," + str(self.m_y) + ")"

    def __repr__(self):
        return "Node: " + self.m_char + " Coords: " + "(" + str(self.m_x) + "," + str(self.m_y) + ")"

    def getX(self):
        return self.m_x

    def getY(self):
        return self.m_y

    def getChar(self):
        return self.m_char

    def setH(self, h):
        self.m_h = h

    def __eq__(self, other):
        return self.m_x == other.m_x and self.m_y == other.m_y  # são iguais se coords forem iguais

    def __hash__(self):
        return hash(self.m_x*0.5 + self.m_y*0.25)
