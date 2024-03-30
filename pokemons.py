# Info sacada de https://www.pokexperto.net/index2.php
from abc import ABC, abstractmethod
import attacks as at

# LISTA DE HABILIDADES

Impactrueno     = at.Impactrueno().create()
Rayo            = at.Rayo().create()
Ataque_Rapido   = at.Ataque_Rapido().create()
Placaje         = at.Placaje().create()
Tacleada        = at.Tacleada().create()
Supersonico     = at.Supersonico().create()
Drenadoras      = at.Drenadoras().create()
Picotazo        = at.Picotazo().create()
Remolino        = at.Remolino().create()
Tornado         = at.Tornado().create()
Latigo_Cepa     = at.Latigo_Cepa().create()
Somnifero       = at.Somnifero().create()
Lanzallamas     = at.Lanzallamas().create()
Aranazo         = at.Aranazo().create()
Grunido         = at.Grunido().create()
Ascuas          = at.Ascuas().create()
Pistola_Agua    = at.Pistola_Agua().create()
Burbuja         = at.Burbuja().create()
Rayo_Burbuja    = at.Rayo_Burbuja().create()
Tajo_Cruzado    = at.Tajo_Cruzado().create()
Hipercolmillo   = at.Hipercolmillo().create()
Golpe_Cabeza    = at.Golpe_Cabeza().create()
Lodo            = at.Lodo().create()
Bomba_Lodo      = at.Bomba_Lodo().create()
Ataque_Acido    = at.Ataque_Acido().create()
Infortunio      = at.Infortunio().create()
Hidropulso      = at.Hidropulso().create()


# ------------------------ PLANTILLA PARA POKEMONS(STATS) ------------------------

class Pokemon_Blueprint:
    def __init__(self,name:str,ps:int,attack:int,atEspecial:int,defense:int,defEspecial:int,velocity:int,abilities:list[at.Ability_Blueprint]):
        self.name = name 
        self.ps = ps
        self.attack = attack
        self.atEspecial = atEspecial
        self.defense = defense 
        self.defEspecial = defEspecial
        self.velocity = velocity
        self.abilities = abilities

    def __str__(self) -> str:
        return f'\033[1m{self.name}\033[0m\n❤️  PS: {self.ps} - 🎿  Velocidad: {self.velocity} \n🗡️  Ataque: {self.attack} - 🌟  Ataque Especial: {self.atEspecial}\n🛡️  Defensa: {self.defense} - ☔  Defensa Especial {self.defEspecial}\n🌀 Habilidades: {[x.name for x in self.abilities]}'
    
    def status(self):
        print(f' \033[1m {self.name}\033[0m\n  ❤️  PS: {self.ps}')

# ------------------------ FACTORY PATTERN POKEMON ------------------------

class Pokemon_Factory(ABC):
    @abstractmethod
    def create(self):
        pass 

# ------------------------ CREACIÓN DE HABILIDADES A PARTIR DE FACTORY PATTERN ------------------------

class Pikachu(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name='Pikachu',
                                ps=35,
                                attack=55,
                                defense=40,
                                velocity=90,              
                                atEspecial=50,             
                                defEspecial=50,
                                abilities=[Impactrueno,Rayo,Ataque_Rapido,Placaje])

class Caterpie(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Caterpie',
                                ps = 45,
                                attack = 30,
                                defense = 35,
                                velocity = 45,
                                atEspecial = 20,       
                                defEspecial = 20, 
                                abilities = [Placaje,Tacleada,Supersonico,Drenadoras])
 
 
class Pidgeotto(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Pidgeotto',
                                ps = 40,
                                attack = 45,
                                defense = 40,
                                velocity = 56,
                                atEspecial = 35,       
                                defEspecial = 35,
                                abilities = [Picotazo,Remolino,Tornado,Ataque_Rapido])

class Bulbasaur(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Bulbasaur',
                                ps = 45,
                                attack = 49,
                                defense = 49,
                                velocity = 45,
                                atEspecial = 65,      
                                defEspecial = 65, 
                                abilities = [Latigo_Cepa,Drenadoras,Placaje,Somnifero])

class Charmander(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Charmander',
                                ps = 39,
                                attack = 52,
                                defense = 43,
                                velocity = 65,
                                atEspecial = 60,       
                                defEspecial = 50,
                                abilities = [Lanzallamas,Grunido,Aranazo,Ascuas])

class Squirtle(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Squirtle',
                                ps = 44,
                                attack = 48,
                                defense = 65,
                                velocity = 43,
                                atEspecial = 50,       
                                defEspecial = 64, 
                                abilities = [Pistola_Agua,Burbuja,Ataque_Rapido,Placaje])

class Krabby(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Krabby',
                                ps = 30,
                                attack = 105,
                                defense = 90,
                                velocity = 50,
                                atEspecial = 25,       
                                defEspecial = 25, 
                                abilities = [Burbuja,Rayo_Burbuja,Placaje,Tajo_Cruzado])

class Raticate(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Raticate',
                                ps = 30,
                                attack = 56,
                                defense = 35,
                                velocity = 72,
                                atEspecial = 25,       
                                defEspecial = 35,
                                abilities = [Hipercolmillo,Ataque_Rapido,Placaje,Golpe_Cabeza])

class Muk(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Muk',
                                ps = 80,
                                attack = 80,
                                defense = 50,
                                velocity = 25,
                                atEspecial = 40,      
                                defEspecial = 50, 
                                abilities = [Lodo,Bomba_Lodo,Ataque_Acido,Infortunio])

class Kingler(Pokemon_Factory):
    def create(self):
        return Pokemon_Blueprint(name = 'Kingler',
                                ps = 30,
                                attack = 105,
                                defense = 90,
                                velocity = 50,
                                atEspecial = 25,       
                                defEspecial = 25,
                                abilities = [Hidropulso,Rayo_Burbuja,Rayo,Placaje])