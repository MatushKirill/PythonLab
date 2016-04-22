import pickle


def write(obj, filename='./pickle.pickle'):
    with open(filename, 'wt') as f:
        pickle.dump(obj, f)


def read(filename='./pickle.pickle'):
    with open(filename, 'r') as f:
        return pickle.load(f)
