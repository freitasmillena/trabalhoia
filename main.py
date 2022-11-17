from Mapa import Mapa
from nodo import Nodo
from grafo import Grafo
import sys


def main():
   
   # ficheiro linhas colunas

    ficheiro = "teste.txt" #sys.argv[1]
    linhas = 7 #int(sys.argv[2])
    colunas = 10 #int(sys.argv[3])

    #m = Mapa(linhas, colunas)

    #m.parse(ficheiro)

    #m.expande_grafo()

    #a,b = m.grafo.procura_BFS()

    #print(a,b)

    #Problema: Sobreposição de velocidades D:

    aceleracoes_possiveis = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
    for (aceleracao_x, aceleracao_y) in aceleracoes_possiveis:
        v_final_x = 0 + aceleracao_x
        v_final_y = 0 + aceleracao_y
        nodo_final_x = 3 + v_final_x
        nodo_final_y = 1 + v_final_y
        print("velocidade",v_final_x,v_final_y)
        print("nodo",nodo_final_x,nodo_final_y)
        print("-----------")



if __name__ == '__main__':
    main()



