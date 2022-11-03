from nodo import Nodo
from grafo import Grafo


def main():
   #n1 = Nodo(1,3,"X")
   #n2 = Nodo(0,5,"-")
   #n3 = Nodo(3,1,"X")

   grafo = Grafo()

   grafo.parse("teste.txt")

   print(grafo)

if __name__ == '__main__':
    main()



