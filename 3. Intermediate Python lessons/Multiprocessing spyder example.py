# -*- coding: utf-8 -*-
"""
Source:https://www.youtube.com/watch?v=
N0ph2a6Vd7M&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=12&ab_channel=sentdex
"""
from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://', starting, '.com'])
    return url

def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link