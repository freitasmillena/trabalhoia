import time
from Mapa import Mapa
import sys
import os
from ficheiro import Ficheiro
import pickle
#USAR ISTO   <-----------------------------
# self.fstpath.pop(0)
#self.fstpath.pop()
# recebe como argumento o ficheiro

def DFS(m,ficheiro):
   m.listaTemp = m.listaPartida.copy()
   results = []
   resultDFS = []
   paths = []
   i = 1
   while True:
      if len(resultDFS) != 0:
         resultDFS.pop(0)
         resultDFS.pop()
         m.grafo.paths.append(resultDFS)

      bin_ficheiro = ficheiro.diretoria + "DFS" + str(i) + ".bin"
      isExist = os.path.exists(bin_ficheiro)
      if isExist:
         file = open(bin_ficheiro, 'rb')
         m = pickle.load(file)
         file.close()
      else :
         m.expandir()
         file = open(bin_ficheiro, 'wb')
         pickle.dump(m, file)
         file.close()
      
      t_start = time.time()
      resultDFS, custoTotalDFS = m.grafo.procura_DFS(m.grafo.nodo_inicial)
      t_end = time.time()
      print("Veiculo " + str(i) + ":")
      print("Resultado: " + str(resultDFS) + "\nCusto: " + str(custoTotalDFS))
      resultDFSExpand, pathDFSExpand, timeDFS = m.expande_caminho(resultDFS)
      paths.append(pathDFSExpand.copy())
      ficheiro.printMapaColorido(pathDFSExpand)
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

   ficheiro.printMapaCaminhosColoridos(paths)

def BFS(m,ficheiro):
   m.listaTemp = m.listaPartida.copy()
   results = []
   resultBFS = []
   paths = []
   i = 1
   while True:
      pathsCopy = [[]]
      if len(resultBFS) != 0:
         resultBFS.pop(0)
         resultBFS.pop()
         m.grafo.paths.append(resultBFS)
      
      bin_ficheiro = ficheiro.diretoria + "BFS" + str(i) + ".bin"
      isExist = os.path.exists(bin_ficheiro)
      if isExist:
         file = open(bin_ficheiro, 'rb')
         m = pickle.load(file)
         file.close()
      else :
         m.expandir()
         file = open(bin_ficheiro, 'wb')
         pickle.dump(m, file)
         file.close()

      t_start = time.time()

      resultBFS, custoTotalBFS = m.grafo.procura_BFS()

      t_end = time.time()
      print("Veiculo " + str(i) + ":")
      print("Resultado: " + str(resultBFS) + "\nCusto: " + str(custoTotalBFS))
      resultBFSExpand, pathBFSExpand, timeBFS = m.expande_caminho(resultBFS)
      paths.append(pathBFSExpand.copy())
      ficheiro.printMapaColorido(pathBFSExpand)
      results.append((i, timeBFS))
      print("Resultado expandido: " + str(resultBFSExpand) + "\nTempo: " + str(timeBFS))
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

   ficheiro.printMapaCaminhosColoridos(paths)

def AStar(m,ficheiro):
   m.listaTemp = m.listaPartida.copy()
   results = []
   resultAStar = []
   paths = []
   i = 1
   while True:
      if len(resultAStar) != 0:
         resultAStar.pop(0)
         resultAStar.pop()
         m.grafo.paths.append(resultAStar)
      
      bin_ficheiro = ficheiro.diretoria + "AStar" + str(i) + ".bin"
      isExist = os.path.exists(bin_ficheiro)
      if isExist:
         file = open(bin_ficheiro, 'rb')
         m = pickle.load(file)
         file.close()
      else :
         m.expandir()
         file = open(bin_ficheiro, 'wb')
         pickle.dump(m, file)
         file.close()

      t_start = time.time()
      resultAStar, custoTotalAStar = m.grafo.procura_aStar()
      t_end = time.time()
      if resultAStar is None:
         break
      print("Veiculo " + str(i) + ":")
      print("Resultado: " + str(resultAStar) + "\nCusto: " + str(custoTotalAStar))
      resultAStarExpand, pathAStarExpand, timeAStar = m.expande_caminho(resultAStar)
      paths.append(pathAStarExpand.copy())
      ficheiro.printMapaColorido(pathAStarExpand)
      results.append((i, timeAStar))
      print("Resultado expandido: " + str(resultAStarExpand) + "\nTempo: " + str(timeAStar))
      print("Tempo para encontrar a solução: " + str(round((t_end - t_start) * 1000, 2)) + " ms")
      print("\n")
      i += 1
      if len(m.listaTemp) == 0:
         break
   if resultAStar is not None:
      results.sort(key=m.vencedor)
      print("Ranking:")
      n = 1
      for (veiculo, tempo) in results:
         print(str(n) + "º: Veiculo " + str(veiculo) + " Tempo " + str(tempo) + " (u.t.)")
         n += 1

      ficheiro.printMapaCaminhosColoridos(paths)

def Greedy(m,ficheiro):
   m.listaTemp = m.listaPartida.copy()
   results = []
   resultGreedy = []
   paths = []
   i = 1
   while True:
      if len(resultGreedy) != 0:
         resultGreedy.pop(0)
         resultGreedy.pop()
         m.grafo.paths.append(resultGreedy)
      
      bin_ficheiro = ficheiro.diretoria + "Greedy" + str(i) + ".bin"
      isExist = os.path.exists(bin_ficheiro)
      if isExist:
         file = open(bin_ficheiro, 'rb')
         m = pickle.load(file)
         file.close()
      else :
         m.expandir()
         file = open(bin_ficheiro, 'wb')
         pickle.dump(m, file)
         file.close()

      t_start = time.time()
      resultGreedy, custoTotalGreedy = m.grafo.greedy()
      t_end = time.time()
      if resultGreedy is None:
         break
      print("Veiculo " + str(i) + ":")
      print("Resultado: " + str(resultGreedy) + "\nCusto: " + str(custoTotalGreedy))
      resultGreedyExpand, pathGreedyExpand, timeGreedy = m.expande_caminho(resultGreedy)
      paths.append(pathGreedyExpand.copy())
      ficheiro.printMapaColorido(pathGreedyExpand)
      results.append((i, timeGreedy))
      print("Resultado expandido: " + str(resultGreedyExpand) + "\nTempo: " + str(timeGreedy))
      print("Tempo para encontrar a solução: " + str(round((t_end - t_start) * 1000, 2)) + " ms")
      print("\n")
      i += 1
      if len(m.listaTemp) == 0:
         break
   if resultGreedy is not None:
      results.sort(key=m.vencedor)
      print("Ranking:")
      n = 1
      for (veiculo, tempo) in results:
         print(str(n) + "º: Veiculo " + str(veiculo) + " Tempo " + str(tempo) + " (u.t.)")
         n += 1
      ficheiro.printMapaCaminhosColoridos(paths)




def main():

   path_ficheiro = sys.argv[1]

   nome_ficheiro = path_ficheiro.split('.')[0]
   bin_ficheiro = nome_ficheiro + ".bin"
   isExist = os.path.exists(bin_ficheiro)

   m = None

   ficheiro = Ficheiro()
   # calcula o número de linhas e colunas do ficheiro
   ficheiro.calculaLC(path_ficheiro) 
   linhas = ficheiro.linhas
   colunas = ficheiro.colunas

   if isExist :
      file = open(bin_ficheiro, 'rb')
      m = pickle.load(file)
      file.close()

   else:
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
      elif saida == 2:
         DFS(m,ficheiro)
      elif saida == 3:
         BFS(m,ficheiro)
      elif saida == 4:
         AStar(m,ficheiro)
      elif saida == 5:
         Greedy(m,ficheiro)
      else:
         print("you didn't add anything")
      
      if saida != 0 :
         l = input("prima enter para continuar")


if __name__ == '__main__':
    main()



