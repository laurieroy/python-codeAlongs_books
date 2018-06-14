#!/usr/local/bin/python3
"""Get price of beans, if less than a certain amount, buy. Price quote on a delay."""
import urllib.request, time
# import sys, tweepy

def set_password():
    password="C8H10n402"

set_password()

def send_to_twitter(msg): # note this code is slightly differnt in book. followup if care
    password_manager = urllib.request.HTTPpasswordMgr()
    password_manager.add_password("Twitter API", "http://twitter.com/statuses", "starbuzzceo", password)
    CONSUMER_KEY = '...'
    CONSUMER_SECRET = '...'
    ACCESS_KEY = '...'
    ACCESS_SECRET ='...'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)
    

def get_price():
    """Func to get price from website."""    
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

price_now = input("Do you want to see the price now (Y/N)?")
if price_now == 'Y':
    send_to_twitter(get_price())
    print('The price now is', price) # warm fuzzy for me
elif price_now == 'N':
    price = 99.99
    while price > 4.74:
        time.sleep(900)
        price = get_price()
    send_to_twitter('Buy!')
else:
    print("\nYour choices are 'Y' for 'YES', or 'N' for 'NO'. ")

    
            
           
      
