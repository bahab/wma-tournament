
'''
Created on 23/01/2013

@author: Adam Carter

WMA Tournament tool is focused on being a tool for WMA tournament organisers. 
'''


import webapp2, logging, os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from core_tools import NAV_ITEMS, ROOT_PATH, TEMPLATE_DIR



#Generic handler for front page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        tmpl_vars = {
             'current_tab' : None, 
             'nav_items' : NAV_ITEMS, 
             'main_page' : 'home.html'
        }
        path = os.path.join(os.path.dirname(__file__) + "/HTML", 'index.html')
        self.response.out.write(template.render(path, tmpl_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
