import json

# https://docs.python.org/3/library/json.html#encoders-and-decoders

mys = '''
{
"states": [
    {
      "name": "Alabama",
      "abbreviation": "AL"
    },
    {
      "name": "Alaska",
      "abbreviation": "AK"
    }
  ]
}
'''

data = json.loads(mys)  # loads as a dict from a STRING
print(type(data))  # json object = dict
print(type(data['states']))  # json array = list

for state in data['states']:
    print(state)  # also a dict

# remove ta key-value pair
for state in data['states']:
    del state['abbreviation']

# sort_keys - sorts the keys in the dictionary
# .dumps() - converts the data to a json STRING
new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
