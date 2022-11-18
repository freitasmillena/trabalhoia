import math
from queue import Queue

# import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
# import matplotlib.pyplot as plt  # idem

from nodo import Nodo


class Grafo:

    def __init__(self):
        self.m_nodos = []
        self.nodo_inicial = None
        self.m_grafo = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para posteriormente armazenar as heuristicas para cada nodo -> pesquisa informada
        self.m_nodos_objetivos = []

    ################################
    # Escrever o grafo como string #
    ################################
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

        # self.m_grafo[nodo2].add((nodo1, custo)) -> confirmar se é direcionado ou não direcionado

    def charCusto(self, char1, char2):
        if char1 == "X" or char2 == "X":
            return 25
        else:
            return 1

    '''
    def parse(self, ficheiro, bool_mapa):
        x = 0
        y = 0
        f = open(ficheiro, 'r')
        aux = {}
        linhas = f.readlines()
        for linha in linhas:
            for char in linha:
                if char != '\n':
                    aux[(x, y)] = char
                    n2 = Nodo(x, y, char, bool_mapa)
                    if x - 1 >= 0:
                        n1 = Nodo(x - 1, y, aux[(x - 1, y)], bool_mapa)
                        custo = self.charCusto(aux[(x - 1, y)], char)
                        self.add_aresta(n1, n2, custo)
                    if y - 1 >= 0:
                        n1 = Nodo(x, y - 1, aux[(x, y - 1)], bool_mapa)
                        custo = self.charCusto(aux[(x, y - 1)], char)
                        self.add_aresta(n1, n2, custo)
                    if char == 'F':  # and n2 not in self.m_nodos_objetivos
                        self.m_nodos_objetivos.append(n2)
                    elif char == 'P':
                        self.nodo_inicial = n2
                y += 1
            y = 0
            x += 1
    '''

    ####################################
    # Calcular Distâncias de Manhattan #
    ####################################

    def distManhattan(self, nodo):
        dist_menor = math.inf
        for (x, y) in self.m_nodos_objetivos:
            aux = abs(x - nodo.m_x) + abs(y - nodo.m_y)
            if aux < dist_menor:
                dist_menor = aux
        return dist_menor

        ##############

    # Heuristica #
    ##############

    def add_heuristica(self):
        for nodo in self.m_nodos:
            self.m_h[nodo] = self.distManhattan(nodo)

    ##################################
    # Devolver o custo de uma aresta #
    ##################################

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_grafo[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo
        return custoT

    ########################################
    #  Dado um caminho calcula o seu custo #
    ########################################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            # print(teste[i])
            i = i + 1
        return custo

    def nodoCoords(self, nodo):
        return nodo.m_x, nodo.m_y

    '''
    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()
    '''

    #########################
    # Algoritmos de Procura #
    #########################

    ###############
    # Procura BFS #
    ###############

    # Neste algoritmo, ignoram-se os 'X'
    def procura_BFS(self):
        # definir nodo final
        nodo_objetivo_final = None

        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(self.nodo_inicial)
        visited.add(self.nodo_inicial)

        # garantir que o inicial node nao tem pais...
        parent = dict()
        parent[self.nodo_inicial] = None

        path_found = False
        while not fila.empty() and path_found == False:
            # print("visitou")
            nodo_atual = fila.get()
            # print(nodo_atual)
            if self.nodoCoords(nodo_atual) in self.m_nodos_objetivos:
                path_found = True
                nodo_objetivo_final = nodo_atual
            else:
                for (adjacente, custo) in self.m_grafo[nodo_atual]:
                    # print(adjacente)
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        # Reconstruir o caminho

        path = []
        if path_found:
            path.append(nodo_objetivo_final)
            while parent[nodo_objetivo_final] is not None:
                path.append(parent[nodo_objetivo_final])
                nodo_objetivo_final = parent[nodo_objetivo_final]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
            # print("chegou")
            return (path, custo)
        else:
            return (path, 0)

    #####################################################
    # Função   getAdjacentes, devolve vizinhos de um nó #
    #####################################################

    def getAdjacentes(self, nodo):
        #  - Versão Antiga -
        lista = []
        for (adjacente, custo) in self.m_grafo[nodo]:
            lista.append((adjacente, custo))

        # lista = mapa.nove(nodo)
        # print(lista)
        return lista

    ##############################
    # devolve heuristica do nodo #
    ##############################

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            print(nodo)
            return math.inf
        else:
            return self.m_h[nodo]

    def calcula_est(self, estima):
        l = list(estima.keys())
        min_estima = estima[l[0]]
        node = l[0]
        for k, v in estima.items():
            if v < min_estima:
                min_estima = v
                node = k
        return node

    ##################################
    # Devolver o custo de uma aresta #
    ##################################

    def get_arc_cost_AStar(self, node1, node2):
        custoT = math.inf
        a = self.m_grafoAStar[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo
        return custoT

    ########################################
    #  Dado um caminho calcula o seu custo #
    ########################################

    def calcula_custo_AStar(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost_AStar(teste[i], teste[i + 1])
            # print(teste[i])
            i = i + 1
        return custo

    ############
    #    A*    #
    ############

    def procura_aStar(self):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {self.nodo_inicial}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[self.nodo_inicial] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[self.nodo_inicial] = self.nodo_inicial
        n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            calc_heurist = {}
            flag = 0
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.getH(v)
            if flag == 1:
                min_estima = self.calcula_est(calc_heurist)
                n = min_estima
            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructing the path from it to the inicial_node
            if self.nodoCoords(n) in self.m_nodos_objetivos:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(self.nodo_inicial)

                reconst_path.reverse()

                # print('Path found: {}'.format(reconst_path))
                return reconst_path, self.calcula_custo(reconst_path)

            # for all neighbors of the current node do
            for (m, weight) in self.getAdjacentes(n):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    # self.m_grafoAStar[n].add((m, weight))
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    # print(str(g[n]) + " " + n.getChar() + " " + m.getChar())
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        # self.m_grafoAStar[n].add((m, weight))

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
