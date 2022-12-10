class Ficheiro:
    
    # Cores possíveis para pintar o mapa
    Red = "\033[91m"
    Green = "\033[92m"
    Blue = "\033[94m"
    Cyan = "\033[96m"
    White = "\033[97m"
    Yellow = "\033[93m"
    Magenta = "\033[95m"
    Grey = "\033[90m"
    Black = "\033[90m"
    Default = "\033[39m"

    def __init__(self, linhas=0, colunas=0):
        self.linhas = linhas
        self.colunas = colunas
        self.mapa = [] # matriz com os caracteres do mapa

    def calculaLC(self, ficheiro):
        f = open(ficheiro, 'r')
        linhas = f.readlines()
        self.mapa = linhas
        for linha in linhas:
            self.linhas += 1
        linha1 = linhas[0]
        for char in linha1:
            self.colunas += 1
        self.colunas -= 1 # \n
    

    # Mapa colorido com o caminho 
    def printMapaColorido(self, path):
        mapa = {}
        for linha in range(0, self.linhas) :
            for coluna in range (0, self.colunas):
                mapa[(linha, coluna)] = self.mapa[linha][coluna]
        
        nodo_inicial = path.pop(0)
        mapa[(nodo_inicial.m_x, nodo_inicial.m_y)] = self.Green + mapa[(nodo_inicial.m_x, nodo_inicial.m_y)] + self.Default
        nodo_final = path.pop()
        mapa[(nodo_final.m_x, nodo_final.m_y)] = self.Cyan + mapa[(nodo_final.m_x, nodo_final.m_y)] + self.Default

        # Pintar de vermelho os nodos do percurso recebido
        for node in path:
            mapa[(node.m_x, node.m_y)] = self.Red + mapa[(node.m_x, node.m_y)] + self.Default;

        print("")
        for linha in range(0, self.linhas) :
            for coluna in range (0, self.colunas):
                print(mapa[(linha, coluna)], end ="")
            print()
        print()