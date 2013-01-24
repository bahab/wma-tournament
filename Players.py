'''
Created on 24/01/2013

@author: Adam Carter
'''
import webapp2, logging, os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from core_tools import NAV_ITEMS, ROOT_PATH, TEMPLATE_DIR

#List players
class Players(webapp2.RequestHandler):
    def get(self):
        tmpl_vars = {
             'current_tab' : None, 
             'nav_items' : NAV_ITEMS, 
             'main_page' : 'players.html'
        }
        path = os.path.join(os.path.dirname(__file__) + "/HTML", 'index.html')
        self.response.out.write(template.render(path, tmpl_vars))
        
    def post(self):
        out = {}
        for i in self.request.arguments():
            out[i] = self.request.get(i)
            logging.info('['+i+']' + " " + out[i])
            
        self.redirect('/players/')

app = webapp2.WSGIApplication([
   ('/players/', Players)
])