#Creamos la función busqueda_binaria que recibe dos parámetros: una lista y un elemento a buscar
def busqueda_binaria(lista, elemento):
    low = 0 #Definimos el límite inferior de la lista
    high= len(lista) -1 #Definimos el límite superior de la lista

#Mientras el límite inferior sea menor o igual al límite superior
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == elemento: #Si el elemento en la posición media es igual al elemento que buscamos devolvemos el índice
            return mid
        #Caso contrario, continuamos la comparación hasta encontrar el elemento y devolver su índice
        elif lista[mid] < elemento:
            low = mid + 1
        else: 
            high = mid - 1 
    return -1
    
lista = [4,25, 56,7,5]
lista.sort() #La busqueda binaria requiere que la lista esté ordenada
print(busqueda_binaria(lista,5)) #Devuelve 1