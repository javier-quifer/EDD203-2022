class Nodo:
    def __init__(self, info):
        self.info = info
        self.izdo = None
        self.dcho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def crear_arbol(self):
        resp = ""
        aux = input('Introd. info para la raiz ... ')
        self.raiz = Nodo(aux)

        self.raiz.izdo = None
        self.raiz.dcho = None

        resp = input('Tienes mas datos? (si/no)')

        while resp == "si":
            x = input('Escriba la información para el nodo ...')
            dat = Nodo(x)

            aux1 = aux2 = self.raiz

            while  not aux1 is None:
                aux2 = aux1
                if dat.info < aux2.info:
                    aux1 = aux2.izdo
                else:
                    aux1 = aux2.dcho

            if dat.info < aux2.info:
                aux2.izdo = dat
            else:
                aux2.dcho = dat

            resp = input('Tienes mas datos? (si/no) ')

    def en_orden(self, r):
        # Si r es diferente de nulo
        if not r is None:
            self.en_orden(r.izdo)
            print(r.info)
            self.en_orden(r.dcho)

    def pre_orden(self, r):
        if not r is None:
            print(r.info)
            self.pre_orden(r.izdo)
            self.pre_orden(r.dcho)

    def pos_orden(self, r):
        if not r is None:
            self.pos_orden(r.izdo)
            self.pos_orden(r.dcho)
            print(r.info)

    def busqueda(self, r, x):
        if r is None:
            print('No se encuentra')
        elif r.info == x:
            print(x , ' fue encontrado')
        elif x < r.info:
            self.busqueda(r.izdo, x)
        elif x > r.info:
            self.busqueda(r.dcho, x)


arbol = ArbolBinario()
arbol.crear_arbol()
arbol.en_orden(arbol.raiz)
# arbol.pre_orden(arbol.raiz)
# arbol.busqueda(arbol.raiz, '18')
