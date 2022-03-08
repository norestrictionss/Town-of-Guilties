import random
import time


def give_roles(names, roles, all_people):
    taken_names = []

    for x in range(8):
        last_index = len(names) - 1
        chosen_element_index = random.randint(0, last_index)
        while True:
            if names[chosen_element_index] not in taken_names:
                if x <= 2:
                    all_people[x] = [roles[x], names[chosen_element_index]]
                else:
                    all_people[x] = [roles[3], names[chosen_element_index]]
                taken_names.append(names[chosen_element_index])
                break
            else:
                chosen_element_index = random.randint(0, last_index)

    return all_people


def role_finder(my_informations, all_people):
    for x in range(len(all_people)):
        if all_people[x][0] in ["Police", "Mafia", "Serial Killer"]:
            my_informations = all_people[x]
    return my_informations


def role_teller(all_people):
    my_informations = ""
    my_informations = role_finder(my_informations, all_people)

    if my_informations[0] == 'Police':
        print("Your role is Police. You have to find Serial Killer and Mafia before everyone be killed.")
    elif my_informations[0] == 'Mafia':
        print("Your role is Mafia. You have to kill everyone before Sheriff finds you.")

    elif my_informations[0] == 'Serial Killer':
        print("Your role is Serial Killer. You have to kill everyone before Police finds you.")

    return my_informations


def shuffle_all(all_people):
    all_people = sorted(all_people, key=lambda v: random.random())

    for x in range(len(all_people)):
        all_people[x].append(x + 1)
    return all_people


def mafia(take_number, player_numbers, my_informations, validator, all_people):
    while take_number not in player_numbers and my_informations[0] == 'Mafia':

        while validator not in ["Y", "y", "N", "n"]:
            print("Warning. Be careful about being caught by the police.")
            time.sleep(2)
            validator = input("Would you like to choose anyone for being killed?(y/n or Y/N):")
        if validator in ["N", "n"] or validator == "":
            break
        else:
            while take_number not in player_numbers:
                take_number = int(input("Write the player's number:"))
            while take_number == my_informations[2]:
                print("You can't kill yourself. Try again.")
                take_number = int(input("Write the player's number:"))
        if take_number in player_numbers:
            for x in range(len(all_people)):
                if all_people[x][2] == take_number and all_people[x][0] == 'Serial Killer':
                    print("You tried to kill Serial killer but couldn't succeed it. :(")
                    break
                elif all_people[x][2] == take_number:
                    print(all_people[x][1], "was killed. Role of ", all_people[x][1], "was", all_people[x][0])
                    all_people.remove(all_people[x])
                    break

        return take_number


def serial_killer(take_number, player_numbers, my_informations, validator, all_people):
    while take_number not in player_numbers and my_informations[0] == 'Serial Killer':

        while validator not in ["Y", "y", "N", "n"]:
            print("Warning. Be careful about being caught by the police. And also mafia can't kill you.")
            time.sleep(2)
            validator = input("Would you like to choose anyone for being killed?(y/n or Y/N):")
        if validator in ["N", "n"] or validator == "":
            break
        else:
            while take_number not in player_numbers:
                take_number = int(input("Write the player's number:"))

            while take_number == my_informations[2]:
                print("You can't kill yourself. Try again.")
                take_number = int(input("Write the player's number:"))
        if take_number in player_numbers:
            for x in range(len(all_people)):
                if all_people[x][2] == take_number:
                    print(all_people[x][1], " was killed. Role of ", all_people[x][1], "was", all_people[x][0])
                    all_people.remove(all_people[x])
                    break
        return take_number


def police(take_number, player_numbers, my_informations, validator, all_people):
    while take_number not in player_numbers and my_informations[0] == 'Police':

        while validator not in ["Y", "y", "N", "n"]:
            validator = input("Would you like to choose anyone for being killed?(y/n or Y/N):")
        if validator in ["N", "n"] or validator == "":
            break
        else:
            while take_number not in player_numbers:
                take_number = int(input("Write the player's number:"))
            while take_number == my_informations[2]:
                print("You can't kill yourself. Try again.")
                take_number = int(input("Write the player's number:"))
        if take_number in player_numbers:
            for x in range(len(all_people)):
                if all_people[x][2] == take_number:
                    print(all_people[x][1], " was killed. Role of ", all_people[x][1], "was", all_people[x][0])
                    all_people.remove(all_people[x])
                    break
        return take_number


def other_killers_choice(all_people, all_killersv2):
    for x in range(len(all_killersv2)):
        random_victim = random.choice(all_people)

        while random_victim == all_killersv2[x]:
            random_victim = random.choice(all_people)
        choice = ["Nobody", random_victim]
        choice = random.choice(choice)
        if choice == "Nobody":
            pass
        elif all_killersv2[x][0] == "Mafia" and random_victim[0] == "Serial Killer":
            print("Mafia tried to kill Serial Killer but couldn't succeed it. :(")
        else:
            print(random_victim[1], "was killed. Role of ", random_victim[1], "was", random_victim[0])
            all_people.remove(random_victim)


def other_killers_editor(other_killers, my_informations, other_killersv2):
    for x in range(len(other_killers)):
        if other_killers[x] != my_informations and other_killers[x] != []:
            other_killersv2.append(other_killers[x])


def my_informations_writer(my_informations, all_people):
    print("You are player", my_informations[2], ".", len(all_people),
          "person left. You have to specify someone who might be guilty. The specified one will be killed.")


def player_writer(all_people, player_number_string):
    for x in range(len(all_people)):
        print("Player name:", str(all_people[x][1]), " ", player_number_string.rjust(10), str(all_people[x][2]))


def start_game(my_informations, all_people):
    player_number_string = "Player Number:"
    day_counter = 1
    serial_killer_information, mafia_information, police_information = 0, 0, 0
    while True:
        other_killersv2 = []
        print("\n")
        print("Day ", day_counter)

        take_number = ""
        validator = ""
        my_informations_writer(my_informations, all_people)
        player_numbers = [all_people[x][2] for x in range(len(all_people))]
        number_all_people_before = len(all_people)
        player_writer(all_people, player_number_string)

        time.sleep(5)
        if my_informations in all_people:
            take_number = police(take_number, player_numbers, my_informations, validator, all_people) or \
                          mafia(take_number, player_numbers, my_informations, validator, all_people) or \
                          serial_killer(take_number, player_numbers, my_informations, validator, all_people)

        day_counter += 1

        for x in range(len(all_people)):
            if all_people[x][0] == "Police":
                police_information = all_people[x]
            elif all_people[x][0] == "Mafia":
                mafia_information = all_people[x]
            elif all_people[x][0] == "Serial Killer":
                serial_killer_information = all_people[x]
        other_killers = [serial_killer_information, mafia_information, police_information]
        other_killers_editor(other_killers, my_informations, other_killersv2)
        other_killers_choice(all_people, other_killersv2)
        if len(all_people) == number_all_people_before:
            print("Nobody is killed last night.")
        all_roles = [all_people[x][0] for x in range(len(all_people))]
        if "Mafia" not in all_roles and "Serial Killer" not in all_roles:
            print("Innocents won. ^_^ ^_^ ^_^ ^_^ ^_^ ^_^")
            break
        elif "Police" not in all_roles:
            print("Guilties won. :(")
            break


def main():
    print("\n\n\n")
    names = ["Jack", "Jonathan", "Garry", "Sally", "Agnes", "Ursa", "Amy", "Jackie", "Rose", "Arthur", "Frank",
             "Anna", "Charlie", "Jamie", "Nami"]
    roles = ["Police", "Mafia", "Serial Killer", "Innocent"]
    all_people = [0] * 8
    print("Welcome to the Town of Guilties. I hope you can fulfill your necessity of your role.")
    time.sleep(5)
    print("\n")
    all_people = give_roles(names, roles, all_people)
    all_people = shuffle_all(all_people)
    my_informations = role_teller(all_people)
    print("\n")
    start_game(my_informations, all_people)


main()
