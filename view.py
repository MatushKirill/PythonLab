from os import system

def view_menu():
    """

    This function that print on the screen start menu
    """
    #system('clear')
    print """1:Run the calculator
2:exit"""

def view_1menu():
    """
    this function print on the screen end menu

    """
    print """1:Repeat?
2:exit"""

def view_nWeekTreinings():
    """
    this function print on hte screen

    """
    #system('clear')
    print """1:Don't train
2:Do fitness 3 times a week
3:Do fitness 5 times a week
4:Do hard train 3 times a week
5:Do fitness every day
6:Do hard trains every day
7:Don't train"""



def enter_view(a=""):
    """

    :param a:
    """
    print "Enter your",a

def incorrect_view(a=""):
    """

    :param a:
    :return:
    """
    print "enter correct",a

