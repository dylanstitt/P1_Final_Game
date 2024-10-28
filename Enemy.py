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


class Spider(Enemy):

    def __init__(self):
        super().__init__('Spider', 15, randint(5, 10))
        self.description = 'Spider will attack you when you least expect it (15 HP, 5-10 DMG)'

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Spider put webs in your face and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class Scorpion(Enemy):

    def __init__(self):
        super().__init__('Scorpion', 25, randint(10, 15))
        self.description = 'Scorpion is a dangerous animal (25 HP, 10-15 DMG)'


    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Scorpion threw its stinger at you and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class Beast(Enemy):

    def __init__(self):
        super().__init__('The Beast', 30, randint(15, 20))
        self.description = '8 arms of death (30 HP, 15-20 DMG)'

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Beast chucked one of its arms at you and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class Hoard(Enemy):

    def __init__(self):
        super().__init__('The Hoard', 40, randint(25, 35))
        self.description = 'A hoard of the undead that will run you over in a heartbeat (40 HP, 25-35 DMG)'

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 60:
            print('The Hoard ran you over and did 1.5x damage')
            time.sleep(2)
            os.system('cls')
            player.take_damage(self.dmg*1.5)
        else:
            player.take_damage(self.dmg)


class Dragon(Enemy):

    def __init__(self):
        super().__init__('Dragon', 60, randint(50, 60))
        self.description = 'A dragon that will eat you when you enter his fight (60 HP, 40-50 DMG)'


    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 95:
            print('The Dragon jumped on you and killed you instantly')
            time.sleep(2)
            os.system('cls')
            player.take_damage(player.maxHP)
        else:
            player.take_damage(self.dmg)
    

class Boss(Enemy):
    
    def __init__(self):
        super().__init__('King', 150, 25)

    
    def attack(self, player):
        if self.knockedOut:
            self.knockedOut = False
            return
        
        if randint(0, 100) > 95:
            print('The King drowned you in tar and you died')
            time.sleep(2)
            os.system('cls')
            player.take_damage(player.maxHP)
        else:
            player.take_damage(self.dmg)


        if randint(0, 100) > 97:
            print('The King healed to full HP')
            time.sleep(2)
            os.system('cls')
            self.hp = self.maxHP
        