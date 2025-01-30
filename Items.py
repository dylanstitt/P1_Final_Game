from random import randint
import time

class Treasure:
    
    def __init__(self, name):
        self.name = name
    

    def __str__(self):
        return self.name
    

class PoisonSpray(Treasure):

    def __init__(self):
        super().__init__('Poison Spray')
        self.description = 'Blind your enemies for one turn where they can\'t hit you'
    
    
    def remove(self, item, player):
        if len(player.inv[type(item)])-1 == 0:
            del player.inv[type(item)]

        else:
           del player.inv[type(item)][-1]
    
    
    def use(self, enemy, player):
        enemy.knockedOut = True
        self.remove(PoisonSpray(), player)


class Coin(Treasure):

    def __init__(self):
        super().__init__('Gold Coins')
        self.description = 'These can be used to possibly bribe an enemy or to buy your way out of a cave'


class Armor(Treasure):

    def __init__(self, player):
        super().__init__('Armor')
        self.description = 'Acts like extra health to the player, but will not be restored/fixed when you eat/drink a consumable'
        value = randint(5, 15)

        if player.armor+value > player.maxArmor:
            player.armor = player.maxArmor

        else:
            player.armor += value


class Consumable:
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


    def __str__(self):
        return self.name
    

    def remove(self, item, player):
        player.inv[type(item)].pop()
    

class SuperApple(Consumable):

    def __init__(self):
        super().__init__('Super Apple', 20)
        self.description = 'Restores 20 HP and gives you a 10% damage buff for 3 turns (Does not stack with Wings)'

    
    def use(self, player):
        player.attDmg = 1.10
        player.attBuffTurns = 3
        self.remove(SuperApple(), player)

    
class Pills(Consumable):

    def __init__(self):
        super().__init__('Pills', 30)
        self.description = 'Restores 30 HP and doubles your Attack Damage for 1 turn (Does not stack w/ Super Apple)'
    

    def use(self, player):
        player.attDmg = 2
        player.attBuffTurns = 1
        self.remove(Pills(), player)


class StrangeWater(Consumable):

    def __init__(self):
        super().__init__('Strange Water', 15)
        self.description = 'Restores 15 HP and gives you a chance to miss an attack'
    

    def use(self, player):
        player.isDrunk = True
        self.remove(StrangeWater(), player)


class HealingPotion(Consumable):

    def __init__(self):
        super().__init__('HealingPotion', 50)
        self.description = 'Restores 50 HP and you are paralyzed for 2 turns'
    

    def use(self, player):
        player.paralyzedTurns = 2
        self.remove(HealingPotion(), player)


class Weapon:
    
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg
        self.og_dmg = self.dmg

    
    def __str__(self):
        return self.name
    

class Katana(Weapon):

    def __init__(self):
        super().__init__('Katana', 15)
        self.description = 'A long sword that deals 15 damage to all enemies'


    def special(self):
        if randint(0, 100) >= 70:
            self.dmg *= 2


class Dagger(Weapon):

    def __init__(self):
        super().__init__('Dagger', 10)
        self.description = 'A small knife that deals 10 damage that has a chance for a deep cut (1.5x damage)'

    
    def special(self):
        if randint(0, 100) >= 60:
            self.dmg *= 1.5


class Club(Weapon):

    def __init__(self):
        super().__init__('Club', 5)
        self.description = 'Your starting weapon that deals 5 damage and has a chance to knock the enemy out for 1 turn'

    
    def special(self, enemy):
        if randint(0, 100) >= 70:
            print('You knocked the enemy out!')
            time.sleep(3)
            enemy.knockedOut = True


class Glock(Weapon):

    def __init__(self):
        super().__init__('Glock', 1000)
        self.description = 'A very powerful weapon that one shots every enemy other than The King (1 use)'
