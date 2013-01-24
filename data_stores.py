'''

Central hub of datastores classes

Created on 24/01/2013

@author: Adam Carter
'''

import logging, types, datetime, time, random, md5
from google.appengine.ext import db

def createURI():
    hexStr = generateID(object())
    return hexStr
    
def generateID(obj):
    objectHash = obj.__hash__()
    milliseconds1970 = 1000.00 * time.mktime(datetime.datetime.now().timetuple())
    nonHashID = str(objectHash) + str(milliseconds1970) + str(random.random())
    
    return md5.md5(nonHashID).hexdigest()


class URIModel(db.Model):
    uri = db.StringProperty(required=False, default = createURI(), indexed=True)
    deleted = db.BooleanProperty(required = True, default = False)
    timestamp = db.DateTimeProperty(auto_now_add = True)
    
class Club(URIModel):
    clubName = db.StringProperty(required = True)
    clubShortName = db.StringProperty()
    
class Player(URIModel):
    givenName = db.StringProperty(required=True)
    familyName = db.StringProperty(required=True)
    
class PlayerClubTriple(URIModel):
    playerURI = db.StringProperty(required = True)
    clubURI = db.StringProperty(required = True)
    
    playerReference = db.ReferenceProperty(Player)
    clubReference = db.StringProperty(Club)
    
    
class Discipline(URIModel):
    broadName = db.StringProperty(required = True)
    
class PlayerDisiplineTriple(URIModel):
    playerURI = db.StringProperty(required = True)
    DisciplineURI = db.StringProperty(required = True)
    
    playerReference = db.ReferenceProperty(Player)
    DisciplineReference = db.ReferenceProperty(Discipline)

    