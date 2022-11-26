

#fincion 
#recibe 3 parametros x = y = n = cantidad de iteraciones
def fib_list(x,y,n):
    L=[x,y] #creamos una lista
    #ciclo for para las iteraciones 
    for i in range(n-1):
        #realizamos a adicion de los indices inferior y superiorvalores a la lista
        L.append(L[-1]+ L[-2])
    #se devuelve el ultimo numero de la    
    return L[-1]


#fibonacci recursividad
def fib_rec(x,y,n):
    #se almacena la suma de los dos indices anteriores
    z = x + y
    #se valida que n no sea igual a cero
    if n > 0:
        #se realiza el llamado a la misma funcion pasando 
        #el indice final como indice inicial
        #la sumatoria de los dos indice anteriores como indice final
        #la cantidad de iteraciones menos 1
        return fib_rec(y,z,n-1)
    else:
        #si la cantidad de iteraciones es igual a cero o inferior
        #el resultado es el indice inicial
        return x

#fibbonacci

def fib_for(x,y,n):
    for i in range(n-1):
        z = x + y
        x = y
        y = z
    return z