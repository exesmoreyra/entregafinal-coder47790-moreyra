import random

def obtener_opcion_usuario():
  while True:
        opcion = input("Elige Piedra, Papel o Tijera: ").lower()
        if opcion in ["piedra", "papel", "tijera"]:
            return opcion
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def obtener_opcion_computadora():
    
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(opcion_usuario, opcion_computadora):
    
    if opcion_usuario == opcion_computadora:
        return "Empate"
    elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
         (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
         (opcion_usuario == "tijera" and opcion_computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar_piedra_papel_tijera():
  
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")

    while True:
        opcion_usuario = obtener_opcion_usuario()
        opcion_computadora = obtener_opcion_computadora()

        print(f"Tú elegiste: {opcion_usuario}")
        print(f"La computadora eligió: {opcion_computadora}")

        resultado = determinar_ganador(opcion_usuario, opcion_computadora)
        print(f"Resultado: {resultado}\n")

        jugar_nuevamente = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_nuevamente != 's':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break

if __name__ == "__main__":
    jugar_piedra_papel_tijera()
