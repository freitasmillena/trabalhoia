import math
from queue import Queue

# import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
# import matplotlib.pyplot as plt  # idem

from nodo import Nodo


class Grafo:

    def __init__(self):
        self.m_nodos = []
        self.m_grafo = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para posterirmente armazenar as heuristicas para cada nodo -< pesquisa informada

    #############
    # Escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_grafo.keys():
            out = out + "nodo" + str(key) + ": " + str(self.m_grafo[key]) + "\n"
        return out

    def add_aresta(self, nodo1, nodo2, custo):

        if nodo1 not in self.m_nodos:
            self.m_nodos.append(nodo1)
            self.m_grafo[nodo1] = set()

        if nodo2 not in self.m_nodos:
            self.m_nodos.append(nodo2)
            self.m_grafo[nodo2] = set()

        self.m_grafo[nodo1].add((nodo2, custo))

        self.m_grafo[nodo2].add((nodo1, custo))

    def charCusto(self,  char1, char2):
        if char1 == "X" or char2 == "X":
            return 25
        else: return 1

    def parse(self, ficheiro):
        x = 0
        y = 0
        f = open(ficheiro, 'r')
        aux = {}
        linhas = f.readlines()
        for linha in linhas:
            for char in linha:
                if char != "\n":
                    aux[(x,y)] = char
                    if x - 1 >= 0:
                        n1 = Nodo(x-1, y, aux[(x-1,y)])
                        n2 = Nodo(x, y , char)
                        custo = self.charCusto(aux[(x-1,y)],char)
                        self.add_aresta(n1, n2, custo)
                    if y - 1 >= 0:
                        n1 = Nodo(x, y - 1, aux[(x, y - 1)])
                        n2 = Nodo(x, y, char)
                        custo = self.charCusto(aux[(x, y - 1)], char)
                        self.add_aresta(n1, n2, custo)
                y += 1
            y = 0
            x += 1