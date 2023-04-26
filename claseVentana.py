'''
Métodos y Constructores con valores por defecto

Defina una clase Ventana con los siguientes atributos: título, valor de las coordenadas x e y del vértice superior izquierdo y valor de las coordenadas x e y 
del vértice inferior derecho. Implemente los métodos necesarios, para que pueda ejecutarse el programa dado.

Reglas de negocio:

El menor valor para las coordenadas del vértice superior izquierdo es 0 para cada una.
El mayor valor para las coordenadas del vértice inferior derecho es 500 para cada una.
El desplazamiento por defecto de una ventana es en una unidad en la dirección correspondiente.
El valor de x del vértice superior izquierdo siempre debe ser menor al valor de x del vértice inferior derecho.
El valor de y del vértice superior izquierdo siempre debe ser menor al valor de y del vértice inferior derecho.
'''
class Ventana:
    __titulo: str
    __vi1: int ## cordenada x de vertice izquierdo
    __vi2: int ## cordenada y de vertice izquierdo
    __vd1: int ## cordenada x de vertice derecho
    __vd2: int ## cordenada y de vertice derecho

    def __init__ (self, titulo, vi1=0, vi2=0, vd1=500, vd2=500):
        self.__titulo = titulo
        if (vi1 >= 0 & vi2 >= 0 & vi1 < vd1):
            self.__vi1 = vi1
            self.__vi2 = vi2
        else: print ('Error, valor minimo para el vertice superior izquierdo es 0')
        if (vd1 <= 500 & vd2 >= 500 & vi2 < vd2):
            self.__vd1 = vd1
            self.__vd2 = vd2
        else: print ('Error, valor maximo para el vertice inferior derecho es 500')

    def mostrar (self):
        print (f'''
Titulo: {self.__titulo}
Cordenada x de vertice izquierdo: {self.__vi1}
Cordenada y de vertice izquierdo: {self.__vi2}
Cordenada x de vertice derecho: {self.__vd1}
Cordenada y de vertice derecho: {self.__vd2}
        ''')

    def alto(self):
        return self.__vi2

    def ancho(self):
        return self.__vd1

    def moverDerecha(self, u=1):
        self.__vd1 += u
        self.__vi1 += u

    def moverIzquierda (self, u=1):
        self.__vd1 -= u
        self.__vi1 -= u

    def bajar (self, u=1):
        self.__vd2 -= u
        self.__vi2 -= u

    def subir (self, u=1):
        self.__vd2 += u
        self.__vi2 += u

    def getTitulo (self):
        return self.__titulo
    
