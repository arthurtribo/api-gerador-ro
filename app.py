#!/usr/bin/pythons
# -*- coding: utf-8 -*-


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dictionary.py
 
from flask import Flask, jsonify
from flask_cors import CORS
from dictionary import get_database
from apps.apis import bp

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.register_blueprint(bp)

print (app.url_map)
app.url_map.strict_slashes = False

if(__name__ == '__main__'):
    app.run('localhost', 5000, True)

# import csv

# with open('janeiro.csv') as csv_file:
#   reader = csv.DictReader(csv_file, delimiter=';')
#   in_memory_entries = list(reader)
#   print(len(in_memory_entries))
#   print(in_memory_entries[0])
#   print(in_memory_entries[1])

# with open('fevereiro.csv') as csv_file:
#   reader = csv.DictReader(csv_file, delimiter=';')
#   in_memory_entries = list(reader)
#   print(len(in_memory_entries))
#   print(in_memory_entries[0])
#   print(in_memory_entries[1])