'''
Created on 23/01/2013

@author: bahab
'''
import os


# Global path variables
ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(ROOT_PATH, 'HTML', 'index.html')


# Global Navigation
NAV_ITEMS = [
    {'name' : 'News', 'address' : '/'},
    {'name' : 'Profiles', 'address' : 'profiles.html'},
    {'name' : 'Clubs', 'address' : 'groups.html'},
    {'name' : 'Events', 'address' : 'events.html'},
    {'name' : 'Signup', 'address' : 'sign-up.html'}
]