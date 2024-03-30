from abc import ABC, abstractmethod
import random
import time
import attacks as at
import pokemons as pk

# LISTA DE POKEMONS

Pikachu     = pk.Pikachu().create()
Caterpie    = pk.Caterpie().create()
Pidgeotto   = pk.Pidgeotto().create()
Bulbasaur   = pk.Bulbasaur().create()
Charmander  = pk.Charmander().create()
Squirtle    = pk.Squirtle().create()
Krabby      = pk.Krabby().create()
Raticate    = pk.Raticate().create()
Muk         = pk.Muk().create()
Kingler     = pk.Kingler().create()

# CONSTANTES

POKEMONS = [Pikachu,Caterpie,Pidgeotto,Bulbasaur,Charmander,Squirtle,Krabby,Raticate,Muk,Kingler]
CANT_JUGADORES = 1
DELAY = 1.2

# ------------------------ PLANTILLA PARA TIPOS DE ATAQUE ------------------------

class Attack_model(ABC):
    @abstractmethod
    def __init__(self,ability:at.Ability_Blueprint,attacker:pk.Pokemon_Blueprint,receiver:pk.Pokemon_Blueprint):
        self.ability = ability
        self.attacker = attacker
        self.receiver = receiver

    @abstractmethod
    def attack(self):
        pass 

class Magic_attack(Attack_model):
    def __init__(self,ability:at.Ability_Blueprint,attacker:pk.Pokemon_Blueprint,receiver:pk.Pokemon_Blueprint):
        self.ability = ability
        self.attacker = attacker 
        self.receiver = receiver

    def attack(self):
        if self.ability.precision >= random.randint(0,100):
            return round(((2 * self.attacker.atEspecial / self.receiver.defEspecial) * self.ability.power) / 50 + 2)
        else:
            return 0

class Physical_attack(Attack_model):
    def __init__(self,ability:at.Ability_Blueprint,attacker:pk.Pokemon_Blueprint,receiver:pk.Pokemon_Blueprint):
        self.ability = ability
        self.attacker = attacker 
        self.receiver = receiver

    def attack(self):
        if self.ability.precision >= random.randint(0,100):
            return round(((2 * self.attacker.attack / self.receiver.defense) * self.ability.power) / 50 + 2)
        else:
            return 0
        
# ------------------------ CLASE JUGADOR ------------------------

class Player:
    def __init__(self,*team:pk.Pokemon_Blueprint):
        self.team = [i for i in team]

    def show_team(self):
        print('\n🌌 \033[1mTEAM\033[0m 🌌')
        for pokemons in self.team:
            print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
            print(pokemons)
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    def abilities(self,n_pokemon:int):
        return [abilities for abilities in self.team[n_pokemon].abilities]
    
    def team_len(self):
        return len(self.team)

# ------------------------ PLANTILLA PARA PREGUNTAS ------------------------

def valid_ask(text:str,max:int,min:int=0,type=int):
    while True:    
        try:
            ask = type(input(text))
            if ask >= 0 and ask <= max:
                return ask
        except:
            print("\nERROR: Sea serio pelao'\n")

class Ask_model(ABC):
    @abstractmethod
    def ask(self:Player):
        pass

class Random_team_choice(Ask_model):
    def ask(self) -> Player:
        global POKEMONS
        pk_lst = POKEMONS.copy()
        random_pokemon_lst = []
        for i in range(3):
            r = random.randrange(len(pk_lst))
            random_pokemon_lst.append(pk_lst[r])
            del pk_lst[r]

        return Player(random_pokemon_lst[0],random_pokemon_lst[1],random_pokemon_lst[2])

class Random_pokemon_choice(Ask_model):
    def ask(self,py:Player) -> int:
        return random.randrange(len(py.team))
    
class Random_ability_choice(Ask_model):
    def ask(self):
        r = random.randrange(4)
        return r 

class Player_team_choice(Ask_model):
    def ask(self) -> Player:
        global POKEMONS
        pk_lst = POKEMONS.copy()
        global CANT_JUGADORES
        while True:
            op_1 = valid_ask(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                            f'\033[1mELECCION DEL JUGADOR {CANT_JUGADORES}\033[0m\n'
                            f'1) Elegir Pokemons Manualmente\n'+
                            f'2) Elegir Pokemons Aleatoriamente\n'+
                            f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n',2)
            CANT_JUGADORES+=1
            if op_1 == 1:
                pokemon_lst = []
                for i in range(3):
                    for x,pokemon in enumerate(pk_lst):
                        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
                        print(f'{x+1}) \033[1m{pokemon.name}\033[0m')
                    print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n')
                    r = valid_ask(f'\033[1mSelecciona un pokemon: \n\033[0m',len(pk_lst))-1
                    pokemon_lst.append(pk_lst[r])
                    del pk_lst[r]
                team = Player(pokemon_lst[0],pokemon_lst[1],pokemon_lst[2])
                team.show_team()
                ask = valid_ask(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                                f'\033[1m¿Está de acuerdo con su equipo?\n\033[0m'+        
                                f'1) Si\n'+
                                f'2) No\n'+
                                f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n',2)
                if ask == 1:
                    return team
                else:
                    pass
            if op_1 == 2:
                team = Random_team_choice().ask()
                team.show_team()   
                ask = valid_ask(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                                f'\033[1m¿Está de acuerdo con su equipo?\n\033[0m'+        
                                f'1) Si\n'+
                                f'2) No\n'+
                                f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n',2) 
                if ask == 1:
                    return team
                else:
                    pass              

class Player_pokemon_choice(Ask_model):
    def ask(self,py:Player) -> int:
        print(f'\n👹 \033[1mPOKEMONS\033[0m 👹')
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        for x,i in enumerate(py.team):
            print(f'{x+1}) \033[1m{i.name}\033[0m')
            print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        ask = valid_ask(f'\n\033[1m¡Elija un pokemon!: \033[1m\n',py.team_len())-1             
        return ask

class Player_ability_choice(Ask_model):
    def ask(self,py:pk.Pokemon_Blueprint) -> int:
        print('\n🔥 \033[1mHABILIDADES\033[0m 🔥')
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        for i in range(4):
            print(f'{i+1}) \033[1m{py.abilities[i].name}\033[0m\nTipo: {py.abilities[i].type}\nPoder: {py.abilities[i].power}\nPrecisión: {py.abilities[i].precision}')
            print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        ask = valid_ask(f'\n\033[1m¡Elija una habilidad!: \033[1m\n',4)-1             
        return ask

# ------------------------ CLASE GAME ------------------------

class Game:
    def __init__(self,Player_01:Player,Player_02:Player,pc:bool):
        self.Player_01 = Player_01
        self.Player_02 = Player_02
        self.pc = pc

    def show_status(self,pokemon_attacker:pk.Pokemon_Blueprint,pokemon_receiver:pk.Pokemon_Blueprint):
        print('\n ✨ \033[1mESTADO\033[0m ✨ ')
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        pokemon_attacker.status()
        print(f'➖➖➖➖➖➖➖ VS ➖➖➖➖➖➖➖➖')
        pokemon_receiver.status()
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    def show_damage(self,pokemon_attacker:pk.Pokemon_Blueprint,n_ability:int,damage:int):
        ability = pokemon_attacker.abilities[n_ability]
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        print(f'💥 \033[1m{ability.name}\033[0m ha hecho \033[1m{damage}\033[0m de daño!💥')
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    def show_who_attacks(self,pokemon_attacker:pk.Pokemon_Blueprint):
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        print(f'⚡ \033[1m{pokemon_attacker.name}\033[0m Ataca!⚡')
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    def calc_damage(self,pokemon_attacker:pk.Pokemon_Blueprint,pokemon_receiver:pk.Pokemon_Blueprint,n_ability:int):
        ability = pokemon_attacker.abilities[n_ability]
        if ability.type == 'Magic':
            return Magic_attack(ability,pokemon_attacker,pokemon_receiver).attack()
        else:
            return Physical_attack(ability,pokemon_attacker,pokemon_receiver).attack()
            
    def attack_turn(self):
        # PREGUNTA POR POKEMON HASTA QUE NO HAYA EN EL EQUIPO
        while self.Player_01.team_len() > 0 and self.Player_02.team_len():
            print('\n\033[1mJUGADOR 1 ELIJE POKÉMON\033[0m')
            n_pokemon_py1 = Player_pokemon_choice().ask(self.Player_01)
            time.sleep(DELAY)
            if self.pc == True:
                n_pokemon_py2 = Random_pokemon_choice().ask(self.Player_02)
            else:
                print('\n\033[1mJUGADOR 2 ELIJE POKÉMON\033[0m')
                n_pokemon_py2 = Player_pokemon_choice().ask(self.Player_02)
                time.sleep(DELAY)
                                                            
            pokemonpy1 = self.Player_01.team[n_pokemon_py1]
            pokemonpy2 = self.Player_02.team[n_pokemon_py2]
            self.show_status(pokemonpy1,pokemonpy2)

            # PREGUNTA HABILIDADES DE CIERTO POKEMON ELEGIDO, HASTA QUE ESTE NO TENGA PS
            while pokemonpy1.ps > 0 and pokemonpy2.ps > 0:
                if pokemonpy1.velocity >= pokemonpy2.velocity:
                    # TURNO JUGADOR 1
                    self.show_who_attacks(pokemonpy1)
                    time.sleep(DELAY)
                    n_ability = Player_ability_choice().ask(pokemonpy1) 
                    damage = self.calc_damage(pokemonpy1,pokemonpy2,n_ability)
                    self.Player_02.team[n_pokemon_py2].ps -= damage
                    self.show_damage(pokemonpy1,n_ability,damage)
                    time.sleep(DELAY)
                    self.show_status(pokemonpy1,pokemonpy2)
                    time.sleep(DELAY)

                    # TURNO JUGADOR 2
                    if pokemonpy1.ps > 0 and pokemonpy2.ps > 0:
                        if self.pc == True:
                            print('\n\033[1mTURNO DE LA MÁQUINA\033[0m')
                            self.show_who_attacks(pokemonpy2)
                            time.sleep(DELAY)
                            n_ability_2 = Random_ability_choice().ask()
                        else:
                            self.show_who_attacks(pokemonpy2)
                            time.sleep(DELAY)
                            n_ability_2 = Player_ability_choice().ask(pokemonpy2)
                        
                        damage = self.calc_damage(pokemonpy2,pokemonpy1,n_ability_2)
                        self.Player_01.team[n_pokemon_py1].ps -= damage
                        self.show_damage(pokemonpy2,n_ability_2,damage)
                        time.sleep(DELAY)
                        self.show_status(pokemonpy1,pokemonpy2)
                        time.sleep(DELAY)
                    else:
                        break
                else:
                    # TURNO JUGADOR 2
                    if self.pc == True:
                        print('\n\033[1mTURNO DE LA MÁQUINA\033[0m')
                        self.show_who_attacks(pokemonpy2)
                        time.sleep(DELAY)
                        n_ability_2 = Random_ability_choice().ask()
                    else:
                        self.show_who_attacks(pokemonpy2)
                        time.sleep(DELAY)
                        n_ability_2 = Player_ability_choice().ask(pokemonpy2)

                    damage = self.calc_damage(pokemonpy2,pokemonpy1,n_ability_2)
                    self.Player_01.team[n_pokemon_py1].ps -= damage
                    self.show_damage(pokemonpy2,n_ability_2,damage)
                    time.sleep(DELAY)
                    self.show_status(pokemonpy1,pokemonpy2)
                    time.sleep(DELAY)

                    # TURNO JUGADOR 1
                    if pokemonpy1.ps > 0 and pokemonpy2.ps > 0:
                        self.show_who_attacks(pokemonpy1)
                        time.sleep(DELAY)
                        n_ability = Player_ability_choice().ask(pokemonpy1) 

                        damage = self.calc_damage(pokemonpy1,pokemonpy2,n_ability)
                        self.Player_02.team[n_pokemon_py2].ps -= damage
                        self.show_damage(pokemonpy1,n_ability,damage)
                        time.sleep(DELAY)
                        self.show_status(pokemonpy1,pokemonpy2)
                        time.sleep(DELAY)
                    else:
                        break

            if pokemonpy2.ps <= 0:
                del self.Player_02.team[n_pokemon_py2]
                print(f'\033[1m{pokemonpy1.name} Ganó el combate!!\033[1m')
            else:
                del self.Player_01.team[n_pokemon_py1]
                print(f'\033[1m{pokemonpy2.name} Ganó el combate!!\033[1m')

        if self.Player_01.team_len() <= 0:
                print(f'👑 \033[1m¡¡¡EL JUGADOR 2 GANÓ!!!\033[1m👑')
        else:
            print(f'👑 \033[1m¡¡¡EL JUGADOR 1 GANÓ!!!\033[1m👑')