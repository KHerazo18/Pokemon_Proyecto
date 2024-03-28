# Info sacada de https://www.pokexperto.net/index2.php

class stats: 
    nombre = ''
    tipo = ''  
    potencia = 0
    precision = 0

    def __str__(self):
        pass

class Impactrueno (stats):
    nombre = 'Impactrueno'
    tipo = 'Mágico'
    potencia = 40
    precision = 100

class Rayo (stats):
    nombre = 'Rayo'
    tipo = 'Mágico'
    potencia = 90
    precision = 100

class Ataque_Rapido (stats):
    nombre = 'Ataque Rápido'
    tipo = 'Físico'
    potencia = 40
    precision = 100

class Placaje (stats):
    nombre = 'Placaje'
    tipo = 'Físico'
    potencia = 1000
    precision = 100

class Tacleada (stats):
    nombre = 'Tacleada'
    tipo = 'Físico'
    potencia = 35
    precision = 100

#Este ataque solo genera confusión 
class Supersonico (stats):
    nombre = 'Supersónico'
    tipo = 'Mágico'
    potencia = 55
    precision = 55

#Este ataque roba vida 
class Drenadoras (stats):
    nombre = 'Drenadoras'
    tipo = 'Mágico'
    potencia = 40
    precision = 90

class Picotazo (stats):
    nombre = 'Picotazo'
    tipo = 'Físico'
    potencia = 35
    precision = 100

#Este ataque obliga al enemigo a intercambiar pokemon
class Remolino (stats):
    nombre = 'Remolino'
    tipo = 'Físico'
    potencia = 60
    precision = 75

class Tornado (stats):
    nombre = 'Tornado'
    tipo = 'Mágico'
    potencia = 40
    precision = 100

class Latigo_Cepa (stats):
    nombre = 'Latigo Cepa'
    tipo = 'Mágico'
    potencia = 45
    precision = 100

#Este ataque solo duerme al enemigo
class Somnifero (stats):
    nombre = 'Somnifero'
    tipo = 'Mágico'
    potencia = 45
    precision = 75

class Lanzallamas (stats):
    nombre = 'Lanzallamas'
    tipo = 'Mágico'
    potencia = 90
    precision = 100

#Este ataque baja la defensa
class Grunido (stats):
    nombre = 'Gruñido'
    tipo = 'Físico'
    potencia = 55
    precision = 55

class Aranazo (stats):
    nombre = 'Arañazo'
    tipo = 'Físico'
    potencia = 40
    precision = 100

class Ascuas (stats):
    nombre = 'Ascuas'
    tipo = 'Mágico'
    potencia = 40
    precision = 100

class Pistola_Agua (stats):
    nombre = 'Pistola Agua'
    tipo = 'Mágico'
    potencia = 40
    precision = 100

#Este ataque reduce la velocidad
class Burbuja (stats):
    nombre = 'Burbuja'
    tipo = 'Mágico'
    potencia = 45
    precision = 100

class Rayo_Burbuja (stats):
    nombre = 'Rayo Burbuja'
    tipo = 'Mágico'
    potencia = 65
    precision = 100

#Este ataque tiene gran posibilidad de critico
class Tajo_Cruzado (stats):
    nombre = 'Tajo Cruzado'
    tipo = 'Físico'
    potencia = 100
    precision = 80

#Este ataque hace retroceder
class Hipercolmillo (stats):
    nombre = 'Hipercolmillo'
    tipo = 'Físico'
    potencia = 80
    precision = 90

#Este ataque hace retroceder
class Golpe_Cabeza (stats):
    nombre = 'Golpe Cabeza'
    tipo = 'Físico'
    potencia = 70
    precision = 100

#Nada se llama así xd
class Lodo (stats):
    nombre = 'Lodo'
    tipo = 'Mágico'
    potencia = 30
    precision = 100

#Este ataque envenena
class Bomba_Lodo (stats):
    nombre = 'Bomba Lodo'
    tipo = 'Mágico'
    potencia = 90
    precision = 100

#Nada se llama así xd
class Ataque_Acido (stats):
    nombre = 'Ataque Ácido'
    tipo = 'Mágico'
    potencia = 40
    precision = 100

class Infortunio (stats):
    nombre = 'Infortunio'
    tipo = 'Mágico'
    potencia = 65
    precision = 100

class Hidropulso (stats):
    nombre = 'Hidropulso'
    tipo = 'Mágico'
    potencia = 60
    precision = 100

class Attacks:
    def __init__(self, atq:stats):
        super().__init__()
        self.atq = atq 

    def __str__(self):
        return f' \033[1m{self.atq.nombre}\033[0m\n Tipo: {self.atq.tipo}\n Potencia: {self.atq.potencia}\n Presición: {self.atq.precision}'