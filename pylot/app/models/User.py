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

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """
    def create_user(self, info):
        email_check ="select email from users where email ='{}'".format(info['email'])
        print email_check
        emails = self.db.query_db(email_check)
        # print emails
        error = []

        if len(info['email'])<1 or len(info['first_name']) < 1 or len(info['last_name']) < 1 or len(info['password']) < 1:
            error.append("please don't leave anything black")
        if not EMAIL_REGEX.match(info['email']):
            error.append('please enter a proper email')
        # if len(emails) > 0:
        #     error.append('this email already exists')
        # if info['password'] != info['confirm_password']:
        #     error.append('the passwords are not matching')
        print "len of error=", len(error)
        # didn't od anything with the birthday cause i was too stuck on figuering not friend. refer to app/models/friendship/not_friend
        if error:
            print error
            return{"status":False, "errors":error}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(info['password'])
            insert_query = "INSERT INTO `givr`.`users` (`first_name`, `last_name`, `password`, `email`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}','{}', NOW(),NOW() )".format(info['first_name'],info['last_name'],hashed_pw, info['email']);
            print insert_query
            self.db.query_db(insert_query)
            # print insert_query
            query = "select * from users where email = '{}' ".format(info['email']);
            print query
            user = self.db.query_db(query)
            return {"status":True, "user":user[0]}

    def user_info_by_id(self, user_id):
        query = "select * from users where id ={}".format(user_id)
        user_info = self.db.query_db(query)
        return user_info[0]

    def show_all_users(self):
        query= "select * from users"
        return self.db.query_db(query)

    def login(self,info):
        query = "select * from users where email = '{}'".format(info['email'])
        check = self.db.query_db(query)
        if check and self.bcrypt.check_password_hash(check[0]['password'], info['password']):
            return {'status':True, 'user':check[0]}
        message = "please enter a proper email/password combination"
        return{'status':False,'message':message}

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """
