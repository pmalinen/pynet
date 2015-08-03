#!/usr/bin/env python

import yaml
import json

from pprint import pprint

yaml_file = 'my_file.yml'
json_file = 'my_file.json'

with open(yaml_file) as f:
    yaml_list = yaml.load(f)

with open(json_file) as f:
    json_list = json.load(f)

pprint(yaml_list)
pprint(json_list)
