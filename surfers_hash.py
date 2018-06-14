#!/usr/local/bin/python3
"""Searches file for specified detail (ID).
Exercise from headfirst book."""
""" my original pseudo:
surfers = {}
import data
result_f = open (...)
for line in result_f:
    (surfers['ID'],surfers['Name'],surfers['Country'],surfers['Average'],surfers['Board Type'],surfers['Age']) = line.split(';')
    
result_f(close)
print("ID:        "+ surfers['ID'})
print("Name:     " + surfers['Name'])
print('Country:    '+surfers['Country'])
print('Average:    '+surfers['Average'])
print('Board Type: '+surfers['Board Type'])
print('Age:        '+surfers['Age'])
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

