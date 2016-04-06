
"""


>>> from model import *

>>> from control import *

>>> from view import *

>>> view_menu()
1:Run the calculator
2:exit

>>> view_1menu()
1:Repeat?
2:exit

>>> view_nWeekTreinings()
1:Don't train
2:Do fitness 3 times a week
3:Do fitness 5 times a week
4:Do hard train 3 times a week
5:Do fitness every day
6:Do hard trains every day
7:Don't train

>>> enter_view("weight")
Enter your weight

>>> incorrect_view("height")
enter correct height

>>> calculation(97,182,20,chooseNumberOfT(4))
2862

>>> weight(input())
97

>>> height(input())
182

>>> age(input())
20

>>> chooseNumberOfT(1)
1.2

>>> chooseNumberOfT(6)
1.725

>>> chooseNumberOfT(5)
1.6375

>>> chooseNumberOfT(4)
1.55

>>> chooseNumberOfT(3)
1.4625

>>> count()
Enter your weight
Enter your height
Enter your age
1:Don't train
2:Do fitness 3 times a week
3:Do fitness 5 times a week
4:Do hard train 3 times a week
5:Do fitness every day
6:Do hard trains every day
7:Don't train
2862

>>> menu_listener()
1:Run the calculator
2:exit
Enter your weight
Enter your height
Enter your age
1:Don't train
2:Do fitness 3 times a week
3:Do fitness 5 times a week
4:Do hard train 3 times a week
5:Do fitness every day
6:Do hard trains every day
7:Don't train
Quantity- 2862
1:Repeat?
2:exit
1:Run the calculator
2:exit


"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
