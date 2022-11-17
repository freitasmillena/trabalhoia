from grafo import Grafo
from nodo import Nodo


class Mapa:

    def __init__(self, l, c, grafo):
        self.xPartida = None
        self.yPartida = None
        self.listaObjetivo = []
        self.linhas = l
        self.colunas = c
        self.mapa = [[0 for x in range(self.colunas)] for y in range(self.linhas)]
        self.grafo = grafo

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
                n1 = Nodo(x, y, char, True)
                if char != '\n':
                    self.mapa[x][y] = n1
                if char == 'P':
                    self.xPartida = x
                    self.yPartida = y
                if char == 'F':
                    self.listaObjetivo.append(n1)
                y += 1
            y = 0
            x += 1

    # Cálculo do nodo anterior a um X, vendo que a velocidade segue primeiro a linha, e depois a coluna
    def linhaColuna(self, nodo, nodo_final_x, nodo_final_y, v_final_x, v_final_y):
        # Como só pode ser inserido um dos dois custos (25 ou 1), é melhor criar um booleano que indica se encontrou algum X
        obstaculo = False

        custo_final = 0
        x = nodo.m_x
        ant = x
        while x != nodo_final_x:
            ant = x
            if x < nodo_final_x:
                x += 1
            else:
                x -= 1
            if self.mapa[x][nodo.m_y].m_char == 'X':
                nodo_final_x = ant
                v_final_x = 0
                v_final_y = 0
                if obstaculo == False :
                    custo_final += 25
                    obstaculo = True
                break
            else:
                custo_final += 1

        y = nodo.m_y
        while y != nodo_final_y:
            ant = y
            if y < nodo_final_y:
                y += 1
            else:
                y -= 1
            if self.mapa[nodo_final_x][y].m_char == 'X':
                nodo_final_y = ant
                v_final_x = 0
                v_final_y = 0
                if obstaculo == False :
                    custo_final += 25
                    obstaculo = True
                break
            else:
                custo_final += 1

        nodo_opt1 = self.mapa[nodo_final_x][nodo_final_y]
        nodo_opt1.v_x = v_final_x
        nodo_opt1.v_y = v_final_y
        return nodo_opt1,custo_final


    def colunaLinha(self, nodo, nodo_final_x, nodo_final_y, v_final_x, v_final_y):
        # Como só pode ser inserido um dos dois custos (25 ou 1), é melhor criar um booleano que indica se encontrou algum X
        obstaculo = False
        
        custo_final = 0
        y = nodo.m_y
        while y != nodo_final_y:
            ant = y
            if y < nodo_final_y:
                y += 1
            else:
                y -= 1
            if self.mapa[nodo_final_x][y].m_char == 'X':
                nodo_final_y = ant
                v_final_x = 0
                v_final_y = 0
                if obstaculo == False :
                    custo_final += 25
                    obstaculo = True
                break
            else:
                custo_final += 1
        
        x = nodo.m_x
        while x != nodo_final_x:
            ant = x
            if x < nodo_final_x:
                x += 1
            else:
                x -= 1
            if self.mapa[x][nodo.m_y].m_char == 'X':
                nodo_final_x = ant
                v_final_x = 0
                v_final_y = 0
                if obstaculo == False :
                    custo_final += 25
                    obstaculo = True
                break
            else:
                custo_final += 1

        nodo_opt1 = self.mapa[nodo_final_x][nodo_final_y]
        nodo_opt1.v_x = v_final_x
        nodo_opt1.v_y = v_final_y
        return nodo_opt1, custo_final

    def nove(self, nodo):
        aceleracoes_possiveis = None
        if nodo.v_x == 0 and nodo.v_y == 0 :
            aceleracoes_possiveis = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
        else:
            aceleracoes_possiveis = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
        nodos_resultado = []
        for (aceleracao_x, aceleracao_y) in aceleracoes_possiveis:
            v_final_x = nodo.v_x + aceleracao_x
            v_final_y = nodo.v_y + aceleracao_y
            nodo_final_x = nodo.m_x + v_final_x
            nodo_final_y = nodo.m_y + v_final_y

            if 0 <= nodo_final_x < self.linhas and 0 <= nodo_final_y < self.colunas and self.mapa[nodo_final_x][nodo_final_y].m_char != 'P':
                (n1,c1) = self.linhaColuna(nodo, nodo_final_x, nodo_final_y, v_final_x, v_final_y)
                (n2,c2) = self.colunaLinha(nodo, nodo_final_x, nodo_final_y, v_final_x, v_final_y)

                if c1 <= c2:
                    nodos_resultado.append((n1, c1))
                    # self.grafo.add_aresta(nodo, n1, c1)
                else:
                    nodos_resultado.append((n2, c2))
                    # self.grafo.add_aresta(nodo, n2, c2)

        return nodos_resultado

    '''
    def expande_grafo(self):
        self.grafo.m_nodos_objetivos = self.listaObjetivo
        nodos_visitados = set()
        nodos_a_visitar = []
        nodo_partida = self.mapa[self.xPartida][self.yPartida]
        self.grafo.nodo_inicial = nodo_partida
        nodos_a_visitar.append(nodo_partida)
        # print(nodo_partida)
        while (nodos_a_visitar):
            nodo_atual = nodos_a_visitar.pop()
            if nodo_atual not in nodos_visitados:

                nodo_resultado = self.nove(nodo_atual)

                for nodo in nodo_resultado:
                    nodos_a_visitar.append(nodo)

                nodos_visitados.add(nodo_atual)

        self.grafo.add_heuristica()
        # print(nodo_partida)
    '''