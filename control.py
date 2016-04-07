from os import system
from model import *
from view import *
import ser_json
import ser_pickle
import ser_yaml
import ConfigParser

lastRez = LastResults()
configParser = ConfigParser.ConfigParser()


def backup():
    configParser.read("./config.ini")
    if configParser.getboolean("Backup_Restore", "backup_to_yaml"):
        ser_yaml.write(lastRez)
    if configParser.getboolean("Backup_Restore", "backup_to_json"):
        ser_json.write(lastRez, )
    if configParser.getboolean("Backup_Restore", "backup_to_pickle"):
        ser_pickle.write(lastRez)


def restore():
    global lastRez
    configParser.read("./config.ini")
    restore_from = configParser.get("Backup_Restore", "restore_from")
    if restore_from == "yaml":
        lastRez = ser_yaml.read()
    if restore_from == "json":
        lastRez = ser_json.read()
    if restore_from == "pickle":
        lastRez = ser_pickle.read()


def count():
    """
    This function calculated your calories
    :return:calories
    """
    # lastRez=restore()
    # system('clear')
    enter_view("weight")
    weight_value = weight(input())
    enter_view("height")
    height_value = height(input())
    enter_view("age")
    age_value = age(input())
    # system('clear')
    view_n_week_trainings()
    factor = choose_number_of_t(input())
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
        input_value = input()
        if input_value == 1:
            result = count()
            print "Quantity-", result
            view_1menu()
            input_value = input()
            if input_value == 2:
                # system('clear')
                return
        elif input_value == 2:
            # system("clear")
            return
        else:
            print "Choose correct line"
