from task3 import Heros
import datetime

champions = []


def add_hero():
    hero_name = input("Enter Hero name: ")
    hero_vitality = int(input("Enter vitality number between 1 and 10: "))
    hero_armor = int(input("Enter armor number between 1 and 10: "))
    hero_speed = int(input("Enter speed number between 1 and 10: "))
    hero_power = int(input("Enter power number between 1 and 10: "))
    if hero_vitality >= 1 and hero_vitality <= 10 and hero_armor >= 1 and hero_armor <= 10 and hero_speed >= 1 and hero_speed <= 10 and hero_power >= 1 and hero_power <= 10:
        chatachter = Heros(hero_name, hero_vitality, hero_armor, hero_speed, hero_power)
        champions.append(chatachter)
    else:
        print("Please enter numbers between 1 and 10")


# def first_contestant():
#     first_champ = input("enter the name of the first contestant: ")
#     for i in champions:
#         if Heros.get_name(i) == first_champ:
#             first_hero.append(i)
#
#
# def second_contestant():
#     seond_champ = input("enter the name of the second contestant: ")
#     for i in champions:
#         if Heros.get_name(i) == seond_champ and Heros.get_name(i) != first_hero:
#             second_hero.append(i)

def attack_champ():
    first = None
    first_champ = input("enter the name of the first contestant: ")
    for i in champions:
        if Heros.get_name(i) == first_champ:
            first = i
            hero_timer1 = datetime.datetime.now() + datetime.timedelta(0, Heros.get_attack_time(first))
    second = None
    seond_champ = input("enter the name of the second contestant: ")
    for i in champions:
        if Heros.get_name(i) == seond_champ and Heros.get_name(i) != Heros.get_name(first):
            second = i
            hero_timer2 = datetime.datetime.now() + datetime.timedelta(0, Heros.get_attack_time(second))

    while Heros.get_healt(first) > 0 and Heros.get_healt(second) > 0:
        if Heros.get_healt(first) > 0 and hero_timer1 < datetime.datetime.now():
            damage_dealt = Heros.get_damage(first) * (1.0 - Heros.get_damage_reduct(second))
            Heros.set_health(second, damage_dealt)
            hero_timer1 = datetime.datetime.now() + datetime.timedelta(0, Heros.get_attack_time(first))
            print(
                "{0} strikes at {1}, dealing {2} damage {3}".format(Heros.get_name(first),
                                                                    Heros.get_name(second),
                                                                    damage_dealt, Heros.get_healt(second)))
        elif Heros.get_healt(second) > 0 and hero_timer2 < datetime.datetime.now():
            damage_dealt = Heros.get_damage(second) * (1.0 - Heros.get_damage_reduct(first))
            Heros.set_health(first, damage_dealt)
            hero_timer2 = datetime.datetime.now() + datetime.timedelta(0, Heros.get_attack_time(second))
            print(
                "{0} strikes at {1}, dealing {2} damage {3}".format(Heros.get_name(second),
                                                                    Heros.get_name(first),
                                                                    damage_dealt, Heros.get_healt(first)))


def print_champ():
    for i in champions:
        Heros.print_hero(i)


if __name__ == '__main__':
    print("To add Champion write add")
    print("To see all the champions added write list all")
    print("To make them fight write attack")
    command = ""
    while command != "exit":
        command = input("Choose your option: ")
        if command == "add":
            add_hero()
        if command == "list all":
            print_champ()
        if command == "attack":
            attack_champ()
