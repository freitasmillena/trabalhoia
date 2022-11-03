from nodo import Node


def main():
   n1 = Node(1,3,"X")
   n2 = Node(0,5,"-")
   n3 = Node(3,1,"X")

   print(n1)
   print(n2)
   print(n3)

   print(n1.__hash__())
   print(n3.__hash__())

if __name__ == '__main__':
    main()


