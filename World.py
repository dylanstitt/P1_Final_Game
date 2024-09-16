from random import *
from Items import *
from Enemy import *
from rand_mess import *
import os, time, art

class World:

    def __init__(self):
        # Map Icons
        self.TRE = '📦'
        self.FIG = '⚔'
        self.CAV = '🪨'
        self.CAS = '🏰'
        self.FOR = '🌲'
        self.PLA = '🧑'

        # Map Creations
        self.display_map = [[self.FOR for i in range(10)] for j in range(10)]
        self.map = [[self.FOR for i in range(10)] for j in range(10)]
        self.backup_map = [[self.FOR for i in range(10)] for j in range(10)]

        fights = [2, 6, 0, 7, 1, 4, 6, 9, 0, 1]

        # BTS Map
        for i in range(len(self.map)):
            self.map[i][fights[i]] = self.FIG
        self.map[9][7] = self.FIG

        self.map[1][1] = self.TRE
        self.map[1][9] = self.TRE
        self.map[2][5] = self.TRE
        self.map[4][4] = self.TRE
        self.map[4][9] = self.TRE
        self.map[5][0] = self.TRE
        self.map[7][4] = self.TRE
        self.map[9][2] = self.TRE
        self.map[9][9] = self.TRE

        self.map[1][3] = self.CAV
        self.map[3][2] = self.CAV
        self.map[4][5] = self.CAV
        self.map[6][2] = self.CAV
        self.map[6][9] = self.CAV
        self.map[9][4] = self.CAV

        self.map[0][9] = self.CAS
        self.map[9][0] = self.PLA
        self.display_map[9][0] = self.PLA

        # Backup Map for Map Icon Replacing
        for i in range(len(self.backup_map)):
            self.backup_map[i][fights[i]] = self.FIG
        self.backup_map[9][7] = self.FIG

        self.backup_map[1][1] = self.TRE
        self.backup_map[1][9] = self.TRE
        self.backup_map[2][5] = self.TRE
        self.backup_map[4][4] = self.TRE
        self.backup_map[4][9] = self.TRE
        self.backup_map[5][0] = self.TRE
        self.backup_map[7][4] = self.TRE
        self.backup_map[9][2] = self.TRE
        self.backup_map[9][9] = self.TRE

        self.backup_map[1][3] = self.CAV
        self.backup_map[3][2] = self.CAV
        self.backup_map[4][5] = self.CAV
        self.backup_map[6][2] = self.CAV
        self.backup_map[6][9] = self.CAV
        self.backup_map[9][4] = self.CAV

        self.backup_map[0][9] = self.CAS


    def __str__(self):
        temp_map = []
        for row in self.display_map:
            temp_map.append(' '.join(row))
        
        return '\n'.join(temp_map)


    def cave(self, player):
        # Prints Cave art, asks if they want to guess or buy out, then does either
        print(art.cave)
        cav_me(randint(1, 3))

        playing = True
        def guess():
            with open('puzzles.txt', 'r') as file:
                content = file.read().split('\n\n\n')
                content = content[randint(0, 5)].split('Ans: ')
                print(content[0])

                guess = input('Enter your answer for the puzzle: ').lower()
                guesses_left = 2

                while guess != content[1].lower() and guesses_left > 0:
                    guesses_left -=1
                    guess = input('Wrong answer, try again: ').lower()

                if guesses_left == 0:
                    player.hp = 0
                    os.system('cls')
                    print(art.game_over)
                    playing = False


        play = input('Would you like to buy (10 coins) your way out or guess (b or g): ').lower()

        while play not in ['b', 'g']:
            play = input('Invalid response. Would you like to buy your way out or guess (b or g): ').lower()

        if play == 'b':
            if len(player.coins) >= 10:
                for i in range(-10, 0):
                    del player.coins[i]
                    os.system('cls')

            else:
                print('Invalid coins')
                time.sleep(2)
                os.system('cls')
                guess()
        
        elif play == 'g' or len(player.coins) < 10:
            guess()
        
        return playing


    def treasure(self, player):
        # Gives random loot w/ a guarunteed Pepto Spray
        print(art.treasure)
        tre_me(randint(1, 3))

        new_items = []

        rand = randint(1, 5)
        for i in range(rand):
            player.coins.append(Coin)

        new_items.append(f'{rand} Coins')

        weapons = [Glock, PeptoBisclub, Dagger, Katana]
        consumables = [PeptoBismol, PeptoBiswangs, PeptoClawmol, MtnBisDew]

        if randint(0, 100) > 65:
            weapon = choice(weapons)()
            player.weapons.append(weapon)
            player.display_weapons.append(str(weapon))

            new_items.append(str(weapon))

        else:
            if randint(0, 100) > 60:
                prev_arm = player.armor
                Armor(player)
                new_items.append(f'{player.armor-prev_arm} Armor')

        consum = choice(consumables)()
        player.pick_up(consum)
        new_items.append(str(consum))

        if randint(0, 100) > 50:
            consum = choice(consumables)()
            player.pick_up(consum)
            new_items.append(str(consum))

        if randint(0, 100) > 55:
            player.pick_up(PeptoSpray())
            new_items.append('Pepto Spray')

        new_items = ', '.join(new_items)
        print(f'\nYou received: \n{new_items}')


    def fight(self, player, boss=None):
        # Selects enemy, player weapon and consumables, then fights with a chance for special attacks
        os.system('cls')
        print(art.fight)
        fig_me(randint(1, 3))

        fighting = True
        curr_weapon = None
        enemy = Boss()

        if boss == None:
            enemy = self.rand_enemy()
        time.sleep(5)
        
        while fighting:
            os.system('cls')
            print(player, end='\n')
            print(enemy, end='\n\n')
            player.inspect()
            
            club_times = 0
            
            for i in player.display_weapons:
              if 'Pepto Bisclub' == i:
                club_times += 1

            if len(player.weapons) == 1 or club_times == len(player.display_weapons):
                curr_weapon = player.weapons[0]
            
            else:
                curr_weapon = input('Enter the weapon you want: ')

                selecting = True
                while selecting:
                    try:
                        curr_weapon = int(curr_weapon)

                        while len(player.weapons) < curr_weapon < 0:
                            curr_weapon = input('That is not a weapon. Enter the consumable you want: ')

                            try:
                                curr_weapon = int(curr_weapon)

                            except:
                                print('That is not an integer')
                                time.sleep(2)
                                os.system('cls')  

                        curr_weapon = player.weapons[curr_weapon-1]
                        selecting = False

                    except:
                        print('That is not an integer')
                        time.sleep(2)
                        os.system('cls')
            
            con = []
            cons = input('\n\nEnter 1 to use a consumable or enter 0 to not: ')
            
            selecting = True
            while selecting:
                try:
                    cons = int(cons)
                    selecting = False

                except:
                    print('That is not an integer')
                    time.sleep(2)
                    os.system('cls')

            if cons == 1:        
                selecting = True
                while selecting:
                    os.system('cls')
                    player.inspect()
                    consum = input('\nEnter the consumable you want to use or enter 0 to stop: ')

                    try:
                        consum = int(consum)

                        while len(player.inv) < consum < 0:
                            consum = input('Enter the consumable you want to use: ')
                            
                            try:
                                consum = int(consum)

                            except:
                                print('That is not an integer or you do not have that consumable in your inventory')
                                time.sleep(2)
                                os.system('cls')
                        
                        if list(player.inv.values())[consum-1] == 0:
                            print('You do not have the consumable in your inventory')
                            time.sleep(2)
                            os.system('cls')
                            continue

                        if consum == 0:
                            selecting = False
                            continue
                        
                        match consum:
                            case 1:
                                con.append(PeptoBismol)
                            case 2:
                                con.append(PeptoBiswangs)
                            case 3:
                                con.append(PeptoClawmol)
                            case 4:
                                con.append(MtnBisDew)
                            case 5:
                                con.append(PeptoSpray)
                        
                        for i in con:
                            if isinstance(i(), Consumable):
                                i().use(player)
                                
                            else:
                                i().use(enemy, player)
                                
                            print(f'\nYou used {i().name}')
                            time.sleep(1.5)
                            os.system('cls')
                            player.inspect()

                    except:
                        print('That is not an integer or you do not have that consumable in your inventory')
                        time.sleep(2)
                        os.system('cls') 

            player.attack(curr_weapon, enemy)

            if enemy.hp == 0:
                os.system('cls')
                if isinstance(enemy, Boss):
                    print('You beat the game!! Congrats on defeating the Pepto BisDog! See you soon...')
                    time.sleep(6)
                    return 'Won Boss'
                
                return self.win(player)

            enemy.attack(player)

            if player.hp == 0:
                os.system('cls')
                return self.loss(enemy)


    def rand_enemy(self):
        # Selects a random enemy for fighting
        rand = randint(0, 100)
        if rand > 95:
            return House()
        
        elif rand > 85:
            return Van()
        
        elif rand > 70:
            if randint(0, 100) > 50:
                return Pizza()
            return Peptolupa()
        
        else:
            return Oreos()
    

    def win(self, player):
        print(art.win)
        print(f'You won! You finished the fight with {player.hp}/{player.maxHP} HP')
        time.sleep(5)
        return 'Won Fight'


    def loss(self, enemy):
        print(art.loss)
        print(f'You lost! The enemy finished the fight with {enemy.hp}/{enemy.maxHP} HP')
        time.sleep(5)
        return 'Lost Fight'
