class Ficheiro:
    
    def __init__(self, linhas=0, colunas=0):
        self.linhas = linhas
        self.colunas = colunas

    def calculaLC(self, ficheiro):
        f = open(ficheiro, 'r')
        linhas = f.readlines()
        for linha in linhas:
            self.linhas += 1
        linha1 = linhas[0]
        for char in linha1:
            self.colunas += 1
        self.colunas -= 1 # \n