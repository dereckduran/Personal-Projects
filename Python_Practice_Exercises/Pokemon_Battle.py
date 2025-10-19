import time
import sys
import random
from IPython.display import clear_output
i j

#pokemon battle game user gets to pick between charizard, blastoise and venusaur
#main function
def main():
    #intro messages
    delay_print("Welcome to the pokemon battle simulator!\n")
    delay_print("This program has Charizard, Blastoise and Venusaur.\nEach player gets to choose one.\n")
    time.sleep(2)#using sleep library to not print out all at once
    clear_output()
    #giving the option for players to write their name
    player1 = Player(input("Player 1, what is your name?\n"))#setting them to the class to use the methods

    player2 = Player(input("Player 2, what is your name?\n"))#setting them to the class to use the methods


    poke_battle = True
    #while game is true
    while poke_battle:

        #defining the pokemon
        pokemon = {} #storing them all in a dictionary to index later
        pokemon['Charizard'] = Pokemon('Charizard', ['Fire','Flying'],#name and typing
                        {'Fire Blast':[110,'Fire','special'],#making moves with info into dictionary to index later
                        'Solar Beam':[140,'Grass','special'],
                        'Brave Bird':[120,'Flying','physical'],
                        'Hyper Beam':[150,'Normal','special']},
                        360, 293 , 348 ,328 ,280 , 295)#stats

        #Blastoise
        pokemon['Blastoise'] = Pokemon('Blastoise',['Water','Water'],#name and typing
                        {'Hydro Pump':[110,'Water','special'],#making moves with info into dictionary to index later
                        'Ice Beam':[90,'Ice','special'],
                        'Dark Pulse':[90,'Dark','special'],
                        'Waterfall':[85,'Water','physical']},
                        362, 291, 295, 280, 328, 339)#stats
        #Blastoise
        #Venusaur
        pokemon['Venusaur'] = Pokemon('Venusaur',['Grass','Poison'],#name and typing
                        {'Leaf Storm':[110,'Grass','special'],#making moves with info into dictionary to index later
                        'Sludge Wave':[90,'Poison','special'],
                        'Petal Dance':[130,'Grass','physical'],
                        'Double Edge':[130,'Normal','physical']},
                        364, 289, 328, 284, 291,328)#stats



        clear_output()
        #Letting players know what is available
        delay_print("Which pokemon will each player choose?\n")
        delay_print("The Fire Breathing Dragon, Charizard!\n")
        delay_print("The Water Cannon Turtle, Blastoise!\n")
        delay_print("The Venomous Plant Dinosaur, Venusaur!\n")

        #storing them inside a variable using a method from the player class
        print(f'{player1.name}')#making sure each player knows its their turn to pick a pokemon
        player1_mon = player1.poke_choice(pokemon)

        print(f'{player2.name}')
        player2_mon = player2.poke_choice(pokemon)#choice method
        clear_output()

        #more intro messages
        print(f'A POKEMON BATTLE HAS STARTED BETWEEN {player1.name} WITH {player1_mon.name} AND {player2.name} WITH {player2_mon.name}!!!\n')
        print('Start!!!\n')
        clear_output()

        #intro messages for each player
        player1.intro(player1_mon)
        time.sleep(1.2)
        clear_output()
        player2.intro(player2_mon)
        time.sleep(1.2)
        clear_output()

        while player1_mon.hp > 0 or player2_mon.hp > 0: #continue playing until one of the pokemons hp falls below 0
            #letting players know how much HP their pokemon have
            delay_print(round((f'{player1_mon.name} currently has {player1_mon.hp} HP.\n')))
            time.sleep(1)
            clear_output()
            delay_print(round((f'{player1_mon.name} currently has {player1_mon.hp} HP.\n')))
            time.sleep(1)
            clear_output()
            #players cho0se attack
            delay_print(f'{player1.name}, please choose a move.\n')

            p1_move = player1.choose_move(pokemon, player1_mon.name)#passing in the correct argument for choosing the object move
            clear_output()

            delay_print(f'{player2.name}, please choose a move.\n')
            p2_move = player2.choose_move(pokemon, player2_mon.name)#passing in the correct argument for choosing the object move
            clear_output()

            #pokemon with higher speed goes first
            if player1_mon.speed > player2_mon.speed:

                #need to make sure both mons attack with an else statement
                damage = damage_calc(pokemon,player1_mon, p1_move ,player2_mon) #passing in correct arguments for the damage calculation
                player2_mon.hp -= damage #reassigning the Hp after damage is dealt
                delay_print(f'{player2_mon.name} has taken {damage} damage!\n') #letting user know how much damage they took
                time.sleep(1)
                if player2_mon.hp < 0: #checking if pokemon fainted after the attack
                    delay_print(f"{player2.name}'s pokemon has fainted! {player1.name} won the pokemon battle!\n")
                    poke_battle = False #pokemon battle has ended
                    break

                damage = damage_calc(pokemon, player2_mon,p2_move,player1_mon)
                player1_mon.hp  -= damage
                delay_print(f'{player1_mon.name} has taken {damage} damage!\n')
                time.sleep(1)
                if player1_mon.hp < 0: #checking if pokemon fainted after the attack
                    delay_print(f"{player1.name}'s pokemon has fainted! {player2.name} won the pokemon battle!\n")
                    poke_battle = False #pokemon battle has ended
                    break


            elif player2_mon.speed > player1_mon.speed:

                #player 2 mon goes first since its faster
                damage = damage_calc(pokemon,player2_mon, p2_move ,player1_mon) #passing in correct arguments for the damage calculation
                player1_mon.hp -=  damage #reassigning the Hp after damage is dealt
                delay_print(f'{player1_mon.name} has taken {damage} damage!\n') #passing in the correct argument for choosing the object move
                time.sleep(1)
                if player1_mon.hp < 0:#checking pokemon hp to verify whether its fainted
                    delay_print(f"{player1.name}'s pokemon has fainted! {player2.name} won the pokemon battle!\n")
                    poke_battle = False #pokemon battle has ended
                    break

                #player 1 mon gets to attack
                damage = damage_calc(pokemon, player1_mon, p1_move ,player2_mon) #passing in correct arguments for the damage calculation
                player2_mon.hp -=  damage #reassigning the Hp after damage is dealt
                delay_print(f'{player2_mon.name} has taken {damage} damage!\n')
                time.sleep(1)
                if player2_mon.hp < 0: #checking if pokemon fainted after the attack
                    delay_print(f"{player2.name}'s pokemon has fainted! {player1.name} won the pokemon battle!\n")
                    poke_battle = False #pokemon battle has ended
                    break
            #turn ends
        delay_print("Thank you for playing!")


#function for delaying the script
def delay_print(s):
    #printing one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#pokemon object class
class Pokemon:
    def __init__(self,name ,typing,moves ,hp, atk,sp_Atk, speed , defense ,sp_Def):#the different attributes each pokemon should have
        self.name = name
        self.typing = typing
        self.moves = moves
        self.hp = hp
        self.atk = atk
        self.sp_Atk = sp_Atk
        self.speed = speed
        self.defense = defense
        self.sp_Def = sp_Def


#function to calculate the damage assuming all pokemon are level 100
def damage_calc(pokemon, player_pokemon, move_choice, foes_pokemon):
    #Variables

    #ATTACKING POKEMON STATS FOR ATTACK
    stab = 1.5 #same type attack bonus
    power = move_choice[0]#move base power
    move_typing = move_choice[1]#indexing the move type
    attack_method = move_choice[2]#indexing the move method
    attack_stat = player_pokemon.atk #attack stat
    special_attack = player_pokemon.sp_Atk #special attack stat
    typing = player_pokemon.typing #pokemon type

    #OPPOSING POKEMOND DEFENSES
    defense = foes_pokemon.defense #defense stat
    special_defense = foes_pokemon.sp_Def#special defense stat
    foes_typing = foes_pokemon.typing

    #trying to define what effectivity is
    version = [['Fire','Flying'],'Water', ['Grass', 'Poison']]
    for i, k in enumerate(version):
        if player_pokemon.typing == k:
            #if same type
            if foes_pokemon.typing == k:
                string_1_attack = "It's not very effective..."
                string_2_attack = "It's not very effective..."

            #if our pokemon has type advantage
            if foes_pokemon.typing == version[(i+2)%3]:
                player_pokemon.atk *= 2
                player_pokemon.defense *= 2
                foes_pokemon.defense /= 2
                foes_pokemon.sp_Def /= 2
                string_1_attack = "It's super effective!"
                string_2_attack = "It's not very effective..."

            #if pokemon has type disadvantage
            if foes_pokemon.typing == version[(i+1)%3]:
                player_pokemon.atk /= 2
                player_pokemon.defense /= 2
                foes_pokemon.defense *= 2
                foes_pokemon.sp_Def *= 2
                string_1_attack = "It's not very effective..."
                string_2_attack = "Its super effective!"

    #calculating for physical moves
    if move_choice[2] == 'physical':
        #stab bonus
        if (move_typing == typing[0]) | (move_typing == typing[1]):
            damage = damage = (102*power*(attack_stat/defense)+2)/50 * stab #* foes_typing
        #no stab
        else:
            damage = (102*power*(attack_stat/defense)+2)/50 #* foes_typing
    #calculating for special moves
    elif move_choice[2] == 'special':
        #stab bonus
        if (move_typing == typing[0]) | (move_typing == typing[1]):
            damage = damage = (102*power*(special_attack/special_defense)+2)/50 * stab
        #define super effective and move base power
        else:
            damage = (102*power*(special_attack/special_defense)+2)/50

    #returning total damage
    return round(damage,2)#returning rounded result


#define Player Class
class Player:
    def __init__(self,name):
        self.name = name

    def poke_choice(self,pokemon):#passing in the pokemon argument to choose
        pokemon_picked = input('Please choose a pokemon: \n').capitalize()#picking mon
        while pokemon_picked not in pokemon.keys():#catching invalid pokemon
            clear_output()
            try:
                clear_output()
                print("That pokemon is not in the game \nPlease try again\n")

                pokemon_picked = input('Please choose a pokemon: ').capitalize()
            except:
                print("That pokemon is not in the game\n")

        pokemon_choice = pokemon[pokemon_picked]#returning the pokemon picked from the the dictionary at player indexed position


        return pokemon_choice#returning the pokemon class at indexed position

    def intro(self,pokemon):#intro
        print(f"Let's give it our best {pokemon.name}!\n")

    #function for choosing a move
    def choose_move(self,pokemon,player_pokemon):
        #storing into a variable
        moves = [move for move in pokemon[player_pokemon].moves.keys()]#using list comp to make the move list
        moves_dict = {1:moves[0], 2:moves[1], 3:moves[2], 4:moves[3]} #making a dictionary to index move position correctly
        print(f'\n\t1.{moves[0]} \t 2.{moves[1]} \n\t3.{moves[2]} \t 4.{moves[3]}')#printing out options for user

        #empty list storing the move choice
        move_choice = []

        #making a while loop to keep asking for correct input
        while True:
            #try/except to catch invalid input
            try:
            #making the input into an integer to index the dictionary
                move_choice = int(input('Select a move(1-4):\n' ))
                while move_choice not in moves_dict: #if the choice is not in the dictionary
                    clear_output()
                    try:#another try/except to catch numbers out of range
                        print(f'{pokemon[player_pokemon].name} only has 4 moves!!')
                        move_choice = int(input('Select a move(1-4):\n' ))
                    except:
                        print(f'{pokemon[player_pokemon].name} only has 4 moves!!')
                        continue
            #checking for invalid input
            except:#catching letters
                print(f'\t Whoops no letters! \n\tNumbers from 1 to 4 please!')
                continue

            else:#succesfully storing the value and printing out which move mon will use
                move_choice = moves_dict[move_choice]
                #clear_output()
                print(f'{pokemon[player_pokemon].name} will use {move_choice}.')
                time.sleep(2)
                break

        #returning selected move with its list of attributes
        return pokemon[player_pokemon].moves[move_choice] #using the list index from the dictionary that the player decided

#runnning the script
if __name__ == "__main__":
    main()
