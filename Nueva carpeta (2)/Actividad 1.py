import json

# Cargar los datos del archivo JSON
with open('data.json', 'r', encoding='utf-8') as archivo:
    data = json.load(archivo)

# 1. Imprimir todos los nombres de los equipos
print("Nombres de los equipos:")
for equipo in data["equipos"]:
    print(equipo["nombre"])
# Comentario: Este bloque imprime todos los nombres de los equipos en la lista.

# 2. Mostrar cuántas veces Atlético Nacional ha ganado la Copa Libertadores
for equipo in data["equipos"]:
    if equipo["nombre"] == "Atlético Nacional":
        print(f"\nAtlético Nacional ha ganado {equipo['titulos']['libertadores']} Copa(s) Libertadores.")
# Comentario: Accede a un valor anidado dentro del objeto "titulos".

# 3. Mostrar equipos con más de 10 títulos de liga
print("\nEquipos con más de 10 títulos de liga:")
for equipo in data["equipos"]:
    if equipo["titulos"]["liga"] > 10:
        print(f"{equipo['nombre']} - {equipo['titulos']['liga']} títulos")
# Comentario: Filtra y muestra los equipos que tienen más de 10 títulos de liga.
