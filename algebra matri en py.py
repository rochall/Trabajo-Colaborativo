import numpy as np

# ======================================
# ÁLGEBRA MATRICIAL EN PYTHON CON NUMPY
# ======================================

# Crear matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

# --------------------------------------
# Suma de matrices
# --------------------------------------
suma = A + B

print("\nSuma de matrices A + B:")
print(suma)

# --------------------------------------
# Resta de matrices
# --------------------------------------
resta = A - B

print("\nResta de matrices A - B:")
print(resta)

# --------------------------------------
# Multiplicación por escalar
# --------------------------------------
escalar = 3
producto_escalar = escalar * A

print("\nMultiplicación de A por 3:")
print(producto_escalar)

# --------------------------------------
# Multiplicación matricial
# --------------------------------------
producto_matricial = np.dot(A, B)

print("\nMultiplicación matricial A x B:")
print(producto_matricial)

# --------------------------------------
# Producto elemento por elemento
# --------------------------------------
producto_elemento = A * B

print("\nProducto elemento por elemento:")
print(producto_elemento)

# --------------------------------------
# Transpuesta
# --------------------------------------
transpuesta_A = A.T

print("\nTranspuesta de A:")
print(transpuesta_A)

# --------------------------------------
# Determinante
# --------------------------------------
determinante_A = np.linalg.det(A)

print("\nDeterminante de A:")
print(determinante_A)

# --------------------------------------
# Matriz inversa
# --------------------------------------
inversa_A = np.linalg.inv(A)

print("\nInversa de A:")
print(inversa_A)

# --------------------------------------
# Traza de una matriz
# --------------------------------------
traza_A = np.trace(A)

print("\nTraza de A:")
print(traza_A)

# --------------------------------------
# Rango de una matriz
# --------------------------------------
rango_A = np.linalg.matrix_rank(A)

print("\nRango de A:")
print(rango_A)

# --------------------------------------
# Valores y vectores propios
# --------------------------------------
valores_propios, vectores_propios = np.linalg.eig(A)

print("\nValores propios de A:")
print(valores_propios)

print("\nVectores propios de A:")
print(vectores_propios)

# --------------------------------------
# Sistema de ecuaciones lineales
# --------------------------------------
# 2x + y = 5
# x - y = 1

C = np.array([[2, 1],
              [1, -1]])

D = np.array([5, 1])

solucion = np.linalg.solve(C, D)

print("\nSolución del sistema de ecuaciones:")
print(solucion)

# --------------------------------------
# Matriz identidad
# --------------------------------------
identidad = np.eye(3)

print("\nMatriz identidad de orden 3:")
print(identidad)

# --------------------------------------
# Matriz de ceros y unos
# --------------------------------------
ceros = np.zeros((2, 2))
unos = np.ones((2, 2))

print("\nMatriz de ceros:")
print(ceros)

print("\nMatriz de unos:")
print(unos)

# --------------------------------------
# Potencia de una matriz
# --------------------------------------
potencia = np.linalg.matrix_power(A, 2)

print("\nA elevado al cuadrado:")
print(potencia)
