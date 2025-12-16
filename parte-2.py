import sys

def resolver(v1, v2, fichero_entrada, fichero_salida):

    
    try: 
        vertice_1 = int(v1)
        vertice_2 = int(v2)
    except ValueError:
        print(f"Error: los vértices deben ser int")
        sys.exit(1)


    lista_vertices, lista_arcos = leer_instancia(fichero_entrada)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python parte-2.py vértice1 vértice2 <nombre-del-mapa> <fichero-salida>")
    else:
        resolver(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


