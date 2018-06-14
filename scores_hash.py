#!/usr/local/bin/python3
"""FInd the high score and return top 3 scores w/names.
This is a first use of reading from a file."""
scores = {}

result_f = open("results.txt")
for each_line in result_f:
    name, score = each_line.split()
    scores[score]= name
result_f.close()
print("The top scores were:")
for each_score in sorted(scores.keys(), reverse=True):
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)

