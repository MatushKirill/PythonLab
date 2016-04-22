import pickle


def write(obj, stream):

        pickle.dump(obj, stream)


def read(stream):
        return pickle.load(stream)
