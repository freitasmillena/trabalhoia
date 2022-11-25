from Mapa import Mapa
from nodo import Nodo
from grafo import Grafo
import sys
import os
from ficheiro import Ficheiro
import pickle

# recebe como argumento o ficheiro
def main():

   path_ficheiro = sys.argv[1]

   nome_ficheiro = path_ficheiro.split('.')[0]
   bin_ficheiro = nome_ficheiro + ".bin"
   isExist = os.path.exists(bin_ficheiro)

   m = None

   if isExist :
      file = open(bin_ficheiro, 'rb')
      m = pickle.load(file)
      file.close()

   else:
      ficheiro = Ficheiro()
      # calcula o número de linhas e colunas do ficheiro
      ficheiro.calculaLC(path_ficheiro) 
      linhas = ficheiro.linhas
      colunas = ficheiro.colunas

      m = Mapa(linhas, colunas)
      m.parse(path_ficheiro)
      m.expande_grafo()
      m.grafo.add_heuristica()

      file = open(bin_ficheiro, 'wb')
      pickle.dump(m, file)
      file.close()


   saida = -1

   # menu de opções
   while saida != 0:
      print("")
      print("1-Desenhar Grafo do Mapa")
      print("2-Desenhar Grafo da Expansão")
      print("3-DFS")
      print("4-BFS")
      print("5-A-star")
      print("6-Greedy")
      print("0-Sair")

      saida = int(input("introduza a sua opcao-> "))
      if saida == 0:
         print("saindo.......")
      elif saida == 1:
         m.grafo_mapa.desenha()
         l=input("prima enter para continuar")
      elif saida == 2:
         m.grafo.desenha()
         l = input("prima enter para continuar")
      elif saida == 3:
         resultDFS, custoTotalDFS = m.grafo.procura_DFS(m.grafo.nodo_inicial)
         print("Resultado: " + str(resultDFS) + "\nCusto: " + str(custoTotalDFS))
         resultDFSExpand, timeDFS = m.expande_caminho(resultDFS)
         print("Resultado expandido: " + str(resultDFSExpand) + "\nTempo: " + str(timeDFS))
         l = input("prima enter para continuar")
      elif saida == 4:
         resultBFS, custoTotalBFS = m.grafo.procura_BFS()
         print("Resultado: " + str(resultBFS) + "\nCusto: " + str(custoTotalBFS))
         resultBFSExpand, timeBFS = m.expande_caminho(resultBFS)
         print("Resultado expandido: " + str(resultBFSExpand) + "\nTempo: " + str(timeBFS))
         l = input("prima enter para continuar")
      elif saida == 5:
         resultAStar, custoTotalAStar = m.grafo.procura_aStar()
         print("Resultado: " + str(resultAStar) + "\nCusto: " + str(custoTotalAStar))
         resultAStarExpand, timeAStar = m.expande_caminho(resultAStar)
         print("Resultado expandido: " + str(resultAStarExpand) + "\nTempo: " + str(timeAStar))
         l = input("prima enter para continuar")
      elif saida == 6:
         resultGreedy, custoTotalGreedy = m.grafo.greedy()
         print("Resultado: " + str(resultGreedy) + "\nCusto: " + str(custoTotalGreedy))
         resultGreedyExpand, timeGreedy = m.expande_caminho(resultGreedy)
         print("Resultado expandido: " + str(resultGreedyExpand) + "\nTempo: " + str(timeGreedy))
         l = input("prima enter para continuar")      
      else:
         print("you didn't add anything")
         l = input("prima enter para continuar")


if __name__ == '__main__':
    main()



