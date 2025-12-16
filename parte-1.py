#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from constraint import *

def leer_instancia(ruta_fichero):
    
    try:
        with open(ruta_fichero, 'r') as f:
            lineas_raw = [l.strip() for l in f.readlines() if l.strip()]
    except FileNotFoundError:
        print(f"Error: No se encuentra el fichero '{ruta_fichero}'")
        sys.exit(1)

    n = len(lineas_raw)
    
    # si la matriz cuadrada, numero de blancos = numero de negros
    if n > 0 and len(lineas_raw[0]) != n:
        print(f"Error: El tablero no es cuadrado ({n}x{len(lineas_raw[0])}).")
        sys.exit(1)
        
    tablero_inicial = []
    
    # si es negro es 1 si es blanco 0
    for linea in lineas_raw:
        fila = []
        for char in linea:
            if char.upper() == 'X':
                fila.append(1)    # 1 representa Negro
            elif char.upper() == 'O':
                fila.append(0)    # 0 representa Blanco
            else:
                fila.append(None) # None (.)
        tablero_inicial.append(fila)
    return n, tablero_inicial, lineas_raw

def escribir_tablero(stream, n, datos_tablero):
   
    if isinstance(datos_tablero, list):
        for linea in datos_tablero:
            stream.write(linea + "\n")
    else:
        for r in range(n):
            fila_str = ""
            for c in range(n):
                val = datos_tablero.get((r, c))
                if val == 1:
                    fila_str += "X"
                elif val == 0:
                    fila_str += "O"
                else:
                    fila_str += "." 
            stream.write(fila_str + "\n")

def restriccion_no_tres_consecutivos(a, b, c):
    """Devuelve False si los tres valores son idénticos (ej: 0,0,0 o 1,1,1)"""
    return not (a == b == c)

def resolver(fichero_entrada, fichero_salida):
    # 1. Lectura usando listas
    n, tablero_inicial, lineas_raw = leer_instancia(fichero_entrada)
    
    if n % 2 != 0:
        print("Error: El tamaño del tablero debe ser par.")
        sys.exit(1)

    problem = Problem()
    
    # 2. Variables y Dominios
    # Creamos variables para cada coordenada (fila, col) con dominio 0 (O) y 1 (X)
    variables = [(fila, columna) for fila in range(n) for columna in range(n)]
    problem.addVariables(variables, [0, 1])

    # 3. Restricción: Valores Preasignados (Usando la LISTA DE LISTAS)
    for r in range(n):
        for c in range(n):
            valor_fijo = tablero_inicial[r][c]
            # Si la celda no es None, obligamos a la variable a tomar ese valor
            if valor_fijo is not None:
                problem.addConstraint(lambda var, val=valor_fijo: var == val, ((r, c),))

    # 4. Restricción: Igual número de blancos y negros (Suma exacta)
    # La suma debe ser la mitad del tamaño (ej: en 6x6, suma=3)
    objetivo_suma = n // 2
    
    # Por filas
    for fila in range(n):
        vars_fila = [(fila, columna) for columna in range(n)]
        problem.addConstraint(ExactSumConstraint(objetivo_suma), vars_fila)
        
    # Por columnas
    for columna in range(n):
        vars_col = [(fila, columna) for fila in range(n)]
        problem.addConstraint(ExactSumConstraint(objetivo_suma), vars_col)

    # 5. Restricción: No tres consecutivos iguales
    # Se aplica a tríos horizontales y verticales
    
    # Tríos Horizontales (filas)
    for fila in range(n):
        for columna in range(n - 2):
            trio = [(fila, columna), (fila, columna+1), (fila, columna+2)]
            problem.addConstraint(restriccion_no_tres_consecutivos, trio)
            
    # Tríos Verticales (columnas)
    for columna in range(n):
        for fila in range(n - 2):
            trio = [(fila, columna), (fila+1, columna), (fila+2, columna)]
            problem.addConstraint(restriccion_no_tres_consecutivos, trio)

    # 6. Obtener soluciones
    soluciones = problem.getSolutions()
    num_soluciones = len(soluciones)

    # 7. Salida por Pantalla
    print("Instancia a resolver:")
    escribir_tablero(sys.stdout, n, lineas_raw)
    print(f"\n{num_soluciones} soluciones encontradas")

    # 8. Salida a Fichero
    with open(fichero_salida, 'w') as f:
        # Primero la instancia original
        escribir_tablero(f, n, lineas_raw)
        
        # Separador visual (opcional pero recomendado para claridad)
        f.write("\n")
        
        if num_soluciones > 0:
            # Escribir TODAS las soluciones encontradas
            for i, sol in enumerate(soluciones):
                if i > 0:
                    f.write("\n") # Separator between solutions
                escribir_tablero(f, n, sol)
        else:
            f.write("No se encontró solución factible.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python parte-1.py <fichero_entrada> <fichero_salida>")
    else:
        resolver(sys.argv[1], sys.argv[2])