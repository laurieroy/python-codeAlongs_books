#!/usr/local/bin/python3
"""Searches db for specified detail (ID).
Exercise from headfirst book."""
# their bit of code as they wrote in book.
import sqlite3

def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")
   

    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("Select * from surfers")
    rows = cursor.fetchall()
    cursor.close()
    for row in rows:
        s={}
        if row['id'] == id2find:
            s['id']         = str(row['id'])
            s['name']       = row['name']
            s['country']    = row['country']
            s['average']    = str(row['average'])
            s['board']      = row['board']
            s['age']        = str(row['age'])
            
            
            return(s)
        
    return({})

lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)

if len(surfer) > 0:
    print("ID:         "+ surfer['id'])
    print("Name:       " + surfer['name'])
    print('Country:    '+ surfer['country'])
    print('Average:    '+ surfer['average'])
    print('Board Type: '+ surfer['board'])
    print('Age:        '+ surfer['age'])
    
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
