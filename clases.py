class Animal ():
    """
    Se establece una clase que represente a animales.
    Sus atributos seran nombre, raza, edad y peso.
    Sus metodos seran comer, caminar y dormir.
    """
    def __init__(self, nombre: str, raza: str, edad: int, peso: float) -> None:
        self.nombre = nombre.capitalize()
        self.raza = raza.capitalize()
        self.edad = edad
        self.peso = peso

    def comer (self):
        return f"El animal {self.nombre}, raza {self.raza} esta comiendo"
    
    def caminar (self):
        return f"El animal {self.nombre}, raza {self.raza} esta caminando"
    
    def dormir (self):
        return f"El animal {self.nombre}, raza {self.raza} esta durmiendo"
        
#Representacion de dos objetos (perro y gato) pertenecientes a la clase Animal
perro = Animal("Brando", "San Bernardo", 3, 30)
gato = Animal ("Roll", "Persa", 4, 3)


#Ejemplo de uso de metodos de clase para ambos objetos
print(perro.comer ())        
print(gato.dormir ())