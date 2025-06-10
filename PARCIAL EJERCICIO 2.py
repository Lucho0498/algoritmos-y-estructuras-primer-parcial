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
    Superheroe("Black Bolt", "Blackagar Boltagon", False, 1967, "Rey de los Inhumanos con voz destructiva."),
    Superheroe("Medusa", "Medusalith Amaquelin", False, 1965, "Reina de los Inhumanos con cabello prehensil."),
    Superheroe("Lockjaw", "Lockjaw", False, 1965, "Perro teletransportador de los Inhumanos."),
    Superheroe("Quicksilver", "Pietro Maximoff", False, 1964, "Mutante con velocidad sobrehumana."),
    Superheroe("Polaris", "Lorna Dane", False, 1968, "Mutante con poderes magnéticos."),
    Superheroe("Kitty Pryde", "Katherine Pryde", False, 1980, "Mutante capaz de atravesar objetos."),
    Superheroe("Psylocke", "Betsy Braddock", False, 1976, "Mutante con habilidades telepáticas y katana psíquica."),
    Superheroe("Angel", "Warren Worthington III", False, 1963, "Mutante con alas y habilidades de vuelo."),
    Superheroe("Bishop", "Lucas Bishop", False, 1991, "Mutante que absorbe energía y la redirige."),
    Superheroe("Cable", "Nathan Summers", False, 1990, "Mutante con habilidades telequinéticas y experto en combate."),
    Superheroe("Forge", "Forge", False, 1984, "Mutante inventor con capacidad tecnológica avanzada."),
    Superheroe("Havok", "Alex Summers", False, 1969, "Mutante con poderes de plasma."),
    Superheroe("Domino", "Neena Thurman", False, 1992, "Mercenaria con habilidades de suerte."),
    Superheroe("Sunfire", "Shiro Yoshida", False, 1970, "Mutante japonés con poder de fuego."),
    Superheroe("Northstar", "Jean-Paul Beaubier", False, 1979, "Mutante con supervelocidad y vuelo."),
    Superheroe("Aurora", "Jeanne-Marie Beaubier", False, 1979, "Hermana de Northstar con habilidades similares."),
    Superheroe("Nightcrawler", "Kurt Wagner", False, 1975, "Mutante teletransportador."),
    Superheroe("Legion", "David Haller", False, 1985, "Mutante con múltiples personalidades, cada una con poderes distintos."),
    Superheroe("Jubilee", "Jubilation Lee", False, 1989, "Mutante con explosiones de luz."),
    Superheroe("Blink", "Clarice Ferguson", False, 1994, "Mutante con habilidades de teletransportación."),
    Superheroe("Sentry", "Robert Reynolds", False, 2000, "Superhéroe con el poder de mil soles."),
    Superheroe("Nova", "Richard Rider", False, 1976, "Miembro de la fuerza Nova con habilidades cósmicas."),
    Superheroe("Iron Fist", "Danny Rand", False, 1974, "Experto en artes marciales con energía mística."),
    Superheroe("Colleen Wing", "Colleen Wing", False, 1974, "Maestra de la espada aliada de Iron Fist."),
    Superheroe("Misty Knight", "Mercedes Knight", False, 1975, "Detective con brazo cibernético."),
    Superheroe("Moon Girl", "Lunella Lafayette", False, 2015, "Niña genio con un T-Rex como compañero."),
    Superheroe("Devil Dinosaur", "Devil Dinosaur", False, 1978, "Dinosaurio rojo con inteligencia avanzada."),
    Superheroe("America Chavez", "America Chavez", False, 2011, "Héroe con super fuerza y capacidad de viajar entre dimensiones."),
    Superheroe("Echo", "Maya Lopez", False, 1999, "Guerrera sorda con habilidades de imitación."),
    Superheroe("X-23", "Laura Kinney", False, 2003, "Clon de Wolverine con garras de adamantium."),
    Superheroe("Professor X", "Charles Xavier", False, 1963, "Líder de los X-Men con poderes telepáticos."),
    Superheroe("Adam Warlock", "Adam Warlock", False, 1967, "Ser cósmico creado artificialmente."),
    Superheroe("Gladiator", "Kallark", False, 1977, "Guerrero Shi'ar con habilidades sobrehumanas."),
    Superheroe("Kang el Conquistador", "Nathaniel Richards", True, 1963, "Viajero del tiempo y enemigo de los Vengadores."),
    Superheroe("High Evolutionary", "Herbert Wyndham", True, 1966, "Científico obsesionado con la evolución."),
    Superheroe("Fin Fang Foom", "Fin Fang Foom", True, 1961, "Dragón alienígena con habilidades destructivas."),
    Superheroe("Arcade", "Arcade", True, 1978, "Villano que usa trampas mortales."),
    Superheroe("Bullseye", "Lester", True, 1976, "Asesino con precisión perfecta."),
    Superheroe("Blackheart", "Blackheart", True, 1989, "Hijo demoníaco de Mephisto."),
    Superheroe("Abomination", "Emil Blonsky", True, 1967, "Enemigo de Hulk con habilidades similares."),
    Superheroe("Omega Red", "Arkady Rossovich", True, 1992, "Mutante con tentáculos letales."),
    Superheroe("M.O.D.O.K.", "George Tarleton", True, 1967, "Villano con inteligencia sobrehumana."),
    Superheroe("Sauron", "Karl Lykos", True, 1969, "Mutante con apariencia de pterodáctilo."),
    Superheroe("Black Cat", "Felicia Hardy", False, 1979, "Ladrona con habilidades de suerte."),
    Superheroe("Shocker", "Herman Schultz", True, 1967, "Villano de Spider-Man con guantes vibratorios."),
    Superheroe("Scorpion", "Mac Gargan", True, 1964, "Enemigo de Spider-Man con traje de escorpión."),
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