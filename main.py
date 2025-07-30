# Diccionario de palabras modernas
meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo raro o embarazoso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador o siniestro",
    "AGGRO": "Ponerse agresivo o enojado"
}

print("Diccionario de palabras modernas")
print('Escribe "salir" para terminar.\n')

# Bucle infinito hasta que el usuario escriba "salir"
while True:
    palabra = input("¿Qué palabra quieres aprender? ")

    if palabra.lower() == "salir":
        break

    palabra_mayus = palabra.upper()

    if palabra_mayus in meme_dict:
        print("Significado:", meme_dict[palabra_mayus])
    else:
        print("Esa palabra no está en el diccionario")

print("Gracias por usar el diccionario.")
