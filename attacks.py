# Info sacada de https://www.pokexperto.net/index2.php
from abc import ABC, abstractmethod

# ------------------------ PLANTILLA PARA HABILIDADES(STATS) ------------------------
class Ability_Blueprint:
    def __init__(self,name:str,type:str,power:int,precision:int):
        self.name = name 
        self.type = type
        self.power = power 
        self.precision = precision

    def __str__(self) -> str:
        return f'{self.name}\nType: {self.type}\nPower: {self.power}\nPrecision: {self.precision}'

# ------------------------ FACTORY PATTERN HABILIDADES ------------------------

class Ability_Factory(ABC):
    @abstractmethod
    def create(self):
        pass 

# ------------------------ CREACIÓN DE HABILIDADES A PARTIR DE FACTORY PATTERN ------------------------

class Impactrueno (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Impactrueno',
                                        type='Magic',
                                        power=40,
                                        precision=100)

class Rayo (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Rayo',
                                        type='Magic',
                                        power=90,
                                        precision=100)

class Ataque_Rapido (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Ataque Rápido',
                                        type='Físico',
                                        power=40,
                                        precision=100) 
      
class Placaje (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Placaje',
                                        type='Físico',
                                        power=40,
                                        precision=100)
    
class Tacleada (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Tacleada',
                                        type='Físico',
                                        power=35,
                                        precision=100)
    
#Este ataque SOLO genera confusión 
class Supersonico (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Supersónico',
                                        type='Magíco',
                                        power=55,
                                        precision=55)
    
#Este ataque roba vida 
class Drenadoras (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Drenadoras',
                                        type='Magíco',
                                        power=40,
                                        precision=90)

class Picotazo (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Picotazo',
                                        type='Físico',
                                        power=35,
                                        precision=100)
    
#Este ataque obliga al enemigo a intercambiar pokemon
class Remolino (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Remolino',
                                        type='Físico',
                                        power=60,
                                        precision=75)

class Tornado (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Tornado',
                                        type='Magíco',
                                        power=40,
                                        precision=100)

class Latigo_Cepa (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Látigo Cepa',
                                        type='Magíco',
                                        power=45,
                                        precision=100)

#Este ataque SOLO duerme al enemigo
class Somnifero (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Somnifero',
                                        type='Magíco',
                                        power=45,
                                        precision=75)

class Lanzallamas (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Lanzallamas',
                                        type='Magíco',
                                        power=90,
                                        precision=100)
    
#Este ataque SOLO baja la defensa
class Grunido (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Gruñido',
                                        type='Físico',
                                        power=55,
                                        precision=55)

class Aranazo (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Arañazo',
                                        type='Físico',
                                        power=40,
                                        precision=100)

class Ascuas (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Placaje',
                                        type='Físico',
                                        power=40,
                                        precision=100)

class Pistola_Agua (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Pistola_Agua',
                                        type='Magíco',
                                        power=40,
                                        precision=100)

#Este ataque reduce la velocidad
class Burbuja (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Burbuja',
                                        type='Magíco',
                                        power=45,
                                        precision=100)

class Rayo_Burbuja (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Rayo Burbuja',
                                        type='Magíco',
                                        power=65,
                                        precision=100)
    
#Este ataque tiene gran posibilidad de critico
class Tajo_Cruzado (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Tajo Cruzado',
                                        type='Físico',
                                        power=40,
                                        precision=100)

#Este ataque hace retroceder
class Hipercolmillo (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Hipercolmillo',
                                        type='Físico',
                                        power=80,
                                        precision=90)

#Este ataque hace retroceder
class Golpe_Cabeza (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Golpe Cabeza',
                                        type='Físico',
                                        power=70,
                                        precision=100)
    
#Nada se llama así xd
class Lodo (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Lodo',
                                        type='Mágico',
                                        power=30,
                                        precision=100)

#Este ataque envenena
class Bomba_Lodo (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Bomba Lodo',
                                        type='Mágico',
                                        power=90,
                                        precision=100)

#Nada se llama así xd
class Ataque_Acido (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Ataque Ácido',
                                        type='Mágico',
                                        power=40,
                                        precision=100)

class Infortunio (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Infortunio',
                                        type='Mágico',
                                        power=65,
                                        precision=100)

class Hidropulso (Ability_Factory):
    def create(self):
        return Ability_Blueprint(name='Hidropulso',
                                        type='Mágico',
                                        power=60,
                                        precision=100)