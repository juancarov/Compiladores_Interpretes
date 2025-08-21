import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('/home/joanchojuanjo/Documentos/resultados.csv')

print(datos)

grafica, (tiempo, memoria) = plt.subplots(1, 2, figsize=(15, 5), sharex=True)

tiempo.plot(datos['n'], datos['TiempoRecursivo(ms)'], color='g', label='Tiempo Funcion Factorial Recursiva')
tiempo.plot(datos['n'], datos['TiempoIterativo(ms)'], color='black', label='Tiempo Funcion Factorial Iterativa')
tiempo.set_title("Tiempo de ejecución (log)")
tiempo.set_xlabel("Valor de n")
tiempo.set_ylabel("Tiempo (ms)")
tiempo.set_yscale("log")   
tiempo.legend()

memoria.plot(datos['n'], datos['MemoriaRecursiva(bytes)'], color='r', label='Memoria Funcion Factorial Recursiva')
memoria.plot(datos['n'], datos['MemoriaIterativa(bytes)'], color='b', label='Memoria Funcion Factorial Iterativa')
memoria.set_title("Uso de memoria (log)")
memoria.set_xlabel("Valor de n")
memoria.set_ylabel("Memoria (bytes)")
memoria.set_yscale("log")  
memoria.legend()

plt.tight_layout()
plt.savefig('/home/joanchojuanjo/Descargas/Memoria_Tiempo_Compilador_log.png')
plt.show()
