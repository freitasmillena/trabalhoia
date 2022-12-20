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
        self.diretoria = None

    def calculaLC(self, ficheiro):
        f = open(ficheiro, 'r')
        self.diretoria = ficheiro.split('.')[0]
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
            mapa[(node.m_x, node.m_y)] = self.Red + node.m_char + self.Default

        print("")
        for linha in range(0, self.linhas) :
            for coluna in range (0, self.colunas):
                print(mapa[(linha, coluna)], end ="")
            print()
        print()
    
    def chooseColor(self, i):
        cor = None
        if i == 1:
            cor = self.Red
        elif i == 2:
            cor = self.Green
        elif i == 3:
            cor = self.Magenta
        elif i == 4:
            cor = self.Yellow
        elif i == 5:
            cor = self.Black
        elif i == 6:
            cor = self.Grey 
        elif i == 99: # caminhso cruzaram-se
            cor = self.Cyan
        else: # cor padrão
            cor = self.Default
        return cor


    # Não funciona para mapas com mais do que 6 veículos

    def printMapaCaminhosColoridos(self, paths):
        cor = None
        i = 1

        mapa = {} # mapa com as várias cores de todos os percursos 
        pintado = {} # dicionário que diz se um espaço do mapa está colorido
        cruzamento = {} # diz se dois caminhos se cruzaram num mesmo ponto
        for linha in range(0, self.linhas) :
            for coluna in range (0, self.colunas):
                mapa[(linha, coluna)] = self.mapa[linha][coluna]
                pintado[(linha, coluna)] = False
                cruzamento[(linha, coluna)] = False

        for path in paths:
            cor = self.chooseColor(i)
            for node in path:
                if node.getColisao:
                    mapa[(node.m_x, node.m_y)] = cor + node.m_char + self.Default
                    pintado[(node.m_x, node.m_y)] = True
                if not pintado[(node.m_x, node.m_y)]:
                    mapa[(node.m_x, node.m_y)] = cor + node.m_char + self.Default
                    pintado[(node.m_x, node.m_y)] = True
                elif not cruzamento[(node.m_x, node.m_y)]:
                    mapa[(node.m_x, node.m_y)] = self.Cyan + node.m_char + self.Default
                    cruzamento[(linha, coluna)] = True
            i+=1

        print("\n\n| Mapa com os vários percursos dos veículos coloridos |\n")

        for linha in range(0, self.linhas) :
            for coluna in range (0, self.colunas):
                print(mapa[(linha, coluna)], end ="")
            print()
        print()