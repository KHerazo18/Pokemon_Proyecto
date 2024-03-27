import pokemons as pk
from random import randrange

class Players:
    def __init__(self):
        self.pokemons = [pk.Pikachu,pk.Caterpie,pk.Pidgeotto,pk.Bulbasaur,pk.Charmander,pk.Squirtle,pk.Krabby,pk.Raticate,pk.Muk,pk.Kingler]
        self.team = []

    def ver_lst_pokemons(self):
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        for i,x in enumerate(self.pokemons):
            print(f'{i+1}) {pk.Pokemon(x()).ver_nombre()}')
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    def ver_pokemons(self,num=0):
        print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        for i,x in enumerate(self.team):
            if num == 0:
                print(f'{i+1}) {pk.Pokemon(x()).ver_nombre()}')
            else:
                print(f'{i+1}) {pk.Pokemon(x())}')
            print(f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

    def actualizar_ps(self,pos,ps):
        self.team[pos].ps = ps

    def len_team(self):
        return len(self.team)

    def del_lst(self,pos):
        del self.pokemons[pos]

    def del_team(self,pos):
        del self.team[pos]

    def choice(self,pos):
        x = pos
        while True:
            try:
                self.team.append(self.pokemons[x])
                self.del_lst(x)
                break
            except:
                x = input('Ingrese un número de pokemon válido\n')

    def random_choice(self):        
        self.choice(randrange(0,len(self.pokemons)))
    
    def random_pick(self):
        return randrange(0,len(self.team))