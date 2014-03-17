import json
from copy import deepcopy

def load_and_split(path, name_prefix, name_property):
    """
    Extract all feature objects from a geojson object at path.
    """
    fh = open(path)
    obj = json.loads(fh.read())
    fh.close()
    for i in obj['features']:
        name = '%s_%s.geojson' % (name_prefix, i['properties'][name_property])
        print 'Starting %s' % name
        newobj = deepcopy(obj)
        newobj['features'] = [deepcopy(i)]
        fh = open(name, 'w')
        fh.write(json.dumps(newobj))
        fh.close()

if __name__ == '__main__':
    state_reps = 'state_reps_09.geojson'
    load_and_split(state_reps, 'state_rep', 'SLDLST')
