import random
#MI COMPAÑERO TUVO PROBLEMAS CON GITHUB, PERO ME AYUDÓ EN EL PROYECTO. LO SUBIRÉ YO EN SU TOTALIDAD POR FACILIDAD. 

#Definimos la función que encuentra aleatoriamente un número entre 8 y 30
#1. Función generadora de numeros aleatorios entre 8 y 30.
def generar_n():
    return random.randint(8, 30)

#La siguiente función va a vaildar el formato solicitado

#Se encuentra k con un bucle infinito que para hasta que no encuentra más "a´s" en el primer tramo de cadena
#Se define l variable i para iterar y contar la cantidad de veces que se cumple cadena[i] == 'a', que es lo mismo
#que el numero de a´s = k. Pasa lo mismo para "s", se empieza a iterar definiendo j = i, se empieza desde el siguiente
#caractér después de k, (hay que tener en cuenta como se manejan los índices en las cadenas).
# para el n, numero de veces de a al final de la cadena se define como el resto de cadena después del último caracter en s
# luego se verifica si todos los caraccteres son efectivamente letreas "a", que hagan cumplir la estructura de la cadena que 
#pertenece al lenguaje.
#Al final la función hace una verificación de si (k+s) = n mod(3), retornando un booleano: True o False. 
def validar_formato_cadena(cadena, n):
    i = 0
    while i < len(cadena) and cadena[i] == 'a':
        i += 1
    k = i

    j = i
    while j < len(cadena) and cadena[j] == 'b':
        j += 1
    s = j - i

    resto = cadena[j:]
    if not all(c == 'a' for c in resto):
        return False
    final_a = len(resto)
    #Se verifia longitud de cadena 
    if k + s + final_a < n:
        print("La cadena es más pequeña que n") 
        return False
    else:
        return (k + s) % 3 == final_a % 3

# 3. Divide la cadena en u, v, x de acuerdo a la estructura del lenguaje
def dividir_cadena(cadena, n):
     #En esta función usamos la lógica de la función anterior para dividir la cadena en u,v,x.
    i = 0
    while i < len(cadena) and cadena[i] == 'a':
        i += 1
    k = i
    u = cadena[:k]

    j = i
    while j < len(cadena) and cadena[j] == 'b':
        j += 1
    s = j - i
    v = cadena[k:j]
    x = cadena[j:]

    if u + v + x == cadena and v != "" and len(u + v) <= n:
        print("División correcta: u = '{}', v = '{}', x = '{}'".format(u, v, x))
        return u, v, x
    else:
        print("División inválida según las reglas.")
        return None, None, None

# 4. Verificamos si una cadena pertenece a L
def pertenece_a_L(w, n):
    return validar_formato_cadena(w, n)

# 5. Construimos una nueva cadena z = u + v*m + x que bombea v.
def construir_cadena(u, v, x, m):
    return u + v * m + x

# 6. Lógica principal del juego
def main():
    print("Bienvenido al juego del lema de bombeo")
    n = generar_n()
    print(f"Número aleatorio entre 8 y 30 generado (n): {n}")

    while True:
        cadena = input("Ingresa una cadena sobre {a, b} de longitud ≥ n que pertenezca al lenguaje L: ").strip()# usamos strip para omitir espacios, por si hay algun error humano.
        if validar_formato_cadena(cadena, n): #Usamos la función de validación de formato, es decir, si pertenece a L
            print("La cadena pertenece al lenguaje L.")
            break
        else:
            print("La cadena no cumple con las condiciones del lenguaje L. Intenta nuevamente.")

    # Paso 2: Dividir cadena
    u, v, x = dividir_cadena(cadena, n)
    if u is None:
        print("No se pudo dividir la cadena correctamente. Finalizando juego.")
        return

    # Paso 3: Solicitar valor de m
    while True: #Bluce infinito que solicita un numero natural >=0, para cuando se ingrese un valor que cumple la condición. 
        try:
            m = int(input("Ingresa un número natural m (puede ser 0): "))
            if m >= 0:
                break
            else:
                print("Debe ser un número natural (mayor o igual que 0).")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número natural.")
     # Paso 4: Generar nueva cadena z y validar si pertenece a L
    z = construir_cadena(u, v, x, m) # Se usa la función de construcción de nueva cadena con los valores, u,v y x que obtuvimos antes, esta vez bombeando v m veces.
    print(f"Cadena generada z = u·v^{m}·x = '{z}'")

    if pertenece_a_L(z, n):
        print("¡GANASTE! La cadena z pertenece al lenguaje L.")
    else:
        print("La máquina gana. La cadena z NO pertenece al lenguaje L.")
    
    #MODIFICACIONES PARA 90% DE VICTORIAS DE MÁQUINA

    #-------------------------------------------------------------------------------------------------------------------------------
    t = generar_n()
    print(f"Número aleatorio entre 8 y 30 generado (n): {t}")
    while True:
        cadena_casomalo = input("Ingresa una cadena sobre {a, b} de longitud ≥ n que pertenezca al lenguaje L: ").strip()
        if validar_formato_cadena(cadena_casomalo, t):
            print("La cadena pertenece al lenguaje L.")
            break
        else:
            print("La cadena no cumple con las condiciones del lenguaje L. Intenta nuevamente.")    

    while True:
        try:
            p = int(input("Ingresa un número natural m (puede ser 0): "))
            if p >= 0:
                pstr = str(p)
                p = int(pstr[-1])#definimos p como el último dígito.
                if p != 1: # Si es distinto de 1 definimos p=0 así k+s = k(distinto del orignial, porque ya sabiamos que v no es vacío)y 
                    #la congruencia de modulos no se cumpliría, o en el caso que K sea multiplo de n, igualmente k+s sería más pequeño que n, ganando la máquina.
                    #Aquí solo hay 1/10 de probabilidad de ganar y es cuando se bombea con 1 y la cadena queda igua
                    p = 0
                    break
                else:
                    p = 1 #Si p = 1, entonces la cadena al ser bombeada quedaría exacatamente igual, y como antes de bombearla ya sabíamos que pertenecía a L,
                    #al ser bombeada con P=1, también pertenece a L.
                    break  
            else:
                print("Debe ser un número natural (mayor o igual que 0).")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número natural.")

    u, v, x = dividir_cadena(cadena_casomalo, t)
    z = construir_cadena(u, v, x, int(p))
    print(f"Cadena generada z = u·v^{p}·x = '{z}'")
    print("Prueba 90%")
    if pertenece_a_L(z, t):
        print("¡GANASTE! La cadena z pertenece al lenguaje L.")
    else:
        print("La máquina gana. La cadena z NO pertenece al lenguaje L.")


#Pruebas automáticas. Este código de pruebas lo obtuvimos de chatgpt, pero comprendemos en totalidad la lógica implementada.
def generar_cadena_valida(n):
    #En este bucle se generan las n cadenas aleatorias.
    while True:
        k = random.randint(1, n // 2) # se omiten los decimales al dividir con // y se manejan valore pequeños para facilidad, si cadena
        s = random.randint(1, n // 2) # termina siendo más pequeña que n, el bucle se repite igualmente. 
        n_mod = (k + s) % 3
        for extra in range(n, n + 10): #Se itera en un rango determinado n + 10 para encontrar a x, ultima subcadena
            if extra % 3 == n_mod:# realizando la verificación de modulo 3 de x o subcadena final con n_mod que es modelo de k+s.
                n_final = extra 
                break
        if k + s + n_final >= n: # condiciona a la cadena a ser mayor a n, si no se cumple se repite el proceso, por el bucle definido.
            cadena = 'a' * k + 'b' * s + 'a' * n_final
            return cadena # Se construye la cadena y se devuelve. 

def prueba_automatica(iteraciones=100):
    print("\nIniciando prueba automática del programa...\n")
    exitos = 0
    for _ in range(iteraciones): # Se itera 100 veces de prueba. 
        n = generar_n()
        cadena = generar_cadena_valida(n) #Se generan las 100 cadenas válidas. 

        if not validar_formato_cadena(cadena, n): # Se verifica si las cadenas no cumplen condiciones. No debería ejecutarse esta línea
            print(f"Error: Cadena generada inválida para n={n}: {cadena}") #si todo está bien.
            continue

        u, v, x = dividir_cadena(cadena, n) #División de la cadena y verificación de propiedades. 
        if not v or u is None:
            print(f"Error en división para cadena: {cadena}")
            continue

        m = random.randint(0, 5) #Se simula la elección de m de bombeo de 0 a 5 para facilidad.
        z = construir_cadena(u, v, x, m) # Se bombea m veces la cadena
        if pertenece_a_L(z, n): #Se verifica si después de bombear, sigue perteneciendo a L.
            exitos += 1 #Variable de conteo de exitos. 

    #Impresión de resultados obtenidos.
    print(f"\nResultado: {exitos} de {iteraciones} cadenas bombeadas siguen en el lenguaje L.")
    print(f"Precisión (usuario gana): {exitos / iteraciones * 100:.2f}%")
    print(f"Error (máquina gana): {(1 - exitos / iteraciones) * 100:.2f}%\n")



if __name__ == "__main__":
    main()
   
    prueba_automatica(100)
