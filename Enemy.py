from random import randint
import time, os

class Enemy:

    def __init__(self, name, hp, dmg):
        self.name = name
        self.maxHP = hp
        self.hp = self.maxHP
        self.dmg = dmg

        self.knockedOut = False
        self.isBlind = False


    def __str__(self):
        return f'{self.name} has {self.hp}/{self.maxHP} HP and deals {self.dmg} DMG/hit'


    def heal(self):
        if randint(0, 100) > 60:
            val = randint(1, 10)
            if self.hp+val > self.maxHP:
                self.hp = self.maxHP
            else:
                self.hp += val
                
            
    def take_damage(self, amount):
        if self.hp-amount < 0:
            self.hp = 0
        else:
            self.hp -= amount


class Oreos(Enemy):

    def __init__(self):
        super().__init__('Pepto Bismol Oreos', 15, randint(5, 10))
        self.description = 'Oreos will attack you when you least expect it (15 HP, 5-10 DMG)'

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Oreos put toothpaste in your eyes and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class Peptolupa(Enemy):

    def __init__(self):
        super().__init__('Peptolupa', 25, randint(10, 15))
        self.description = 'Peptolupa is a dangerous taco (25 HP, 10-15 DMG)'


    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Peptolupa threw stale tortilla chips and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class Pizza(Enemy):

    def __init__(self):
        super().__init__('Pepto Pizza', 30, randint(15, 20))
        self.description = '8 slices of death (30 HP, 15-20 DMG)'

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Pizza chucked burnt crust at you and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class Van(Enemy):

    def __init__(self):
        super().__init__('Pepto Van', 40, randint(25, 35))
        self.description = 'A van that will run you over in a heartbeat (40 HP, 25-35 DMG)'

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Van ran you over and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class House(Enemy):

    def __init__(self):
        super().__init__('Pepto House', 60, randint(50, 60))
        self.description = 'A house that will eat you when you enter his fight (60 HP, 40-50 DMG)'


    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 95:
            print('The House jumped on you and killed you instantly')
            time.sleep(2)
            os.system('cls')
            player.take_damage(player.maxHP)
        else:
            player.take_damage(self.dmg)
    

class Boss(Enemy):
    
    def __init__(self):
        super().__init__('Pepto BisDog', 150, 25)

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 95:
            print('The King drowned you in Mustard and you died')
            time.sleep(2)
            os.system('cls')
            player.take_damage(player.maxHP)
        else:
            player.take_damage(self.dmg)


        if randint(0, 100) > 97:
            print('The Boss healed to full HP')
            time.sleep(2)
            os.system('cls')
            self.hp = self.maxHP
        