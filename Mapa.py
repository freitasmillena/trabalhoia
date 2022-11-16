from nodo import Nodo


class Mapa:

    def __init__(self, l, c):
        self.xPartida = None
        self.yPartida = None
        self.listaObjetivo = []
        self.linhas = l
        self.colunas = c
        self.mapa = [[0 for x in range(self.colunas)] for y in range(self.linhas)]

    def __str__(self):
        out = ""
        for i in range(self.linhas):
            for j in range(self.colunas):
                out = out + self.mapa[i][j].__str__()
            out = out + "\n"

        return out

    def parse(self, ficheiro):
        x = 0
        y = 0
        f = open(ficheiro, 'r')
        linhas = f.readlines()
        for linha in linhas:
            for char in linha:
                if char != '\n':
                    n1 = Nodo(x, y, char)
                    self.mapa[x][y] = n1
                if char == 'P':
                    self.xPartida = x
                    self.yPartida = y
                if char == 'F':
                    self.listaObjetivo.append((x, y))  # qualquer coisa muda-se depois
                y += 1
            y = 0
            x += 1
