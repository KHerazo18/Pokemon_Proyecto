# INICIE EL PROGRAMA DESDE ESTA PESTAÑA 
# PROGRAMA CREADO POR @KHERAZO18

import players as py
import pokemons as pk
import time

delay = 1.2

# --------------------------- FUNCIONES PARA ELECCIÓN DE POKÉMONS ---------------------------

def Player_Choice(x):
    while True:
        try:
            main_op = int(input(
                f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                f'\033[1mELECCION DEL JUGADOR {x}\033[0m\n'
                f'1) Elegir Pokemons Manualmente\n'+
                f'2) Elegir Pokemons Aleatoriamente\n'+
                f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
            ))
            if main_op == 1:
                while True:
                    try:
                        player = py.Players()
                        for i in range(3):
                            player.ver_lst_pokemons()
                            pokemon_op = int(input(f'\033[1mSelecciona un pokemon: \n\033[0m'))-1
                            player.choice(pokemon_op)
                        player.ver_pokemons(1)
                        ask = int(input(
                            f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                            f'\033[1m¿Está deacuerdo con su equipo?\n\033[0m'+        
                            f'1) Si\n'+
                            f'2) No\n'+
                            f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                        ))
                        if ask == 1:
                            return player 
                        elif ask == 2:
                            pass
                    except: 
                        print("\nERROR: Sea serio pelao'\n")
                        
            elif main_op == 2:
                while True:
                    player = py.Players()
                    for i in range(3):
                        player.random_choice()
                    player.ver_pokemons(1)
                    ask = int(input(
                        f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                        f'\033[1m¿Está deacuerdo con su equipo?\n\033[0m'+        
                        f'1) Si\n'+
                        f'2) No\n'+
                        f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                    ))
                    if ask == 1:
                        return player 
                    elif ask == 2:
                        pass
                    else: 
                        print("\nERROR: Sea serio pelao'\n")
        except:
            print("\nERROR: Sea serio pelao'\n")

def PC_player():
    player = py.Players()
    for i in range(3):
        player.random_choice()
    player.ver_pokemons(1)
    return player

# ----------------------------------- INICIO DEL JUEGO -----------------------------------

if __name__ == '__main__':
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    print('\033[1m¡Bienvenido a Pokémon en Terminal!\033[0m')
    print('\033[1mCreated by:\033[0m @KHerazo18')
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')


    while True:
        try:
            ask = int(input(
                f'\033[1m¿Como desea jugar?\n\033[0m'+        
                f'1) Vs PC\n'+
                f'2) Vs Jugador\n'+
                f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                ))
            
    # ----------------------------------- ELECCIÓN DE POKEMONS VS PC -----------------------------------
            
            if ask == 1:
                player_1 = Player_Choice(1)
                time.sleep(delay)
                print('\nEQUIPO ENEMIGO')
                player_2 = PC_player()
                time.sleep(delay)
        # ----------------------------------- BATALLA POKEMON -----------------------------------            
        
                while True:    
                    print('\n\033[1mJugador elija un pokemon\033[0m')
                    player_1.ver_pokemons()
                    try:  
                        op = int(input(''))-1
                        if op >= 0 and player_1.len_team():
                            pokemon_actual = pk.Pokemon(player_1.team[op]())
                            op_pc = player_2.random_pick()
                            pokemon_enemigo = pk.Pokemon(player_2.team[op_pc]())
                            battle = pk.Battle(pokemon_actual,pokemon_enemigo,True)
                            r,ps_actual = battle.play()
                            if len(player_1.team) > 0 or len(player_2.team) > 0:
                                if r == 1:
                                    player_1.del_team(op)
                                    player_2.actualizar_ps(op_pc,ps_actual)
                                elif r == 2:
                                    player_2.del_team(op_pc)
                                    player_1.actualizar_ps(op,ps_actual)

                            elif len(player_2.team) == 0:
                                print('\033[1m¡¡¡GANÓ EL JUGADOR 1!!!\033[0m')
                                quit()
                            else:
                                print('\033[1m¡¡¡GANÓ EL PC!!!\033[0m')
                                quit()
                        else:
                            print("ERROR: Sea serio pelao'")
                    except:
                        print("ERROR: Sea serio pelao'")

    # ----------------------------------- ELECCIÓN DE POKEMONS VS PLAYER -----------------------------------                     
            
            elif ask == 2:
                player_1 = Player_Choice(1)
                time.sleep(delay)
                player_2 = Player_Choice(2)

        # ----------------------------------- BATALLA POKEMON -----------------------------------
                while True:    
                        print('\n\033[1mJugador 1 elija un pokemon\033[0m')
                        player_1.ver_pokemons()
                        try:  
                            op = int(input(''))-1
                            if op >= 0 and player_1.len_team():
                                pokemon_actual = pk.Pokemon(player_1.team[op]())
                                print('\n\033[1mJugador 2 elija un pokemon\033[0m')
                                player_2.ver_pokemons()
                                op_2 = int(input(''))-1
                                if op_2 >= 0 and player_2.len_team():
                                    pokemon_enemigo = pk.Pokemon(player_2.team[op_2]())
                                    battle = pk.Battle(pokemon_actual,pokemon_enemigo,False)
                                    r,ps_actual = battle.play()
                                    if len(player_1.team) > 0 or len(player_2.team) > 0:
                                        if r == 1:
                                            player_1.del_team(op)
                                            player_2.actualizar_ps(op_2,ps_actual)
                                        elif r == 2:
                                            player_2.del_team(op_2)
                                            player_1.actualizar_ps(op,ps_actual)

                                    elif len(player_2.team) == 0:
                                        print('\033[1m¡¡¡GANÓ EL JUGADOR 1!!!\033[0m')
                                        quit()
                                    else:
                                        print('\033[1m¡¡¡GANÓ EL JUGADOR 2!!!\033[0m')
                                        quit()
                                else:
                                    print("ERROR: Sea serio pelao'")
                        except:
                            print("ERROR: Sea serio pelao'")
        except:
            print("ERROR: Sea serio pelao'")