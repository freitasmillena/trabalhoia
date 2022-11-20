from Mapa import Mapa
from nodo import Nodo
from grafo import Grafo
import sys
from ficheiro import Ficheiro

def main():
   
   # ficheiro linhas colunas
   path_ficheiro = sys.argv[1]
   #print(path_ficheiro)
   ficheiro = Ficheiro()
   ficheiro.calculaLC(path_ficheiro)
   linhas = ficheiro.linhas #int(sys.argv[2])
   colunas = ficheiro.colunas #30 #int(sys.argv[3])
   #print(linhas, colunas)

   # A incialização da estrtura Grafo só vai servir para algoritmos de pesquisa NÃO INFORMADA
   # Isto acontece porque neste tipo de algoritmos, não se considera a velocidade e acelração do veículo
   '''
   grafo = Grafo ()
   grafo.parse("teste.txt", False)
   grafo.add_heuristica()
   '''

   # Mapa só pode ser utilizado para algoritmos   grafo = Grafo ()
   # grafo_mapa = Grafo ()
   # grafo_mapa.parse("teste.txt", True)
   # grafo_mapa.add_heuristica()

   m = Mapa(linhas, colunas)
   m.parse(path_ficheiro)
   m.expande_grafo()
   m.grafo.add_heuristica()


   saida = -1

   while saida != 0:
      print("")
      print("1-Desenhar Grafo")
      print("2-Imprimir Nodos do Grafo")
      print("3-DFS")
      print("4-BFS")
      print("5-A-star")
      print("6-Greedy")
      print("0-Sair")

      saida = int(input("introduza a sua opcao-> "))
      if saida == 0:
         print("saindo.......")
      elif saida == 1:
         m.grafo.desenha()
         l=input("prima enter para continuar")
      elif saida == 2:
         print(m.grafo.m_nodos)
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



