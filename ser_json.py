import json

import model


class LastResultsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, model.LastResults):
            return {"lastResult":obj.lastResult}
        return json.JSONEncoder.default(self, obj)


def write(obj, filename='./json.json'):
    with open(filename, 'wt') as f:
        json.dump(obj, f, cls=LastResultsEncoder)


def read(filename='./json.json'):
    with open(filename, 'r') as f:
        res = json.load(f)
        return model.LastResults(res["lastResult"])
