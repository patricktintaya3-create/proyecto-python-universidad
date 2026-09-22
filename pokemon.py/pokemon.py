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
def borraPorPokemon(tupla):
    
    if not tupla:
        print("\nError: No hay entrenadores registrados para eliminar.")
        return
 
    lista = list(tupla)
    n = len(lista)
 
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j][3] < lista[indice_menor][3]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
 
    try:
        vida_buscada = int(input("\nIngrese el valor de vida : "))
    except ValueError:
        print("Debe ingresar un número entero.")
        return
 
    izquierda, derecha = 0, len(lista) - 1
    posicion_encontrada = -1
 
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio][3] == vida_buscada:
            posicion_encontrada = medio
            break
        elif lista[medio][3] < vida_buscada:
            izquierda = medio + 1
        else:
            derecha = medio - 1
 
    if posicion_encontrada == -1:
        print(f"No se encontró ningún Pokemon con vida = {vida_buscada}.")
        return
 
    pokemon_a_borrar = lista[posicion_encontrada]
    tupla.remove(pokemon_a_borrar)
    print(f"\nSe eliminó al entrenador '{pokemon_a_borrar[0]}' "
          f"y su Pokemon '{pokemon_a_borrar[1]}' (Vida: {pokemon_a_borrar[3]}).")
 
 
def peleaPokemon(lista):
    
    if len(lista) < 2:
        print("\nSe necesitan al menos 2 Pokemon registrados para pelear.")
        return
 
    lista_ordenada = listaEntrenador(lista)
 
    try:
        num1 = int(input("\nIngrese el número del primer Pokemon: "))
        num2 = int(input("Ingrese el número del segundo Pokemon: "))
    except ValueError:
        print("Debe ingresar números enteros.")
        return
 
    if (num1 == num2 or num1 < 1 or num2 < 1
            or num1 > len(lista_ordenada) or num2 > len(lista_ordenada)):
        print("Selección inválida. Verifique los números ingresados.")
        return
 
    p1 = lista_ordenada[num1 - 1]
    p2 = lista_ordenada[num2 - 1]
 
    golpe1 = p1[2] * random.randint(0, 5)  
    golpe2 = p2[2] * random.randint(0, 5)  
    vida1_final = p1[3] - golpe2
    vida2_final = p2[3] - golpe1
 
    print(f"\n{p1[0]} ({p1[1]}) ataca causando {golpe1} de daño.")
    print(f"{p2[0]} ({p2[1]}) ataca causando {golpe2} de daño.")
    print(f"Vida restante de {p1[1]}: {vida1_final}")
    print(f"Vida restante de {p2[1]}: {vida2_final}")
 
    if vida1_final <= 0 and vida2_final <= 0:
        print(f"\n¡Ambos Pokemon caen derrotados! "
              f"{p1[0]} y {p2[0]} pierden y son eliminados.")
        lista.remove(p1)
        lista.remove(p2)
 
    elif vida1_final == vida2_final:
        print(f"\n¡Empate! Ambos {p1[0]} y {p2[0]} pierden y son eliminados.")
        lista.remove(p1)
        lista.remove(p2)
 
    elif vida1_final > vida2_final:
        print(f"\n¡Gana {p1[0]} con su Pokemon {p1[1]}!")
        lista.remove(p2)
        idx = lista.index(p1)
        lista[idx] = (p1[0], p1[1], p1[2], vida1_final)
 
    else:
        print(f"\n¡Gana {p2[0]} con su Pokemon {p2[1]}!")
        lista.remove(p1)
        idx = lista.index(p2)
        lista[idx] = (p2[0], p2[1], p2[2], vida2_final)
 
 
def menu():
    
    tupla = []  
 
    while True:
        print("\n MENÚ POKEMON ")
        print("===================================")
        print("1. Crear Entrenador")
        print("2. Listar Entrenadores")
        print("3. Borrar por Pokemon")
        print("4. Pelea Pokemon")
        print("5. Fin")
        print("===================================")
 
        opcion = input("Seleccione una opción (1-2-3-4-5): ").strip()
 
        if opcion == "1":
            crearEntrenador(tupla)
        elif opcion == "2":
            listaEntrenador(tupla)
        elif opcion == "3":
            borraPorPokemon(tupla)
        elif opcion == "4":
            peleaPokemon(tupla)
        elif opcion == "5":
            print("\nFIN DEL JUEGO.")
            break
        else:
            print("\nError: Opción inválida. Intente nuevamente.")
 
 
if __name__ == "__main__":
    menu()