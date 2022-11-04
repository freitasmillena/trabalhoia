from nodo import Nodo
from grafo import Grafo


def main():
   #n1 = Nodo(1,3,"X")
   #n2 = Nodo(0,5,"-")
   #n3 = Nodo(3,1,"X")

   grafo = Grafo()

   grafo.parse("teste.txt")

   grafo.add_heuristica()


   #print(grafo)
   #print(grafo.m_nodos_objetivos)
   #print(grafo.m_h)

   print(grafo.procura_BFS(grafo.nodo_inicial, grafo.m_nodos_objetivos))
   print(grafo.procura_aStar(grafo.nodo_inicial, grafo.m_nodos_objetivos))

if __name__ == '__main__':
    main()



