from os import system
from model import *
from view import *



def count():
    """
    This function calculated your callories
    :return:callories
    """
    #system('clear')
    enter_view("weight")
    Weight=weight(input())
    enter_view("height")
    Height=height(input())
    enter_view("age")
    Age=age(input())
    #system('clear')
    view_nWeekTreinings()
    Factor=chooseNumberOfT(input())
    rz=calculation(Weight,Height,Age,Factor)
    return rz
def menu_listener():
    """
    This function run view functions and print on the screen callories
    :return:
    """
    last=0
    while(True):
        view_menu()
        Input=input()
        if Input==1:
            rezult=count()
            print "Quantity-",rezult
            view_1menu()
            Input=input()
            if Input==2:
                #system('clear')
                return
        elif Input==2:
            #system("clear")
            return
        else:print "Choose correct line"

