#!/usr/local/bin/python3
"""Searches db for specified detail (ID).
Exercise from headfirst book."""
# their bit of code
import sqlite3

db = sqlite3.connect("surfersDB.sdb")
lookup_id = int(input("Enter the id of the surfer: "))

db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("Select * from surfers")
rows = cursor.fetchall()
for row in rows:
    if row['id'] == lookup_id:
        print("ID:         "+ str(row['id']))
        print("Name:       " + row['name'])
        print('Country:    '+ row['country'])
        print('Average:    '+ str(row['average']))
        print('Board Type: '+ row['board'])
        print('Age:        '+ str(row['age']))
        
    cursor.close()
    
"""
def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    s = {}
    for each_line in surfers_f:
        (s['id'],s['name'],s['country'],s['average'],s['board'],s['age']) = each_line.split(';')
        if id2find == int(s['id']): 
            surfers_f.close()
            return(s)
    surfers_f.close()
    return({})

lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)
if surfer:
    print("ID:        "+ surfer['id'])
    print("Name:     " + surfer['name'])
    print('Country:    '+ surfer['country'])
    print('Average:    '+ surfer['average'])
    print('Board Type: '+ surfer['board'])
    print('Age:        '+ surfer['age'])
"""
