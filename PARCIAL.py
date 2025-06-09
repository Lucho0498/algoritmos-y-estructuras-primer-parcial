
superheroes = [
    "Black Widow",
    "Scarlett Witch",
    "Vision",
    "Shang Chi",
    "Thor",
    "Capitana Marvel",
    "Groot",
    "Star-Lord",
    "Bestia",
    "Wolverine",
    "Tormenta",
    "Capitan America",
    "Ciclope",
    "Drax",
    "Gamora"
]

def BuscarCapitanAmerica(superheroes, posicion = 0):
    if posicion >= len(superheroes):
        return f"Capitan America no esta en la lista"
    if superheroes[posicion] == "Capitan America":
        return f"Capitan America está en la lista."
    return BuscarCapitanAmerica(superheroes, posicion + 1)

print(BuscarCapitanAmerica(superheroes))

def MostrarLista(superheroes, posicion=0):
    if posicion >= len(superheroes):
        return
    print(superheroes[posicion])  
    MostrarLista(superheroes, posicion + 1)  

print()
print("lista de superheroes:")
MostrarLista(superheroes)
