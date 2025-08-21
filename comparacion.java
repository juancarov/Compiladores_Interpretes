import java.io.FileWriter;
import java.io.IOException;

public class Tiempo_Memoria {

    public static long factorialRecursivo(int n) {
        if (n < 0) return 0;
        if (n == 0 || n == 1) return 1;
        return n * factorialRecursivo(n - 1);
    }

    public static long factorialIterativo(int n) {
        if (n < 0) return 0;
        long resultado = 1;
        for (int i = 1; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }

    // 🔹 Tiempo total en milisegundos
    public static double medirTiempo(Runnable funcion, int repeticiones) {
        long inicio = System.nanoTime();
        for (int i = 0; i < repeticiones; i++) {
            funcion.run();
        }
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000.0;
    }

    // 🔹 Medición de memoria más sensible
    public static long medirMemoria(Runnable funcion, int repeticiones) {
        Runtime runtime = Runtime.getRuntime();
        long maxDelta = 0;

        for (int j = 0; j < 5; j++) { // tomar varias muestras
            System.gc(); // sugerir recolección
            long memoriaAntes = runtime.totalMemory() - runtime.freeMemory();

            for (int i = 0; i < repeticiones; i++) {
                funcion.run();

                // truco: asignar un arreglo temporal para forzar medición
                int[] temp = new int[1000];  
                temp[0] = 1;
            }

            long memoriaDespues = runtime.totalMemory() - runtime.freeMemory();
            long delta = memoriaDespues - memoriaAntes;

            if (delta > maxDelta) {
                maxDelta = delta;
            }
        }

        return maxDelta;
    }

    // 🔹 Medir factoriales
    public static String medirFactoriales(int n, int repeticiones) {
        double tiempoRec = medirTiempo(() -> factorialRecursivo(n), repeticiones);
        long memoriaRec = medirMemoria(() -> factorialRecursivo(n), repeticiones);

        double tiempoIt = medirTiempo(() -> factorialIterativo(n), repeticiones);
        long memoriaIt = medirMemoria(() -> factorialIterativo(n), repeticiones);

        return String.format("%d,%.6f,%d,%.6f,%d\n",
                n, tiempoRec, memoriaRec, tiempoIt, memoriaIt);
    }

    public static void main(String[] args) {
        int[] datos = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
                       55, 60, 65, 70, 75, 80, 85, 90, 95, 100};

        int repeticiones = 1_000_000; // alto para que se note

        try (FileWriter writer = new FileWriter("resultados.csv")) {
            writer.write("n,TiempoRecursivo(ms),MemoriaRecursiva(bytes),TiempoIterativo(ms),MemoriaIterativa(bytes)\n");

            for (int n : datos) {
                writer.write(medirFactoriales(n, repeticiones));
            }

            System.out.println("Resultados guardados en 'resultados.csv'");
        } catch (IOException e) {
            System.out.println("Error al escribir el archivo CSV: " + e.getMessage());
        }
    }
}

