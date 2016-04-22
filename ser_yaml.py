import yaml


def write(obj, f):
    yaml.dump(obj, f)


def read(f):
    return yaml.load(f)
