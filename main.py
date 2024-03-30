# INICIE EL PROGRAMA DESDE ESTA PESTAÑA 
# PROGRAMA CREADO POR @KHERAZO18
#import players as py
import game as gm

# ----------------------------------- INICIO DEL JUEGO -----------------------------------
            
if __name__ == '__main__':
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    print('\033[1m¡Bienvenido a Pokémon en Terminal!\033[0m')
    print('\033[1mCreated by:\033[0m @KHerazo18')
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    ask = gm.valid_ask(
        f'\033[1m¿Como desea jugar?\n\033[0m'+        
        f'1) Vs PC\n'+
        f'2) Vs Jugador\n'+
        f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n',2)
# ----------------------------------- ELECCIÓN DE POKEMONS VS PC -----------------------------------
    if ask == 1:
        player_1 = gm.Player_team_choice().ask()
        player_2 = gm.Random_team_choice().ask()
    # ----------------------------------- BATALLA POKEMON ----------------------------------- 
        game = gm.Game(player_1,player_2,pc=True)
        game.attack_turn()
        
# ----------------------------------- ELECCIÓN DE POKEMONS VS PLAYER -----------------------------------                     
    elif ask == 2:
        player_1 = gm.Player_team_choice().ask()
        player_2 = gm.Player_team_choice().ask()
    # ----------------------------------- BATALLA POKEMON ----------------------------------- 
        game = gm.Game(player_1,player_2,pc=True)
        game.attack_turn()