from model import *
from view import *
import ser_json
import ser_pickle
import ser_yaml
import configparser

lastRez = LastResults()
configParser = configparser.ConfigParser()


def backup():
    configParser.read("./config.ini")
    if configParser.getboolean("Backup_Restore", "backup_to_yaml"):
        with open('./yaml.yaml', 'wt') as f:
            ser_yaml.write(lastRez, f)
    if configParser.getboolean("Backup_Restore", "backup_to_json"):
        with open('./json.json', 'wt') as f:
            ser_json.write(lastRez, f)
    if configParser.getboolean("Backup_Restore", "backup_to_pickle"):
        with open('./pickle.pickle', 'wb') as f:
            ser_pickle.write(lastRez, f)


def restore():
    global lastRez
    configParser.read("./config.ini")
    restore_from = configParser.get("Backup_Restore", "restore_from")
    if restore_from == "yaml":
        with open('./yaml.yaml', 'r') as f:
            return ser_yaml.read(f)
    if restore_from == "json":
        with open('./json.json', 'r') as f:
            return ser_json.read(f)
    if restore_from == "pickle":
        with open('./pickle.pickle', 'rb') as f:
            return ser_pickle.read(f)


def count():
    """
    This function calculated your calories
    :return:calories
    """
    global lastRez
    lastRez = restore()
    # system('clear')
    enter_view("weight")
    weight_value = weight(int(input()))
    enter_view("height")
    height_value = height(int(input()))
    enter_view("age")
    age_value = age(int(input()))
    # system('clear')
    view_nWeekTreinings()
    factor = choose_number_of_t(int(input()))
    rz = calculation(weight_value, height_value, age_value, factor)
    lastRez.add_result(rz)
    backup()
    return rz


def menu_listener():
    """
    This function run view functions and print on the screen callories
    :return:
    """
    while True:
        view_menu()
        input_value = int(input())
        if input_value == 1:
            result = count()
            print("Quantity-" + str(result))
            view_1menu()
            input_value = int(input())
            if input_value == 2:
                # system('clear')
                return
        elif input_value == 2:
            # system("clear")
            return
        else:
            print("Choose correct line")
