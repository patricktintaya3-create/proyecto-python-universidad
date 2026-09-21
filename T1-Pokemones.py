import random
def crearEntrenador(tupla):
    
    nombre_entrenador = input("Escribe el nombre del nuevo entrenador: ").strip()
    nombre_pokemon = input("Escribe el nombre del Pokemon nuevo: ").strip()
 
    ataq = random.randint(150, 250)
    life = random.randint(500, 900)
 
    tupla.append((nombre_entrenador, nombre_pokemon, ataq, life))
 
    print(f"\nEl Entrenador '{nombre_entrenador}' y su Pokemon '{nombre_pokemon}' "
          f"estan registrados! (Ataque: {ataq}, Vida: {life})")
 
 
def listaEntrenador(tupla):
   
    if not tupla:
        print("\nNo hay entrenadores aun ,registre uno por favor.")
        return []
 
    lista = list(tupla)
    n = len(lista)
 
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j][2] > lista[j + 1][2]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
    print("\n{:<4}{:<15}{:<15}{:<10}{:<10}".format(
        "#", "Entrenador", "Pokemon", "Ataque", "Vida"))
    print("-" * 54)
    for idx, entrenador in enumerate(lista, start=1):
        print("{:<4}{:<15}{:<15}{:<10}{:<10}".format(
            idx, entrenador[0], entrenador[1], entrenador[2], entrenador[3]))
 
    return lista