# INICIE EL PROGRAMA DESDE ESTA PESTAÑA 
# PROGRAMA CREADO POR @KHERAZO18
import prints as pr
# ----------------------------------- INICIO DEL JUEGO -----------------------------------
if __name__ == '__main__':
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    print('\033[1m¡Bienvenido a Pokémon en Terminal!\033[0m')
    print('\033[1mCreated by:\033[0m @KHerazo18')
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    try:
        ask = int(input(
            f'\033[1m¿Como desea jugar?\n\033[0m'+        
            f'1) Vs PC\n'+
            f'2) Vs Jugador\n'+
            f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
            ))
# ----------------------------------- ELECCIÓN DE POKEMONS VS PC -----------------------------------
        if ask == 1:
            player_1 = pr.Player_Choice()
            print('\n\033[1mEQUIPO ENEMIGO\033[0m')
            player_2 = pr.PC_player()

    # ----------------------------------- BATALLA POKEMON ----------------------------------- 
            pr.batalla(player_1,player_2,pc=True)
        
# ----------------------------------- ELECCIÓN DE POKEMONS VS PLAYER -----------------------------------                     
        elif ask == 2:
            player_1 = pr.Player_Choice()
            player_2 = pr.Player_Choice()
    # ----------------------------------- BATALLA POKEMON ----------------------------------- 
            pr.batalla(player_1,player_2,pc=False)
        
    except:
        print("ERROR: Sea serio pelao'")