""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

class Request(Model):
    def __init__(self):
        super(Request, self).__init__()

    def create_request(self, info):
        query ="INSERT INTO requests (name, description, location, lat, long, image_address,\
            created_at, updated_at, user_id, accept_status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', NOW(), NOW(),'{}', '{}');"\
            .format(info['helpee'], info['description'],info['intersection'], info['latt'],info['long'],info["photo"], info['user_id'], "Waiting")
        print query
        # return self.db.query_db(query)
        return 

    def select_all_request(self):
        return 

    def get_requests(self):
        query = "SELECT name, description, location, created_at FROM requests"
        return self.db.query_db(query)





