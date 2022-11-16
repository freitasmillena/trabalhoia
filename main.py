from Mapa import Mapa
from nodo import Nodo
from grafo import Grafo
import sys


def main():
   
   # ficheiro linhas colunas

    ficheiro = "teste.txt" #sys.argv[1]
    linhas = 7 #int(sys.argv[2])
    colunas = 10 #int(sys.argv[3])

    m = Mapa(linhas, colunas)

    m.parse(ficheiro)

    m.expande_grafo()

    a,b = m.grafo.procura_BFS()

    print(a,b)


if __name__ == '__main__':
    main()



