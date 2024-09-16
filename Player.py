from Items import *
from random import randint
from art import castle
import os, time

class Player:

    def __init__(self, name):
        self.name = name
        self.attDmg = 0
        self.armor = 0
        self.maxArmor = 50
        self.maxHP = 100
        self.hp = self.maxHP

        self.weapons = [PeptoBisclub()]
        self.display_weapons = [str(PeptoBisclub())]
        self.coins = [Coin for i in range(5)]
        self.inv = {}

        starting = [PeptoBismol(), PeptoBiswangs(), PeptoClawmol(), MtnBisDew(), PeptoSpray()]
        for item in starting:
            self.pick_up(item)

        print(self.inv)

        self.isDrunk = False
        self.paralyzedTurns = 0
        self.attBuffTurns = 0

    
    def __str__(self):
        return f'You have {self.hp}/{self.maxHP} HP w/ {self.armor} Armor'
    

    def heal(self, amount):
        if self.hp+amount > self.maxHP:
            self.hp = self.maxHP
        else:
            self.hp += amount


    def take_damage(self, amount):
        if self.armor-amount < 0:
            amount -= self.armor
            self.armor = 0

            if self.hp-amount < 0:
                self.hp = 0
            else:
                self.hp -= amount

        else:
            self.armor -= amount


    def attack(self, weapon, enemy):
        if isinstance(weapon, PeptoBisclub):
            weapon.special(enemy)
        
        elif isinstance(weapon, Katana) or isinstance(weapon, Dagger):
            weapon.special()

        if self.paralyzedTurns > 0:
            self.paralyzedTurns -= 1
            print('You are paralayed')
            time.sleep(3)
            return

        if self.isDrunk:
            self.isDrunk = False
            if randint(0, 100) <= 65:
                print('You missed the target')
                time.sleep(3)
                return

        if self.attBuffTurns > 0:
            self.attBuffTurns -= 1
            print(f'You did {self.attDmg}x damage')
            enemy.take_damage(weapon.dmg*self.attDmg)
            time.sleep(2)

        else:
            enemy.take_damage(weapon.dmg)
            
        if self.attBuffTurns == 0:
            self.attDmg = 0

        if isinstance(weapon, Glock):
            del self.weapons[self.weapons.index(weapon)]
            del self.display_weapons[self.display_weapons.index(str(weapon))]

        weapon.dmg = weapon.og_dmg


    def pick_up(self, item):
        if isinstance(item, Weapon):
            self.weapons.append(item)
            self.display_weapons.append(str(item))

        else:
            if type(item) not in self.inv:
                self.inv[type(item)] = [item]

            else:
                self.inv[type(item)].append(item)

    
    def inspect(self):
        inv = []
        c = 1
        for i in self.inv:
            if i != 'Weapons' and i != 'Coins' and len(self.inv[i]) > 0:
                inv.append(f'{c}) {len(self.inv[i])} {self.inv[i][0].name} ({self.inv[i][0].description})')
            c += 1
        print('\n'.join(inv))
        print()
            
        weapons = []
        c = 1
        for i in self.weapons:
            if f'{c}) {str(i)} ({i.description})' not in weapons:
                weapons.append(f'{c}) {str(i)} ({i.description})')
                c += 1

        print('\n'.join(weapons))
        print(f'\n{len(self.coins)} Coins')


    def move(self, world):
        print(world)
        dirr = input('Enter the direction you want to travel or inspect the inventory (N, S, E, W, I): ').lower()

        while dirr not in ['n', 's', 'e', 'w', 'i']:
            print('Invalid Direction')
            time.sleep(2)
            os.system('cls')
            print(world)
            dirr = input('Enter the direction you want to travel or inspect the inventory (N, S, E, W, I): ').lower()

        if dirr == 'i':
            os.system('cls')
            self.inspect()
            input('\nPress ENTER when you\'re ready to continue')
            
        else:
            old_icon = None
            prev_pos = None
            match dirr:
                case 'n': 
                    for i in range(len(world.map)):
                        if world.PLA in world.map[i]:
                            prev_pos = [i, world.map[i].index(world.PLA)]
                            
                            try:
                                if prev_pos[0]-1 != -1:
                                    old_icon = world.map[prev_pos[0]-1][prev_pos[1]]
                                    world.map[prev_pos[0]-1][prev_pos[1]] = world.PLA
                                    world.display_map[prev_pos[0]-1][prev_pos[1]] = world.PLA

                                else:
                                    raise IndexError

                            except:
                                print('That is out of bounds')
                                time.sleep(2)
                                os.system('cls')

                                self.move(world)
                
                case 's': 
                    for i in range(len(world.map)):
                        if world.PLA in world.map[i]:
                            prev_pos = [i, world.map[i].index(world.PLA)]

                            try:
                                if prev_pos[0]+1 != 10:
                                    old_icon = world.map[prev_pos[0]+1][prev_pos[1]]
                                    world.map[prev_pos[0]+1][prev_pos[1]] = world.PLA
                                    world.display_map[prev_pos[0]+1][prev_pos[1]] = world.PLA
                                    break

                                else:
                                    raise IndexError
                            
                            except:
                                print('That is out of bounds')
                                time.sleep(2)
                                os.system('cls')

                                self.move(world)
                
                case 'e': 
                    for i in range(len(world.map)):
                        if world.PLA in world.map[i]:
                            prev_pos = [i, world.map[i].index(world.PLA)]
                            
                            try:
                                if prev_pos[1]+1 != 10:
                                    old_icon = world.map[prev_pos[0]][prev_pos[1]+1]
                                    world.map[prev_pos[0]][prev_pos[1]+1] = world.PLA
                                    world.display_map[prev_pos[0]][prev_pos[1]+1] = world.PLA

                                else:
                                    raise IndexError

                            except:
                                print('That is out of bounds')
                                time.sleep(2)
                                os.system('cls')

                                self.move(world)
                
                case 'w': 
                    for i in range(len(world.map)):
                        if world.PLA in world.map[i]:
                            prev_pos = [i, world.map[i].index(world.PLA)]
                            
                            try:
                                if prev_pos[1]-1 != -1:
                                    old_icon = world.map[prev_pos[0]][prev_pos[1]-1]
                                    world.map[prev_pos[0]][prev_pos[1]-1] = world.PLA
                                    world.display_map[prev_pos[0]][prev_pos[1]-1] = world.PLA

                                else:
                                    raise IndexError

                            except:
                                print('That is out of bounds')
                                time.sleep(2)
                                os.system('cls')

                                self.move(world)

            world.map[prev_pos[0]][prev_pos[1]] = world.backup_map[prev_pos[0]][prev_pos[1]]
            world.display_map[prev_pos[0]][prev_pos[1]] = world.FOR

            if old_icon == world.FIG or old_icon == world.CAS:
                if old_icon == world.CAS:
                    print(castle)
                    time.sleep(2)
                    os.system('cls')

                    return world.fight(self, 'Boss')
                return world.fight(self)

            elif old_icon == world.CAV:
                return world.cave(self)

            elif old_icon == world.TRE:
                os.system('cls')
                world.treasure(self)

                input('\n\nPress ENTER when your ready to continue')

        return True
