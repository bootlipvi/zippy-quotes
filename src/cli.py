#!/usr/bin/env python3
import argparse
import os
import json
import random
from zippy.quotes import get_random_quote

#def load_quotes(filename="C:\\Users\\fek\\OneDrive\\Documents\\zippy\\zippy-quotes-python\\src\\quotes.json"):
def load_quotes(filename="quotes.json"):    
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

quotes = load_quotes()

def main():
    parser = argparse.ArgumentParser(description='Zippy Quotes CLI')
    #parser.add_argument('-h', '--help', action='help', help='Show help message and exit')
    #parser.add_argument('--all', action='store_true', all='Display all quotes')
    
    args = parser.parse_args()

 #   if args.all:
 #       print('\n'.join(quotes))
 #   else:
    #print(get_random_quote())
    print(random.choice(quotes))

if __name__ == '__main__':
    main()