import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Classe pessoa
class Person:
    """
    hp = hit points
    mp = magic points
    atk = attack
    df = defense
    magic = magic
    """

    # Contrutor
    def __init__(self, name, hp, mp, atk, df, magic, item):
        self.name = name
        self.maxHP = hp
        self.hp = hp
        self.maxMP = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.item = item
        self.actions = ['Attack', 'Magic', 'Item']

    def generateDemage(self):
        return random.randrange(start=self.atkl, stop=self.atkh)

    def take_demage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxHP:
            self.hp = self.maxHP

    def get_hp(self):
        return self.hp

    def get_maxHP(self):
        return self.maxHP

    def get_mp(self):
        return self.mp

    def get_maxMP(self):
        return self.maxMP

    def choose_action(self):
        i = 1
        print('\n' + "   " + bcolors.BOLD + self.name + bcolors.ENDC)
        print('\n' + bcolors.OKBLUE + bcolors.BOLD + "   ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print('\n' + bcolors.OKBLUE + bcolors.BOLD + "   MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ':', spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print('\n' + bcolors.OKGREEN + bcolors.BOLD + "   ITEM:" + bcolors.ENDC)
        for item in self.item:
            print("        " + str(i) + ':', item['item'].name, ":", item['item'].description,
                  " (x" + str(item['quantity']) + ')')
            i += 1

    def choose_target(self, enemies):
        i = 0
        print('\n' + bcolors.BOLD + bcolors.FAIL + "    TARGET" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_HP() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target")) - 1
        return choice

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_enemy_status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHP) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + '/' + str(self.maxHP)
        current_hp = ""

        if len(hp_string) < 11:
            decresead = 11 - len(hp_string)

            while decresead > 0:
                current_hp += " "
                decresead -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print(
            bcolors.FAIL + "                             __________________________________________________" + bcolors.ENDC)
        print(bcolors.BOLD + self.name + "         " + current_hp + bcolors.FAIL + " |" + hp_bar + "|" + bcolors.ENDC)

    def get_status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHP) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxMP) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += ""

        hp_string = str(self.hp) + '/' + str(self.maxHP)
        current_hp = ""

        if len(hp_string) < 9:
            decresead = 9 - len(hp_string)

            while decresead > 0:
                current_hp += " "
                decresead -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + '/' + str(self.maxMP)
        current_mp = ""

        if len(mp_string) < 7:
            decresead = 7 - len(mp_string)

            while decresead > 0:
                current_mp += " "
                decresead -= 1
            current_mp += hp_string
        else:
            current_mp = mp_string

        print(
            bcolors.OKGREEN + "                            _________________________" + bcolors.ENDC + bcolors.OKBLUE + "                   __________" + bcolors.ENDC)
        print(
            bcolors.BOLD + self.name + "         " + current_hp + bcolors.OKGREEN + " |" + hp_bar + "|" + bcolors.ENDC + bcolors.BOLD + bcolors.ENDC + "         " + bcolors.BOLD + current_mp + bcolors.OKBLUE + " |" + mp_bar + "|" + bcolors.ENDC)
