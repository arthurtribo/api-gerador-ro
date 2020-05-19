#!/usr/bin/python
# -*- coding: utf-8 -*-


import csv

def get_database():
  db = dict()

  with open('janeiro.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    in_memory_entries = list(reader)
    print(len(in_memory_entries))
    db["janeiro"] = in_memory_entries[1:]

  with open('fevereiro.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    in_memory_entries = list(reader)
    print(len(in_memory_entries))
    db["fevereiro"] = in_memory_entries[1:]

  with open('marco.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    in_memory_entries = list(reader)
    print(len(in_memory_entries))
    db["marco"] = in_memory_entries[1:]

  # with open('abril.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["abril"] = in_memory_entries[1:]

  # with open('maio.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["maio"] = in_memory_entries[1:]

  # with open('junho.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["junho"] = in_memory_entries[1:]

  # with open('julho.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["julho"] = in_memory_entries[1:]

  # with open('agosto.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["agosto"] = in_memory_entries[1:]

  # with open('setembro.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["setembro"] = in_memory_entries[1:]

  # with open('outubro.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["outubro"] = in_memory_entries[1:]

  # with open('novembro.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["novembro"] = in_memory_entries[1:]

  # with open('dezembro.csv') as csv_file:
  #   reader = csv.DictReader(csv_file, delimiter=';')
  #   in_memory_entries = list(reader)
  #   print(len(in_memory_entries))
  #   db["dezembro"] = in_memory_entries[1:]

  return db

#import csv

#with open('janeiro.csv', mode='r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print(f'Column names are {"; ".join(row)}')
#            line_count += 1
#        print('row["Data"]},{row["Nivel"]},{row["Tipo"]},{row["Conta"]},{row["Reduzido"]},{row["Descrição]},{row["Anterio"]},{row["Débitos"]},{row["Créditos"]},{row["Movimento"]},{row["Saldo Atual"]}')
#        line_count += 1
#    print(f'Processed {line_count} lines.')

