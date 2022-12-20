# Classe Node para definiçao dos nodos
# Cada nodo possui coordenadas x e y, bem como o caracter que representa e a heurística

class Nodo:
    def __init__(self, x, y, char, vx=0, vy=0, ax=0, ay=0, t=None, colisao = False):
        self.m_x = x
        self.m_y = y
        self.m_char = char
        self.v_x = vx
        self.v_y = vy
        self.a_x = ax
        self.a_y = ay
        self.trajetoria = t
        self.colisao = colisao

    def __str__(self):
        return self.m_char + " (" + str(self.m_x) + "," + str(self.m_y) + ")"

    def __repr__(self):
        string = "\n" + self.m_char + " p(" + str(self.m_x) + "," + str(self.m_y) + ") " + " v(" + str(self.v_x) + "," + str(self.v_y) + ") " + " a(" + str(self.a_x) + "," + str(self.a_y) + ")"
        return string

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
            return self.m_x == other.m_x and self.m_y == other.m_y and self.v_x == other.v_x and self.v_y == other.v_y

    def __hash__(self):
        return hash(self.m_x * 0.5 + self.m_y * 0.25 + self.v_x * 0.25 + self.v_y * 0.33)
    
    def getColisao(self):
        return self.colisao
