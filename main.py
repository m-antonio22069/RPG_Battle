from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Criando Magia escura
fire = Spell(name='Fire', cost=10, dmg=130, tp='Black')
thunder = Spell(name='Thunder', cost=10, dmg=130, tp='Black')
blizzard = Spell(name='Blizzard', cost=10, dmg=130, tp='Black')
meteor = Spell(name='meteor', cost=20, dmg=200, tp='Black')
quake = Spell(name='quake', cost=14, dmg=140, tp='Black')

# criando magia das luzes
cure = Spell(name='Cure', cost=12, dmg=120, tp='white')
cura = Spell(name='Cura', cost=18, dmg=200, tp='white')

# Criando alguns itens
potion = Item(name='Potion', tp='potion', description='Heals 50 HP', prop=50)
hipotion = Item(name='Hi-Potion', tp='potion', description='Heals 100 HP', prop=100)
superpotion = Item(name='Super Potion', tp='potion', description='Heals 500 HP', prop=500)
elixer = Item(name='Elixer', tp='elixer', description='Fully restores HP/MP of one party member', prop=99999)
hielixer = Item(name='Mega-Elixer', tp='elixer', description="Fully restores HP/MP of one party's HP/MP", prop=99999)

grenade = Item(name='Grenade', tp='attack', description='Deals 500 demage', prop=500)

# Instanciando jogador
player_magic = [fire, thunder, blizzard, meteor, quake, cura, cure]
player_item = [{'item': potion, "quantity": 15},
               {'item': hipotion, "quantity": 5},
               {'item': superpotion, "quantity": 5},
               {'item': elixer, "quantity": 5},
               {'item': hielixer, "quantity": 2},
               {'item': grenade, "quantity": 5}]

player1 = Person(name='Player 1', hp=3260, mp=132, df=300, atk=160, magic=player_magic, item=player_item)
player2 = Person(name='Player 2', hp=4160, mp=188, df=311, atk=240, magic=player_magic, item=player_item)
player3 = Person(name='Player 3', hp=3089, mp=174, df=174, atk=320, magic=player_magic, item=player_item)

# Instanciando inimigo
enemy1 = Person(name='enemy 1', hp=11200, mp=701, df=25, atk=350, magic=[], item=[])
enemy2 = Person(name='enemy 2', hp=18800, mp=120, df=25, atk=560, magic=[], item=[])
enemy3 = Person(name='enemy 3', hp=10200, mp=300, df=25, atk=400, magic=[], item=[])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "Enemy attacks" + bcolors.ENDC)

while running:
    print('===========================================')

    print('\n\n')
    print(bcolors.BOLD + "NAME                    HP                                        MP" + bcolors.ENDC)
    for player in players:
        player.get_status()

    print('\n')

    for enemy in enemies:
        enemy.get_enemy_status()

    for player in players:

        print("\n\n")
        player.get_status()
        print("\n")

        player.choose_action()  # Escolha ação do jogador
        choice = int(input('    Choose action: ')) - 1

        if choice == -1:  # Tratando excessao
            continue

        if choice == 0:  # ação: Ataque

            dmg = player.generateDemage()  # Gerador de danos
            enemy = player.choose_target(enemies)  # escolhendo qual inimigo atacar

            enemies[enemy].take_demage(dmg=dmg)  # Inimigo recebe os dados gerados
            print("You attached", enemies[enemy].name.replace(" ", ""), " for", dmg, "points of demage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " Has died")
                del enemies[enemy]

        elif choice == 1:  # Ação: magica
            player.choose_magic()  # Escolher a magica a ser utilizada
            magic_choice = int(input("    Choose magic:")) - 1

            if magic_choice == -1:  # Tratando excessao
                continue

            spell = player.magic[magic_choice]  # retorna o nome da magia utilizada
            magic_dmg = spell.generate_damage()  # gerador de danos da magica

            current_mp = player.get_mp()  # retorna a quantidade de magic points

            if spell.cost > current_mp:  # Verifica se a quantidade de MP é suficiente
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(cost=spell.cost)  # Reduz o custo de uso da magica

            if spell.tp == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.tp == 'black':

                enemy = player.choose_target(enemies)  # escolhendo qual inimigo atacar

                enemies[enemy].take_demage(dmg=magic_dmg)  # Inimigo recebe os dados gerados

                print(bcolors.OKBLUE + '\n' + spell.name + " deals", str(magic_dmg),
                      "points of demage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " Has died")
                    del enemies[enemy]

        elif choice == 2:  # Escolha o item
            player.choose_item()
            item_choice = int(input("    Choose Item:")) - 1

            if item_choice == -1:  # Tratando excessao
                continue

            item = player.item[item_choice]['item']

            if player.item[item_choice]['quantity'] == 0:  # Verifica a quantidade do item selecionado
                print(bcolors.FAIL + '\n' + 'None left...' + bcolors.ENDC)

            player.item[item_choice]['quantity'] -= 1

            if item.tp == 'potion':
                print(bcolors.OKGREEN + '\n' + item.name + 'heals for ' + item.prop + "HP" + bcolors.ENDC)

            elif item.tp == "elixer":
                if item.name == 'Mega-Elixer':
                    for i in players:
                        i.hp = i.maxHP
                        i.mp = i.maxMP
                else:
                    player.hp = player.maxHP
                    player.mp = player.maxMP

                print(bcolors.OKGREEN + "\n" + item.name + "Fully restored HP/MP" + bcolors.ENDC)

            elif item.tp == 'attack':

                enemy = player.choose_target(enemies)  # escolhendo qual inimigo atacar
                enemies[enemy].take_demage(dmg=item.prop)  # Inimigo recebe os dados gerados

                print(bcolors.FAIL + '\n' + item.name + "deals", str(item.prop),
                      'points of demage to' + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " Has died")
                    del enemies[enemy]

    enemy_choice = 1  # Inimigo so ataca
    target = random.randrange(start=0, stop=3)  # escolhe qual jogador sera atacado
    enemy_dmg = enemies[0].generateDemage()  # gerador de danos do inimigo

    players[target].take_demage(enemy_dmg)  # jogador recebe danos

    # Informações atualizadas
    print("Enemy attached for", enemy_dmg, '\n')
    print('--------------------------------')
    print("Enemy HP:" + bcolors.FAIL + str(enemies[enemy].get_hp()) + "/" + str(enemies[enemy].get_maxHP()) + bcolors.ENDC + '\n')

    # Verifica quem é o ganhador
    defeteaded_enemys = 0
    defeteaded_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeteaded_enemys += 1
    if defeteaded_enemys == 2:
        print(bcolors.OKGREEN + "YOU WIN" + bcolors.ENDC)
        running = False

    for player in players:
        if player.get_hp() == 0:
            defeteaded_players += 1
    if defeteaded_players == 2:
        print(bcolors.FAIL + "Your enemy has defeated you" + bcolors.ENDC)
        running = False
