import json

with open('json_module/states.json') as f:
    # 'load' - for objects
    # loads  - for strings
    data = json.load(f)


for state in data['states']:
    del state['area_codes']

with open('json_module/new_states.json', 'w') as f:
    # .dump() converts the data to a json FILE
    json.dump(data, f, indent=4)


