#Creamos la funcion para la busqueda lineal con los parametros lista y target(objetivo)
def busqueda_lineal(lista, target):
    #Iterando en la lista, compara si el elemento de la iteración es igual al objetivo estalecido.
    for i in range(len(lista)):
        if lista[i] == target:
            return i  
    return -1  #Si el elemento no se encuentra en la lista

lista = [1,2,3,4,5]
print(busqueda_lineal(lista,5)) #Devuelve 4
