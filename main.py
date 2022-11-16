from nodo import Nodo
from grafo import Grafo
import sys


def main():
   
   # ficheiro linhas colunas

    ficheiro = sys.argv[1]
    linhas = int(sys.argv[2])
    colunas = int(sys.argv[3])

    mapa = Mapa(linhas, colunas)

    mapa.parse(ficheiro)

    print(mapa.__str__())


if __name__ == '__main__':
    main()



