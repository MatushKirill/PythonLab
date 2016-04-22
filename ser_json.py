import json

import model


class LastResultsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, model.LastResults):
            return {"lastResult":obj.lastResult}
        return json.JSONEncoder.default(self, obj)


def write(obj, f):
        json.dump(obj, f, cls=LastResultsEncoder)


def read(f):
        res = json.load(f)
        return model.LastResults(res["lastResult"])
