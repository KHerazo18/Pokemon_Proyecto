# Info sacada de https://www.pokexperto.net/index2.php
import attacks as at
import random
import time

delay = 1.5

class stats:
    def __init__(self):
        self.nombre = ''
        self.ps = 0
        self.ataque = 0
        self.atEspecial = 0
        self.velocidad = 0
        self.defensa = 0
        self.defEspecial = 0 
        self.listAtaques = []    

class Pokemon:
    def __init__(self, pj:stats):
        super().__init__()
        self.pj = pj

    def __str__(self):
        return f'\033[1m{self.pj.nombre}\033[0m\n❤️  PS: {self.pj.ps} - 🎿  Velocidad: {self.pj.velocidad} \n🗡️  Ataque: {self.pj.ataque} - 🌟  Ataque Especial: {self.pj.atEspecial}\n🛡️  Defensa: {self.pj.defensa} - ☔  Defensa Especial {self.pj.defEspecial}\n🌀 Habilidades: {[x.nombre for x in self.pj.listAtaques]}'

    def ver_ps(self):
        return self.pj.ps
    
    def ver_nombre(self):
        return self.pj.nombre
    
    def ver_vel(self):
        return self.pj.velocidad

    def new_ps(self,new_ps):
        self.pj.ps = new_ps

    def ver_habilidades(self):
        print(f' 🌌 \033[1mHABILIDADES\033[0m 🌌')
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        for i,x in enumerate(self.pj.listAtaques):
            print(f' {i+1}){at.Attacks(x)}')
            print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    
    def atacar(self,pj_2,atq):
        pk_01, pk_02 = self.pj, pj_2.pj
        habilidad = at.Attacks(pk_01.listAtaques[atq]).atq

        if habilidad.precision >= random.randint(0,100):
            if habilidad.tipo == 'Físico':
                damage = round(((2 * pk_01.ataque / pk_02.defensa) * habilidad.potencia) / 50 + 2)
                pk_02.ps -= damage
                return damage
            else:
                damage = round(((2 * pk_01.atEspecial / pk_02.defEspecial) * habilidad.potencia) / 50 + 2)
                pk_02.ps -= damage
                return damage
        else:
            return 0

class Battle(Pokemon):
    def __init__(self, pj: stats, pj_2:stats, pc:bool):
        super().__init__(pj)
        self.pj = pj
        self.pj_2 = pj_2
        self.pc = pc
    
    def status(self):
        print('\n ✨ \033[1mESTADO\033[0m ✨ ')
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        print(f' \033[1m {self.pj.ver_nombre()}\033[0m\n  ❤️  PS: {self.pj.ver_ps()}')
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        print(f'  \033[1m{self.pj_2.ver_nombre()}\033[0m\n  ❤️  PS: {self.pj_2.ver_ps()}')
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n')

    def play(self):
        def turno_pj(pk_01:Pokemon, pk_02:Pokemon):
            if pk_01.ver_ps() > 0 and pk_02.ver_ps() > 0:
                print(f' ⚔️  \033[1m¡Ataca {pk_01.ver_nombre()}!\033[0m⚔️\n')
                time.sleep(delay)
                pk_01.ver_habilidades()
                op = int(input(f'\033[1m¡Elije una habilidad!\033[0m\n'))-1 
                if op >= 0 and op < 4:
                    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
                    print(f' \033[1m{at.Attacks(pk_01.pj.listAtaques[op]).atq.nombre}\033[0m ha realizado \033[1m{pk_01.atacar(pk_02,op)}\033[0m de daño!')
                    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n')
                    time.sleep(delay)
                    self.status()
                    time.sleep(delay)
                else:
                    print("ERROR: Sea serio pelao'")
            else:
                pass

        def turno_pc(pk_01:Pokemon, pk_02:Pokemon):
            if pk_01.ver_ps() > 0 and pk_02.ver_ps() > 0:
                print(f' ⚔️  \033[1m¡Ataca {pk_01.ver_nombre()}!\033[0m⚔️\n')
                time.sleep(delay)
                op = random.randint(0,3) 
                print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
                print(f' \033[1m{at.Attacks(pk_01.pj.listAtaques[op]).atq.nombre}\033[0m ha realizado \033[1m{pk_01.atacar(pk_02,op)}\033[0m de daño!')
                print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n')
                time.sleep(delay)
                self.status()
                time.sleep(delay)
            else:
                pass
        pk_01 = self.pj
        pk_02 = self.pj_2

        self.status()
        while pk_01.ver_ps() > 0 and pk_02.ver_ps() > 0:
            if self.pc == True:
                if pk_01.ver_vel() >= pk_02.ver_vel():
                    turno_pj(pk_01,pk_02)
                    turno_pc(pk_02,pk_01)
                else:
                    turno_pc(pk_02,pk_01)
                    turno_pj(pk_01,pk_02)
            else:
                if pk_01.ver_vel() >= pk_02.ver_vel():
                    turno_pj(pk_01,pk_02)
                    turno_pj(pk_02,pk_01)
                else:
                    turno_pj(pk_02,pk_01)
                    turno_pj(pk_01,pk_02)
        if pk_01.ver_ps() <= 0:
            return 1,pk_02.ver_ps()
        else:
            return 2,pk_01.ver_ps()

class Pikachu(stats):
    def __init__(self):
        self.nombre = 'Pikachu'
        self.ps = 35
        self.ataque = 55
        self.defensa = 40
        self.velocidad = 90
        self.atEspecial = 50       
        self.defEspecial = 50 
        self.listAtaques = [at.Impactrueno,at.Rayo,at.Ataque_Rapido,at.Placaje]

class Caterpie(stats):
    def __init__(self):
        self.nombre = 'Caterpie'
        self.ps = 45
        self.ataque = 30
        self.defensa = 35
        self.velocidad = 45
        self.atEspecial = 20       
        self.defEspecial = 20 
        self.listAtaques = [at.Placaje,at.Tacleada,at.Supersonico,at.Drenadoras]  
 
class Pidgeotto(stats):
    def __init__(self):
        self.nombre = 'Pidgeotto'
        self.ps = 40
        self.ataque = 45
        self.defensa = 40
        self.velocidad = 56
        self.atEspecial = 35       
        self.defEspecial = 35 
        self.listAtaques = [at.Picotazo,at.Remolino,at.Tornado,at.Ataque_Rapido]      
    
class Bulbasaur(stats):
    def __init__(self):
        self.nombre = 'Bulbasaur'
        self.ps = 45
        self.ataque = 49
        self.defensa = 49
        self.velocidad = 45
        self.atEspecial = 65       
        self.defEspecial = 65 
        self.listAtaques = [at.Latigo_Cepa,at.Drenadoras,at.Placaje,at.Somnifero]  

class Charmander(stats):
    def __init__(self):
        self.nombre = 'Charmander'
        self.ps = 39
        self.ataque = 52
        self.defensa = 43
        self.velocidad = 65
        self.atEspecial = 60       
        self.defEspecial = 50 
        self.listAtaques = [at.Lanzallamas,at.Grunido,at.Aranazo,at.Ascuas] 

class Squirtle(stats):
    def __init__(self):
        self.nombre = 'Squirtle'
        self.ps = 44
        self.ataque = 48
        self.defensa = 65
        self.velocidad = 43
        self.atEspecial = 50       
        self.defEspecial = 64 
        self.listAtaques = [at.Pistola_Agua,at.Burbuja,at.Ataque_Rapido,at.Placaje]      

class Krabby(stats):
    def __init__(self):
        self.nombre = 'Krabby'
        self.ps = 30
        self.ataque = 105
        self.defensa = 90
        self.velocidad = 50
        self.atEspecial = 25       
        self.defEspecial = 25 
        self.listAtaques = [at.Burbuja,at.Rayo_Burbuja,at.Placaje,at.Tajo_Cruzado]        

class Raticate(stats):
    def __init__(self):
        self.nombre = 'Raticate'
        self.ps = 30
        self.ataque = 56
        self.defensa = 35
        self.velocidad = 72
        self.atEspecial = 25       
        self.defEspecial = 35 
        self.listAtaques = [at.Hipercolmillo,at.Ataque_Rapido,at.Placaje,at.Golpe_Cabeza]        

class Muk(stats):
    def __init__(self):
        self.nombre = 'Muk'
        self.ps = 80
        self.ataque = 80
        self.defensa = 50
        self.velocidad = 25
        self.atEspecial = 40       
        self.defEspecial = 50 
        self.listAtaques = [at.Lodo,at.Bomba_Lodo,at.Ataque_Acido,at.Infortunio]       

class Kingler(stats):
    def __init__(self):
        self.nombre = 'Kingler'
        self.ps = 30
        self.ataque = 105
        self.defensa = 90
        self.velocidad = 50
        self.atEspecial = 25       
        self.defEspecial = 25
        self.listAtaques = [at.Hidropulso,at.Rayo_Burbuja,at.Rayo,at.Placaje]      