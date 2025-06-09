from list_ import List
from queue_ import Queue

class Superheroe:
    def __init__(self, nombre, nombrereal, villano, fechaaparicion, biografia):
        self.nombre = nombre
        self.nombrereal = nombrereal
        self.villano = villano
        self.fechaaparicion = fechaaparicion
        self.biografia = biografia

    def __str__(self):
        tipo = "Villano" if self.villano else "Héroe"
        return f"{self.nombre}, ({self.nombrereal}), {tipo}, Año: {self.fechaaparicion}, Biografia: {self.biografia}"

superheroes = List([
    Superheroe("Thor", "Thor Odinson", False, 1962, "Dios del trueno y protector de Asgard."),
    Superheroe("Hulk", "Bruce Banner", False, 1962, "Científico que se convierte en un gigante verde por la radiación gamma."),
    Superheroe("Spider-Man", "Peter Parker", False, 1962, "Un joven con poderes arácnidos tras ser mordido por una araña."),
    Superheroe("Wolverine", "Logan", False, 1974, "Mutante con garras de adamantium y habilidades regenerativas."),
    Superheroe("Deadpool", "Wade Wilson", False, 1991, "Mercenario bocazas con regeneración sobrehumana."),
    Superheroe("Black Panther", "T'Challa", False, 1966, "Rey de Wakanda con traje de vibranium."),
    Superheroe("Groot", "Groot", False, 1960, "Ser vegetal con habilidades regenerativas."),
    Superheroe("Star-Lord", "Peter Quill", False, 1976, "Líder de los Guardianes de la Galaxia."),
    Superheroe("Gamora", "Gamora", False, 1975, "Hija adoptiva de Thanos y experta en combate."),
    Superheroe("Drax", "Drax el Destructor", False, 1973, "Guerrero que busca vengar a su familia."),
    Superheroe("Doctor Strange", "Stephen Strange", False, 1963, "Hechicero supremo que protege la realidad."),
    Superheroe("Scarlet Witch", "Wanda Maximoff", False, 1964, "Mutante con habilidades de alteración de la realidad."),
    Superheroe("Vision", "Vision", False, 1968, "Android con inteligencia avanzada y el poder de la gema de la mente."),
    Superheroe("Hawkeye", "Clint Barton", False, 1964, "Arquero experto y miembro de los Vengadores."),
    Superheroe("Falcon", "Sam Wilson", False, 1969, "Aliado de Captain America con alas mecánicas."),
    Superheroe("Ant-Man", "Hank Pym", False, 1962, "Científico brillante que descubrió las partículas Pym y fue el Ant-Man original. Fundador de los Vengadores."),
    Superheroe("Wasp", "Hope van Dyne", False, 1963, "Heroína con traje de reducción y alas."),
    Superheroe("Moon Knight", "Marc Spector", False, 1975, "Justiciero con identidad múltiple."),
    Superheroe("Baron Zemo", "Helmut Zemo", True, 1973, "Estratega maestro y enemigo del Capitán América. Líder de los Thunderbolts."),
    Superheroe("Shang-Chi", "Shang-Chi", False, 1973, "Experto en artes marciales."),
    Superheroe("Silver Surfer", "Norrin Radd", False, 1966, "Heraldo de Galactus con poderes cósmicos."),
    Superheroe("Ghost Rider", "Johnny Blaze", False, 1972, "Vengador infernal con cadena mística."),
    Superheroe("Nick Fury", "Nicholas Fury", False, 1963, "Líder de S.H.I.E.L.D."),
    Superheroe("Jessica Jones", "Jessica Jones", False, 2001, "Detective con fuerza sobrehumana."),
    Superheroe("Luke Cage", "Carl Lucas", False, 1972, "Héroe de Harlem con piel indestructible."),
    Superheroe("Mister Fantastic", "Reed Richards", False, 1961, "Líder de los Cuatro Fantásticos con elasticidad."),
    Superheroe("Invisible Woman", "Sue Storm", False, 1961, "Miembro de los Cuatro Fantásticos con poderes de invisibilidad."),
    Superheroe("Human Torch", "Johnny Storm", False, 1961, "Miembro de los Cuatro Fantásticos con control del fuego y un suit (traje) especial ignifugo."),
    Superheroe("The Thing", "Ben Grimm", False, 1961, "Miembro de los Cuatro Fantásticos con cuerpo de roca."),
    Superheroe("Captain Marvel", "Carol Danvers", False, 1968, "Heroína con poderes cósmicos."),
    Superheroe("Venom", "Eddie Brock", True, 1984, "Simbionte con habilidades monstruosas."),
    Superheroe("Carnage", "Cletus Kasady", True, 1992, "Versión más letal de Venom."),
    Superheroe("Ultron", "Ultron", True, 1968, "IA con la misión de extinguir la humanidad."),
    Superheroe("Doctor Doom", "Victor Von Doom", True, 1962, "Dictador de Latveria y genio en tecnología."),
    Superheroe("Magneto", "Erik Lehnsherr", True, 1963, "Mutante con control del magnetismo."),
    Superheroe("Loki", "Loki", True, 1949, "Dios del engaño y hermano de Thor."),
    Superheroe("Red Skull", "Johann Schmidt", True, 1941, "Supervillano nazi y enemigo de Captain America."),
    Superheroe("Kingpin", "Wilson Fisk", True, 1967, "Líder criminal con poder sobre la mafia."),
    Superheroe("Taskmaster", "Desconocido", True, 1980, "Villano con memoria muscular."),
    Superheroe("Dormammu", "Dormammu", True, 1967, "Ser interdimensional con poderes oscuros."),
    Superheroe("Mephisto", "Mephisto", True, 1968, "Demonio con habilidades mágicas."),
    Superheroe("Green Goblin", "Norman Osborn", True, 1964, "Villano de Spider-Man con tecnología avanzada."),
    Superheroe("Sandman", "Flint Marko", True, 1963, "Villano con habilidades para transformar su cuerpo en arena."),
    Superheroe("Mysterio", "Quentin Beck", True, 1964, "Ilusionista y enemigo de Spider-Man."),
    Superheroe("Electro", "Max Dillon", True, 1964, "Villano con poderes eléctricos."),
    Superheroe("Juggernaut", "Cain Marko", True, 1965, "Ser con fuerza imparable."),
    Superheroe("Sabretooth", "Victor Creed", True, 1977, "Enemigo de Wolverine con habilidades similares."),
    Superheroe("Rocket Raccoon", "Rocket", False, 1976, "Mapache modificado genéticamente con habilidades en combate, estrategia y armamento pesado. Miembro clave de los Guardianes de la Galaxia."),
    Superheroe("Kraven el Cazador", "Sergei Kravinoff", True, 1964, "Cazador obsesionado con derrotar a Spider-Man."),
])


def order_by_nombre(superheroes):
    return superheroes.nombre

def order_by_nombrereal(superheroes):
    return superheroes.nombrereal

def order_by_fechaaparicion(superheroes):
    return superheroes.fechaaparicion


superheroes.add_criterion("nombre", order_by_nombre)

superheroes.add_criterion("nombrereal", order_by_nombrereal)

superheroes.add_criterion("fechaaparicion", order_by_fechaaparicion)

def ordenarpornombre(superheroes):
    superheroes.sort_by_criterion("nombre")
    for i in superheroes:
        print(i)

ordenarpornombre(superheroes)

def encontrarposicion(superheroes, personaje):
    i = 0
    while i < len(superheroes):
        if superheroes[i].nombre == personaje:
            return i
        i += 1
    return -1

posicionthing = encontrarposicion(superheroes, "The Thing")
posicionrocket = encontrarposicion(superheroes, "Rocket Raccoon")

print(f"The Thing está en la posición: {posicionthing}")
print(f"Rocket Raccoon está en la posición: {posicionrocket}")

def Listarvillanos(superheroes):
    for superheroe in superheroes:
        if superheroe.villano == True:
            print(f"{superheroe.nombre} es villano")
            
Listarvillanos(superheroes)

def PasarVillanosAunaCola(superheroes):
    cola = Queue()
    for superheroe in superheroes:
        if superheroe.villano == True and superheroe.fechaaparicion < 1980:
            cola.arrive(superheroe.nombre)
    return cola

colavillanos = PasarVillanosAunaCola(superheroes)
colavillanos.show()

def Superheroescuyonombreempiezacon(superheroes):
    for superheroe in superheroes:
        if superheroe.nombre[0:2] in ["Bl", "My"]:
            print(superheroe.nombre)
        elif superheroe.nombre[0] in ["G", "W"]:
            print(superheroe.nombre)

Superheroescuyonombreempiezacon(superheroes)

def listarporordennombrereal(superheroes):
    superheroes.sort_by_criterion("nombrereal")
    for i in superheroes:
        print(i)

listarporordennombrereal(superheroes)

def listarporordendefecha(superheroes):
    superheroes.sort_by_criterion("fechaaparicion")
    for i in superheroes:
        print(i)
        
listarporordendefecha(superheroes)

def modificarnombreScottLang(superheroes):
    index = superheroes.search("Ant-Man", "nombre")
    if index is not None:
        superheroes[index].nombrereal = "Scott Lang"

modificarnombreScottLang(superheroes)

def Mostrarsegunbiografia(superheroes):
    for superheroe in superheroes:
        if "suit" in superheroe.biografia or "time-traveling" in superheroe.biografia:
            print(superheroe.nombre)

print("personaje que en su biografia menciona suit o time-traveling:")
Mostrarsegunbiografia(superheroes)

def EliminarElectroZemo():
    index = superheroes.search("Electro", "nombre")
    if index is not None:
        superheroes.delete_value("Electro", "nombre")
    indexZemo =superheroes.search("Baron Zemo", "nombre")
    if indexZemo is not None:
        superheroes.delete_value("Baron Zemo", "nombre")

EliminarElectroZemo()