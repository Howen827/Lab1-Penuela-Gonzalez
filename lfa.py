import random

def verificar_formato(w):
    """Verifica que la cadena tenga el formato a^k b^s a^m"""
    # Verificar que la cadena solo contiene 'a's y 'b's
    if not all(c in {'a', 'b'} for c in w):
        return False, 0, 0
    
    # Contar las 'a's iniciales (k)
    k = 0
    while k < len(w) and w[k] == 'a':
        k += 1
    
    # Contar las 'b's siguientes (s)
    s = 0
    while k + s < len(w) and w[k + s] == 'b':
        s += 1
    
    # Verificar que el resto son 'a's (m)
    m = len(w) - k - s
    if not all(c == 'a' for c in w[k+s:]):
        return False, 0, 0
    
    return True, k, s

def verificar_lenguaje(w, n, m):
    """Verifica si w ∈ L = {a^k b^s a^m | (k + s) ≡ m mod 3} y len(w) ≥ n"""
    if len(w) < n:
        return False
    
    valido, k, s = verificar_formato(w)
    if not valido:
        return False
    
    # Verificar que hay exactamente m 'a's al final
    if len(w) != k + s + m:
        return False
    
    # Verificar la condición (k + s) ≡ m mod 3
    return (k + s) % 3 == m % 3

def dividir_cadena(w, n):
    """Divide w en u, v, x con |uv| ≤ n y |v| ≥ 1"""
    max_uv = min(n, len(w) - 1)
    if max_uv < 1:
        return w, '', ''
    
    u_end = random.randint(0, max_uv - 1)
    v_end = random.randint(u_end + 1, max_uv)
    
    return w[:u_end], w[u_end:v_end], w[v_end:]

def bombeo(u, v, x, i):
    """Aplica el lema de bombeo i veces"""
    return u + (v * i) + x

def jugar(m=2):
    """Función principal del juego interactivo"""
    print("=== JUEGO DEL LEMA DE BOMBEO ===")
    print(f"Lenguaje L = {{a^k b^s a^{m} | (k + s) ≡ {m} mod 3}}")
    n = random.randint(8, 30)
    print(f"\nLongitud mínima requerida: {n}")
    
    # Paso 1: Obtener cadena válida del usuario
    while True:
        w = input(f"\nIngrese una cadena w con formato a^k b^s a^{m} que cumpla (k+s)≡{m} mod 3: ")
        if verificar_lenguaje(w, n, m):
            break
        print("✖ Cadena no válida. Revise el formato y la condición.")
    
    # Paso 2: Dividir la cadena (con estrategia ganadora)
    u, v, x = dividir_cadena_ganadora(w, n, m)
    print(f"\nDivisión de la cadena:")
    print(f"u = '{u}' (longitud {len(u)})")
    print(f"v = '{v}' (longitud {len(v)})")
    print(f"x = '{x}' (longitud {len(x)})")
    
    # Paso 3: Obtener i del usuario
    while True:
        try:
            i = int(input("\nIngrese un número natural i para el bombeo: "))
            if i >= 0:
                break
            print("i debe ser ≥ 0")
        except ValueError:
            print("Ingrese un número válido")
    
    # Paso 4: Aplicar bombeo y verificar
    z = bombeo(u, v, x, i)
    print(f"\nCadena bombeada: z = '{z}'")
    
    if verificar_lenguaje(z, n, m):
        print("\n¡GANASTE! La cadena bombeada pertenece al lenguaje.")
    else:
        print("\n¡GANÓ LA MÁQUINA! La cadena bombeada no pertenece al lenguaje.")

def dividir_cadena_ganadora(w, n, m):
    """Divide la cadena para que el programa gane el 90% de las veces"""
    if random.random() < 0.9:  # 90% de probabilidad de ganar
        valido, k, s = verificar_formato(w)
        
        # Estrategia: seleccionar v para que al bombear cambie (k + s) mod 3
        if k > 0:  # Tomar parte de las 'a's iniciales
            u_end = random.randint(0, min(k-1, n-1))
            v_end = random.randint(u_end + 1, min(k, n))
        else:  # Tomar parte de las 'b's
            u_end = random.randint(k, min(k + s - 1, n - 1))
            v_end = random.randint(u_end + 1, min(k + s, n))
        
        u = w[:u_end]
        v = w[u_end:v_end]
        x = w[v_end:]
        
        # Asegurar que x tiene exactamente m 'a's
        if not x.endswith('a' * m):
            x = w[-m:]
            v = w[u_end:len(w)-m]
    else:  # 10% de probabilidad de dividir normalmente
        u, v, x = dividir_cadena(w, n)
    
    return u, v, x

def generar_cadena_valida(n, m):
    """Genera una cadena válida para el lenguaje L"""
    # Asegurar (k + s) ≡ m mod 3 y k + s + m ≥ n
    while True:
        k = random.randint(1, max(n - m, 1))
        s = random.randint(1, max(n - k - m, 1))
        if (k + s) % 3 == m % 3:
            break
    return 'a' * k + 'b' * s + 'a' * m

def simular_juego(m=2, verbose=True):
    """Simula un juego completo con usuario automático"""
    n = random.randint(8, 30)
    w = generar_cadena_valida(n, m)
    
    if verbose:
        print(f"\n--- Simulación con n={n}, m={m} ---")
        print(f"Cadena generada: {w} (longitud {len(w)})")
        print(f"k={w.count('a')-m}, s={w.count('b')}, m={m}")
        print(f"Condición: ({w.count('a')-m} + {w.count('b')}) % 3 = {(w.count('a')-m + w.count('b')) % 3}")
    
    if not verificar_lenguaje(w, n, m):
        if verbose: print("Error: Cadena generada no válida")
        return False
    
    u, v, x = dividir_cadena_ganadora(w, n, m)
    i = random.randint(0, 5)
    z = bombeo(u, v, x, i)
    
    if verbose:
        print(f"\nDivisión: u='{u}', v='{v}', x='{x}'")
        print(f"Bombeo con i={i}: z='{z}'")
        print(f"Nuevos valores: k={z.count('a')-m}, s={z.count('b')}")
        print(f"Condición: ({z.count('a')-m} + {z.count('b')}) % 3 = {(z.count('a')-m + z.count('b')) % 3}")
    
    resultado = verificar_lenguaje(z, n, m)
    if verbose:
        print("\nResultado:", "Usuario gana" if resultado else "Máquina gana")
    return resultado

def validar_desempeno(m=2, num_simulaciones=100):
    """Valida el porcentaje de victorias de la máquina"""
    victorias = 0
    for i in range(num_simulaciones):
        if not simular_juego(m, verbose=False):
            victorias += 1
        print(f"Progreso: {i+1}/{num_simulaciones}", end='\r')
    
    print(f"\nResultados con m={m} en {num_simulaciones} simulaciones:")
    print(f"Victorias máquina: {victorias} ({victorias/num_simulaciones*100:.1f}%)")
    print(f"Victorias usuario: {num_simulaciones-victorias} ({(num_simulaciones-victorias)/num_simulaciones*100:.1f}%)")

# Ejecutar el juego interactivo
jugar(m=1)

# Ejecutar simulaciones para validar desempeño
#validar_desempeno(m=2, num_simulaciones=100)