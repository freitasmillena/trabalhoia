import time
from Mapa import Mapa
from nodo import Nodo
from grafo import Grafo
import sys
import os
from ficheiro import Ficheiro
import pickle
#USAR ISTO   <-----------------------------
# self.fstpath.pop(0)
#self.fstpath.pop()
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
      # m.expandir()
      m.grafo.add_heuristica()

      file = open(bin_ficheiro, 'wb')
      pickle.dump(m, file)
      file.close()


   saida = -1

   # menu de opções
   while saida != 0:
      print("")
      print("1-Desenhar Grafo do Mapa")
      print("2-DFS")
      print("3-BFS")
      print("4-A-star")
      print("5-Greedy")
      print("0-Sair")

      saida = int(input("introduza a sua opcao-> "))
      if saida == 0:
         print("saindo.......")
      elif saida == 1:
         m.grafo_mapa.desenha()
         l=input("prima enter para continuar")
      elif saida == 2:
         m.listaTemp = m.listaPartida.copy()
         results = []
         resultDFS = []
         i = 1
         while True:
            if len(resultDFS) != 0:
               m.grafo.fstpath = resultDFS
               m.grafo.fstpath.pop(0)
               m.grafo.fstpath.pop()
            m.expandir()
            t_start = time.time()
            resultDFS, custoTotalDFS = m.grafo.procura_DFS(m.grafo.nodo_inicial)
            t_end = time.time()
            print("Veiculo " + str(i) + ":")
            print("Resultado: " + str(resultDFS) + "\nCusto: " + str(custoTotalDFS))
            resultDFSExpand, timeDFS = m.expande_caminho(resultDFS)
            results.append((i, timeDFS))
            print("Resultado expandido: " + str(resultDFSExpand) + "\nTempo: " + str(timeDFS))
            print("Tempo para encontrar a solução: " + str(round((t_end - t_start) * 1000, 2)) + " ms")
            print("\n")
            i += 1
            if len(m.listaTemp) == 0:
               break
         results.sort(key=m.vencedor)
         print("Ranking:")
         n = 1
         for (veiculo, tempo) in results:
            print(str(n) + "º: Veiculo " + str(veiculo) + " Tempo " + str(tempo) + " (u.t.)")
            n += 1
         l = input("prima enter para continuar")
      elif saida == 3:
         m.listaTemp = m.listaPartida.copy()
         results = []
         resultBFS = []
         i = 1
         while True:
            if len(resultBFS) != 0:
               m.grafo.fstpath = resultBFS
               m.grafo.fstpath.pop(0)
               m.grafo.fstpath.pop()
            m.expandir()
            t_start = time.time()
            resultBFS, custoTotalBFS = m.grafo.procura_BFS()
            t_end = time.time()
            print("Veiculo " + str(i) + ":")
            print("Resultado: " + str(resultBFS) + "\nCusto: " + str(custoTotalBFS))
            resultBFSExpand, timeBFS = m.expande_caminho(resultBFS)
            results.append((i,timeBFS))
            print("Resultado expandido: " + str(resultBFSExpand) + "\nTempo: " + str(timeBFS))
            print("Tempo para encontrar a solução: " + str(round((t_end - t_start) * 1000, 2)) + " ms")
            print("\n")
            i+=1
            if len(m.listaTemp) == 0:
               break
         results.sort(key=m.vencedor)
         print("Ranking:")
         n = 1
         for (veiculo,tempo) in results:
            print(str(n) + "º: Veiculo " + str(veiculo) + " Tempo " + str(tempo) + " (u.t.)")
            n += 1
         l = input("prima enter para continuar")

      elif saida == 4:
         m.listaTemp = m.listaPartida.copy()
         results = []
         resultAStar = []
         i = 1
         while True:
            if len(resultAStar) != 0:
               m.grafo.fstpath = resultAStar
               m.grafo.fstpath.pop(0)
               m.grafo.fstpath.pop()
            m.expandir()
            t_start = time.time()
            resultAStar, custoTotalAStar = m.grafo.procura_aStar()
            t_end = time.time()
            print("Veiculo " + str(i) + ":")
            print("Resultado: " + str(resultAStar) + "\nCusto: " + str(custoTotalAStar))
            resultAStarExpand, timeAStar = m.expande_caminho(resultAStar)
            results.append((i, timeAStar))
            print("Resultado expandido: " + str(resultAStarExpand) + "\nTempo: " + str(timeAStar))
            print("Tempo para encontrar a solução: " + str(round((t_end - t_start) * 1000, 2)) + " ms")
            print("\n")
            i += 1
            if len(m.listaTemp) == 0:
               break
         results.sort(key=m.vencedor)
         print("Ranking:")
         n = 1
         for (veiculo, tempo) in results:
            print(str(n) + "º: Veiculo " + str(veiculo) + " Tempo " + str(tempo) + " (u.t.)")
            n += 1
         l = input("prima enter para continuar")
      elif saida == 5:
         m.listaTemp = m.listaPartida.copy()
         results = []
         resultGreedy = []
         i = 1
         while True:
            if len(resultGreedy) != 0:
               m.grafo.fstpath = resultGreedy
               m.grafo.fstpath.pop(0)
               m.grafo.fstpath.pop()
            m.expandir()
            t_start = time.time()
            resultGreedy, custoTotalGreedy = m.grafo.greedy()
            t_end = time.time()
            print("Veiculo " + str(i) + ":")
            print("Resultado: " + str(resultGreedy) + "\nCusto: " + str(custoTotalGreedy))
            resultGreedyExpand, timeGreedy = m.expande_caminho(resultGreedy)
            results.append((i, timeGreedy))
            print("Resultado expandido: " + str(resultGreedyExpand) + "\nTempo: " + str(timeGreedy))
            print("Tempo para encontrar a solução: " + str(round((t_end - t_start) * 1000, 2)) + " ms")
            print("\n")
            i += 1
            if len(m.listaTemp) == 0:
               break
         results.sort(key=m.vencedor)
         print("Ranking:")
         n = 1
         for (veiculo, tempo) in results:
            print(str(n) + "º: Veiculo " + str(veiculo) + " Tempo " + str(tempo) + " (u.t.)")
            n += 1
         l = input("prima enter para continuar")
      else:
         print("you didn't add anything")
         l = input("prima enter para continuar")


if __name__ == '__main__':
    main()



