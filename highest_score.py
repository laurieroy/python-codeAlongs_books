#!/usr/local/bin/python3
"""FInd the high score and return top 3 scors w/names.
This is a first use of reading from a file."""
scores = {}

result_f = open("results.txt")
for each_line in result_f:
    name, score = each_line.split()
    score[score]= name
result_f.close()
for each_score in scores.keys():
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)
"""
print('The top scores were: ')
print(scores[0])
print(scores[1])
print(scores[2])"""
