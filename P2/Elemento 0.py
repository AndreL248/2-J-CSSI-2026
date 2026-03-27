"""
Fecha   :12/03/2026
Grupo   :2°J
Nombre  :Andre Luciano De la Torre Gutierrez


Encontrar que elementos de una lista suman cero

Escribe una clase de python que encuentre 3 elementos que sumen cero
Los elementos se encuentran en una lista y son numeros enteros +-

"""

#Codigo
class Ceros:    
    def __init__(self, lista):
        self.lista = lista

    def encontrar(self):
        numeros = sorted(self.lista)
        resultado = []

        for i in range(len(numeros) - 2):
            izquierda = i + 1
            derecha = len(numeros) - 1

            while izquierda < derecha:
                suma = numeros[i] + numeros[izquierda] + numeros[derecha]

                if suma == 0:
                    resultado.append(
                        (numeros[i], numeros[izquierda], numeros[derecha])
                    )
                    izquierda += 1
                    derecha -= 1

                elif suma < 0:
                    izquierda += 1
                else:
                    derecha -= 1

        return resultado

test=Ceros([-20,-15,10,7,8])
print(test.encontrar())

"""
Resutlado

"""