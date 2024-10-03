# Actividad Complemetaria No 2

# Datos

data = [81,73,70,71,70,11,68,53,30,15,43,80,54,85,55,27,27,97,57,15,6,86,38,21,25,73,67,78,46,40,34,
        37,58,81,46,34,96,1,28,90,3,20,27,45,72,95,22,42,59,71,95,31,35,52,95,16,66,14,85,8,85,67,17,
        65,91,70,22,67,55,27,1,89,2,69,3,36,28,83,59,60,62,92,11,13,64,11,39,30,4,99,73,14,72,92,47,77,
        63,80,64,27,89,40,85,14,39,78,45,54,4,47,18,38,26,13,57,42,17,34,72,47,34,69,13,80,23,42,95,34,
        72,76,15,60,98,66,66,6,49,38,80,29,64,53,69,84,59,12,2,97,19,9,53,78,60,33,49,36,48,66,57,40,16,
        9,9,17,61,60,37,65,12,21,4,27,90,77,47,45,67,26,90,16,10,86,66,51,93,34,2,85,91,92,28,65,91,27,17,
        46,7,43,21,73,69,69,88,72,2,39,7,49,78,10,85,88,31,97,83,20,9,15,4,92,89,34,49,6,51,12,56,65,6,63,
        13,54,96,22,76,79,30,20,15,21,20,43,22,32,93,50,54,22,11,24,43,9,8,86,98,26,65,46,66,34,32,97,71,
        11,24,44,58,11,42,44,49,74,14,77,59,89,30,15,95,80,36,92,89,68,98,81,49,18,23,20,36,98,28,60,79,
        75,40,87,67,86,99,52,90,2,39,37,4,9,20,15,83,47,4,50,80,91,64,89,29,43,58,74,48,11,67,78,80,80,93
        ,34,48,88,34,95,91,43,48,96,86,81,3,72,77,83,57,4,72,17,68,95,65,63,67,90,71,73,98,4,68,25,71,67,
        85,91,95,11,31,99,26,64,73,87,86,76,86,31,36,43,59,78,44,34,34,82,36,28,16,15,71,12,6,92,59,60,59
        ,20,71,74,59,65,35,36,25,51,13,27,61,70,84,56,64,99,67,70,53,97,88,47,74,10,10,77,1,40,34,40,55,24,28
        ,41,66,51,29,31,97,22,99,68,30,75,91,48,25,3,21,51,53,7,13,72,63,81,52,65,1,87,85,78,30,41,95,99,63,24
        ,99,53,63,36,11,7,45,76,10,90,49,55,70,12,49,8,39,71,17,83,90,62,20,67,67,12,83,22,4,37,27,31,84,13,44,57,
        74,34,81,33,48,75,70,75,90,33,68,37,58,35,97,35,13,11,97,55,47,49,66,40,99,1,22,91,47,54,74,53,51,36,19,42,11
        ,22,97,49,15,59,6,24,70,66,97,17,27,22,22,7,26,25,92,90,55,39,36,17,92,2,1,88,94,39,74,88,46,9,53,73,49,86,63,
        46,65,91,8,80,39,72,19,82,62,2,59,95,83,90,69,98,42,19,26,30,95,7,27,3
]

#Obviando que el conjunto de datos no está agrupado las definiciones son las siguintes:


# MEDIA (x̄)
# Definición: La media es el promedio de todos los valores en una lista de datos.
# Cálculo: La suma de todos los valores (∑​xi) entre el número de datos (n)
# x̄= ∑​xi/n

#Código

sumxi = sum(data) # Sumar todos los valores
n = len(data) # Contar los valores de la lista

media = sumxi/n # Aplicar formula para hallar la media x̄= ∑​xi/n

# MEDIANA
# Definición: La mediana es el valor que divide la lista de datos ordenada en dos partes iguales.
# Cálculo:
# 1. Ordena los datos de menor a mayor.
# Para hallar el valor central: Dato Central = n/2
# 2. Si el número de datos (n) es impar, la mediana es el valor central
# 3. Si el número de datos (n) es par, la mediana es el promedio de los dos valores centrales.

#Código


lista_ordenada = sorted(data) # Ordenar la lista


if n % 2 != 0: # Verificar si la longitud de la lista es impar
        datocentral = lista_ordenada[n // 2] # Si es impar, devolver el número central
        mediana = datocentral
else:
        datocentral1 = lista_ordenada[n // 2 - 1] # Si es par, devolver el promedio de los dos números centrales
        datocentral2 = lista_ordenada[n // 2]
        promedio = (datocentral1 + datocentral2) / 2
        mediana = promedio

# MODA
# Definición: La moda es el valor que aparece con mayor frecuencia en la lista de datos.
# Cálculo: Identifica el valor que se repite más veces en la lista.

# Código

repeticiones = {} # Se crea un diccionario para almacenar las repeticiones por valores

for elemento in data: # Recorrer la lista y contar las repeticiones

    if elemento in repeticiones:
        repeticiones[elemento] += 1
    else:
        repeticiones[elemento] = 1

valor_mas_repetido = None  # Encontrar el valor con la mayor frecuencia
max_repeticiones = 0

for valor, cantidad in repeticiones.items():
    if cantidad > max_repeticiones:
        max_repeticiones = cantidad
        valor_mas_repetido = valor

moda = f"la moda es {valor_mas_repetido}, se repite {max_repeticiones} veces."


# VARIANZA (σ^2)
# Definición: La varianza mide la dispersión de los datos respecto a la media.
# Cálculo: Suma los restultados de restar cada valor (​xi) menos las media (x̄) elevados al cuadrado
#          y esta suma la divide entre el número de datos (n)
# σ^2 = ∑(​xi-x̄)^2/n

# Código

suma_diferencias_cuadrado = sum((xi - media) ** 2 for xi in data) # calcular ∑(​xi-x̄)^2

varianza = suma_diferencias_cuadrado / n # Divide las suma de diferencias al cuadrado sobre el numero de datos.


# DESVIACIÓN ESTANDAR (σ)
# Definición: La desviación estándar es la raíz cuadrada de la varianza y proporciona una medida
#             de la dispersión de los datos.
# Cálculo: σ=√σ^2

desviacionEstandar= varianza ** 0.5 # Propiedad de los exponentes, elevar un número a 1/2 es igual a su √

# COEFICIENTE DE VARIACIÓN (CV)
# Definición: El coeficiente de variación es una medida de la dispersión relativa de los datos en 
#             relación con la media,
# Cálculo: σ/x̄*100%

CV = (desviacionEstandar/media)*100 # Se realiza la formula, al momento de mostrar los resultados se formatea con un {CV}%

# NORMALIZACIÓN Z (Z)
# Definición: La normalización Z transforma los datos para que tengan una media de 0 y una desviación
#             estándar de 1.
# Cálculo: Z = ​xi-x̄/σ

normalizacion_z = [(x - media) / desviacionEstandar for x in data]  # Calcular la normalización Z para cada dato


resultados = f"Según los {n} datos agregados, los resultados de las medidas son:\n\n Media: {media}\n Mediana: {mediana}\n Moda: {moda}\n Varianza: {varianza}\n Desviación Estandar: {desviacionEstandar}\n Coeficiente de Variación {CV}%\n\n Con La normalización z Aplicada a los {n} valores, los valores son:\n\n{normalizacion_z}"

print(resultados)

