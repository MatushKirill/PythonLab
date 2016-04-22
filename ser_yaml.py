import yaml


def write(obj, filename='./yaml.yaml'):
    with open(filename, 'wt') as f:
        yaml.dump(obj, f)


def read(filename='./yaml.yaml'):
    with open(filename, 'r') as f:
        return yaml.load(f)
