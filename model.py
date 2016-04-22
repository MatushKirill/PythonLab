class LastResults:
    def __init__(self, res=[]):
        self.lastResult = res

    def add_result(self, rez):
        self.lastResult.append(rez)

    def print_last_res(self):
        print (self.lastResult)


def weight(input_weight):
    """
    This function check rightness of weight that you write
    :param input_weight:weight that you write
    :return:weight
    """
    while True:
        if input_weight > 160 or input_weight <= 0:
            input_weight = input()
        else:
            return input_weight


def height(input_height):
    """
    This function check rightness of height that you write
    :param input_height:height that you write
    :return:height
    """
    while True:
        if input_height > 250 or input_height <= 0:
            input_height = input()
        else:
            return input_height


def age(input_age):
    """
    This function check rightness of age that you write
    :param input_age:age that you write
    :return:age
    """
    while True:
        if input_age > 110 or input_age <= 0:
            input_age = input()

        else:
            return input_age


def choose_number_of_t(number):
    """
    In this function you choose how often you do physical exercises
    :param number:Number of your week train
    :return:factor that depends on your week trains
    """
    if number == 1:
        factor = 1.2
    elif number == 2:
        factor = 1.375
    elif number == 3:
        factor = 1.4625
    elif number == 4:
        factor = 1.550
    elif number == 5:
        factor = 1.6375
    elif number == 6:
        factor = 1.725
    elif number == 7:
        factor = 1

    return factor


def calculation(weight_in, height_in, age_in, factor):
    """

    :param weight_in:your weight
    :param height_in:your height
    :param age_in:your age
    :param factor:factor that depends on your week trains
    :return:calories that your must get every day
    """
    calories = int((10 * weight_in + 6.25 * height_in - 5 * age_in - 161) * factor)
    return calories
