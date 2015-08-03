#!/usr/bin/env python


import yaml
import json

yaml_file = 'my_file.yml'
json_file = 'my_file.json'


my_dict = {
    'hostname': 'myhost',
    'ip': '10.10.10.1',
    }

my_list = [
    'Testing',
    1234,
    my_dict,
    ]

print my_dict
print my_list

print yaml.dump(my_list, default_flow_style=False)

with open(yaml_file, "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open(json_file, "w") as f:
    json.dump(my_list, f)
