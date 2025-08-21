import time
import tracemalloc
import matplotlib.pyplot as plt

def fact_recursivo(n):
    if n < 0:
        return 'Error'
    elif n == 1 or n == 0:
        return 1
    else:
        return n * fact_recursivo(n-1)
    
def fact_iterativo(n):
    if n < 0:
        return 'Error'
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


datos = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
memoria = 0

def calcular_tiempo(datos, funcion):
    tiempos = []
    for i in datos:
        inicio = time.time()
        funcion(i)
        fin = time.time()
        tiempos.append(fin-inicio)
    return tiempos

def calcular_memoria(datos,funcion):
    memorias = []
    for i in datos:
        tracemalloc.start()
        funcion(i)
        current, peak = tracemalloc.get_traced_memory()
        memorias.append(peak)
        tracemalloc.stop()
    return memorias

tiempos_recursiva = calcular_tiempo(datos, fact_recursivo)
tiempos_iterativa = calcular_tiempo(datos, fact_iterativo)

memoria_recursiva = calcular_memoria (datos,fact_recursivo)
memoria_iterativa = calcular_memoria (datos, fact_iterativo)

grafica,(tiempo,memoria) = plt.subplots(1,2, figsize=(15,5))

tiempo.plot (datos,tiempos_recursiva, color = 'g', label='Tiempo Funcion Factorial Recursiva')
tiempo.plot (datos, tiempos_iterativa, color = 'black', label = 'Tiempo Funcion Factorial Iterativa')
tiempo.set_title("Tiempo de ejecución")
tiempo.set_xlabel("Valor de n")
tiempo.set_ylabel("Tiempo (s)")
tiempo.legend()
memoria.plot (datos,memoria_recursiva, color = 'r' , label = 'Memoria Funcion Factorial Recursiva')
memoria.plot (datos, memoria_iterativa, color = 'b', label = 'Memoria Funcion Factorial Iterativa')
memoria.set_title("Uso de memoria")
memoria.set_xlabel("Valor de n")
memoria.set_ylabel("Memoria (bytes)")
memoria.legend()
plt.tight_layout()
plt.show()