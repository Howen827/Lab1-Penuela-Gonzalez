def es_valida_en_lenguaje(s):
    """
    Verifica si una cadena pertenece al lenguaje L = { aⁿbⁿ | n ≥ 1 }
    """
    if set(s) - {'a', 'b'}:
        return False  # contiene otros caracteres

    n = len(s)
    i = 0
    while i < n and s[i] == 'a':
        i += 1
    num_a = i
    num_b = n - i

    return num_a > 0 and num_a == num_b and all(c == 'b' for c in s[i:])


def juego_lema_de_bombeo():
    print("🎮 Bienvenido al Juego del Lema de Bombeo 🎮")
    print("Lenguaje objetivo: L = { aⁿbⁿ | n ≥ 1 } (no regular)")
    print("Intenta violar la propiedad del lenguaje bombeando cadenas...\n")

    cadena_original = input("Ingresa una cadena que pertenezca al lenguaje (ej: aabb): ")

    if not es_valida_en_lenguaje(cadena_original):
        print("❌ Esa cadena NO pertenece al lenguaje L = { aⁿbⁿ }")
        return

    print("✅ La cadena pertenece al lenguaje.")

    print("\nAhora elige una forma de dividir la cadena en xyz, donde |xy| ≤ p, |y| ≥ 1")
    p = int(input("Elige un valor para p (ej: 2): "))

    if p >= len(cadena_original):
        print("❌ p debe ser menor que la longitud de la cadena.")
        return

    print(f"La cadena tiene longitud {len(cadena_original)}. Vamos a dividirla en xyz con |xy| ≤ {p} y |y| ≥ 1.")

    x = input("Ingresa la parte x: ")
    y = input("Ingresa la parte y: ")
    z = input("Ingresa la parte z: ")

    if x + y + z != cadena_original:
        print("❌ La concatenación de x, y, z no coincide con la cadena original.")
        return
    if len(x + y) > p:
        print("❌ La condición |xy| ≤ p no se cumple.")
        return
    if len(y) < 1:
        print("❌ La condición |y| ≥ 1 no se cumple.")
        return

    i = int(input("Elige un valor para i (cuántas veces bombear y): "))

    nueva_cadena = x + y * i + z
    print(f"\n🔁 Cadena bombeada con i = {i}: {nueva_cadena}")

    if es_valida_en_lenguaje(nueva_cadena):
        print("✅ La cadena bombeada aún pertenece al lenguaje.")
    else:
        print("❌ La cadena bombeada NO pertenece al lenguaje. ¡Has demostrado que no es regular!")

if __name__ == "__main__":
    juego_lema_de_bombeo()
