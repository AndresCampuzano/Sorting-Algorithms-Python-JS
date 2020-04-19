# Buscar el numero menor en mi array.
# Crear dos subarrays para llevar el control de mi algoritmo.
# Imprimir el resultado del ordenamiento.


def selectionSort(array):
    # recorrer el array completo
    for i in range(len(array)):
        # encontrar el valor minimo restante dentro del array desordenado.
        idxDes = i
        for j in range(i+1, len(array)):
            if array[idxDes] > array[j]:
                idxDes = j

         # ya que encontramos el minimo elemento,
         # lo vamos a cambiar por el primer valor de nuestro array desordenado.
         array[i],array[idxDes] = array[idxDes], array[i]
