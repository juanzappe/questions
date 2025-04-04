import random
import sys

# Lista de preguntas, respuestas y respuesta correcta (índice), todo junto
questions_data = list(zip(
    [
        "¿Qué función se usa para obtener la longitud de una cadena en Python?",
        "¿Cuál de las siguientes opciones es un número entero en Python?",
        "¿Cómo se solicita entrada del usuario en Python?",
        "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
        "¿Cuál es el operador de comparación para verificar si dos valores son iguales?"
    ],
    [
        ("size()", "len()", "length()", "count()"),
        ("3.14", "'42'", "10", "True"),
        ("input()", "scan()", "read()", "ask()"),
        ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
        ("=", "==", "!=", "===")
    ],
    [1, 2, 0, 3, 1]
))

# Seleccionamos 3 preguntas aleatorias sin repetición
questions_to_ask = random.sample(questions_data, k=3)

# Puntaje jugador
puntaje_usuario = 0

# Recorremos las preguntas seleccionadas
for question, options, correct_index in questions_to_ask:
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    for attempt in range(2):
        try:
            user_input = input("Respuesta: ")
            user_answer = int(user_input) - 1

            if user_answer < 0 or user_answer >= len(options):
                print("Respuesta no válida")
                sys.exit(1)

            if user_answer == correct_index:
                print("¡Correcto!")
                puntaje_usuario = puntaje_usuario + 1
                break
            else:
                puntaje_usuario = puntaje_usuario -0.5
                print("Incorrecto. Intenta de nuevo.")

        except ValueError:
            print("Respuesta no válida")
            sys.exit(1)

    else:
        print("Incorrecto. La respuesta correcta es:")
        print(options[correct_index])

    print()
print("Elpuntaje obtenido es de",puntaje_usuario)
