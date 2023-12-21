import random

def obtener_palabra():
    
    palabras = ["python", "programacion", "juego", "desarrollo", "computadora", "inteligencia", "edificio"]
    return random.choice(palabras)

def mostrar_tablero(palabra_oculta, letras_adivinadas):
   
    resultado = ""
    for letra in palabra_oculta:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jugar_ahorcado():
   
    print("¡Bienvenido al juego del Ahorcado!")

    palabra_secreta = obtener_palabra().lower()
    letras_adivinadas = set()
    intentos_maximos = 6
    intentos = 0

    while True:
        print("\n" + mostrar_tablero(palabra_secreta, letras_adivinadas))

        if "_" not in mostrar_tablero(palabra_secreta, letras_adivinadas):
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

        letra_usuario = input("Adivina una letra: ").lower()

        if letra_usuario.isalpha() and len(letra_usuario) == 1:
            if letra_usuario in letras_adivinadas:
                print("Ya adivinaste esa letra. ¡Intenta con otra!")
            elif letra_usuario in palabra_secreta:
                letras_adivinadas.add(letra_usuario)
                print("¡Correcto!")
            else:
                intentos += 1
                print("Incorrecto. ¡Te quedan {} intentos!".format(intentos_maximos - intentos))

                if intentos == intentos_maximos:
                    print("¡Perdiste! La palabra era '{}'. ¡Mejor suerte la próxima vez!".format(palabra_secreta))
                    break
        else:
            print("Ingresa una letra válida.")

if __name__ == "__main__":
    jugar_ahorcado()
