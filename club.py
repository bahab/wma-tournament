'''
Created on 23/01/2013

@author: Adam Carter
'''

import webapp2, os, logging, cgi, data_stores
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from core_tools import NAV_ITEMS, ROOT_PATH, TEMPLATE_DIR

# Register new clubs
class ClubRegistration(webapp2.RequestHandler):
    def get(self):
        clubs = data_stores.Club.all()
        tmpl_vars = {
             'current_tab' : None, 
             'nav_items' : NAV_ITEMS, 
             'main_page' : 'clubs.html',
             'clubs' : clubs
        }
        
        
        
        path = os.path.join(os.path.dirname(__file__) + "/HTML", 'index.html')
        self.response.out.write(template.render(path, tmpl_vars))
        
    def post(self):
        out = {}
        for i in self.request.arguments():
            out[i] = self.request.get(i)
            logging.info('['+i+']' + " " + out[i])
            
        cName = cgi.escape(self.request.get('clubName'))
        cShortName = cgi.escape(self.request.get('clubShortName'))
        
        #check to see if unique // or add functionality to ensure unique add
        
        club = data_stores.Club (
             clubName = cName,
             clubShortName = cShortName 
        )
        
        club.put()
        
        self.redirect('/clubs/new/')
        
app = webapp2.WSGIApplication([
   ('/clubs/new/', ClubRegistration)
])