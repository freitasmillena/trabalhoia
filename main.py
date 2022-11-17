from Mapa import Mapa
from nodo import Nodo
from grafo import Grafo
import sys


def main():
   
   # ficheiro linhas colunas

   ficheiro = "teste.txt" #sys.argv[1]
   linhas = 7 #int(sys.argv[2])
   colunas = 10 #int(sys.argv[3])

   # A incialização da estrtura Grafo só vai servir para algoritmos de pesquisa NÃO INFORMADA
   # Isto acontece porque neste tipo de algoritmos, não se considera a velocidade e acelração do veículo
   grafo = Grafo ()
   grafo.parse("teste.txt", False)
   grafo.add_heuristica()

   # Mapa só pode ser utilizado para algoritmos   grafo = Grafo ()
   grafo_mapa = Grafo ()
   grafo_mapa.parse("teste.txt", True)
   grafo_mapa.add_heuristica()
   m = Mapa(linhas, colunas, grafo)
   m.parse(ficheiro)
   #m.expande_grafo()

   saida = -1

   while saida != 0:
      print("")
      print("1-Imprimir Grafo")
      print("2-Imprimir Nodos do Grafo")
      print("3-BFS")
      print("4-A-star")
      print("0-Sair")

      saida = int(input("introduza a sua opcao-> "))
      if saida == 0:
         print("saindo.......")
      elif saida == 1:
         print(grafo.m_grafo)
         l=input("prima enter para continuar")
      elif saida == 2:
         print(grafo.m_grafo.keys())
         l = input("prima enter para continuar")
      elif saida == 3:
         resultBFS, custoTotalBFS = grafo.procura_BFS()
         print(resultBFS, custoTotalBFS)
         l = input("prima enter para continuar")
      elif saida == 4:
         resultAStar, custoTotalAStar = m.grafo.procura_aStar(m)
         print(resultAStar, custoTotalAStar)
         l = input("prima enter para continuar")
      else:
         print("you didn't add anything")
         l = input("prima enter para continuar")



if __name__ == '__main__':
    main()



