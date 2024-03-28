import players as py
import pokemons as pk
import time

DELAY = 1.2
CANT_JUGADOR = 1

# --------------------------- FUNCIONES PARA ELECCIÓN DE POKÉMONS ---------------------------

def PC_player():
    player = py.Players()
    for i in range(3):
        player.random_choice()
    player.ver_pokemons(1)
    return player

def Player_Choice():
    global CANT_JUGADOR 
    while True:
        try:
            main_op = int(input(
                f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                f'\033[1mELECCION DEL JUGADOR {CANT_JUGADOR}\033[0m\n'
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
                            f'\033[1m¿Está de acuerdo con su equipo?\n\033[0m'+        
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
                    player = PC_player()
                    ask = int(input(
                        f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'+
                        f'\033[1m¿Está de acuerdo con su equipo?\n\033[0m'+        
                        f'1) Si\n'+
                        f'2) No\n'+
                        f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                    ))
                    if ask == 1:
                        CANT_JUGADOR+=1
                        time.sleep(DELAY)
                        return player 
                    elif ask == 2:
                        pass
                    else: 
                        print("\nERROR: Sea serio pelao'\n")
        except:
            print("\nERROR: Sea serio pelao'\n")

# --------------------------- FUNCIONES PARA LA IMPRESIÓN DE LA BATALLA ---------------------------

def batalla(player_1,player_2,pc=True):
    while True:   
        try:
            if len(player_1.team) > 0 and len(player_2.team) > 0:
                print('\n\033[1mJugador elija un pokemon\033[0m')
                player_1.ver_pokemons()  
                op = int(input(''))-1
                if op >= 0 and player_1.len_team():
                    pokemon_actual = pk.Pokemon(player_1.team[op]())
                    if pc == True:
                        op_2 = player_2.random_pick()
                        pokemon_enemigo = pk.Pokemon(player_2.team[op_2]())
                    else:
                        print('\n\033[1mJugador 2 elija un pokemon\033[0m')
                        player_2.ver_pokemons()
                        op_2 = int(input(''))-1
                    battle = pk.Battle(pokemon_actual,pokemon_enemigo,pc)
                    r,ps_actual = battle.play()
                    if r == 1:
                        player_1.del_team(op)
                        player_2.actualizar_ps(op_2,ps_actual)
                    elif r == 2:
                        player_2.del_team(op_2)
                        player_1.actualizar_ps(op,ps_actual)
                else:
                    print("ERROR: Sea serio pelao'")

            elif len(player_2.team) == 0:
                print('\033[1m¡¡¡GANÓ EL JUGADOR 1!!!\033[0m')
                break
            else:
                print('\033[1m¡¡¡GANÓ EL PC!!!\033[0m')
                break 
        except:
            print("ERROR: Sea serio pelao'")