#!/usr/local/bin/python3
"""Format outputfor POS staton.
Exercise from headfirst book."""

def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%07d%16s%16s\n" % (price * 100, credit_card, description))
    file.close()


    
     
