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

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """
    def user_info_by_id(self, user_id):
        query = "select * from users where id =%s"
        data = user_id
        user_info = self.db.query_db(query, user_id)
        return user_info[0]



    def create_user(self, info):
        email_check ="select email from users where email =%s"
        data = info['email']
        print email_check
        emails = self.db.query_db(email_check, data)
        # this process check if the email already exist or not
        error = []

        if len(info['first_name'])<1 or len(info['Last_name']) < 1 or len(info['email']) < 1 or len(info['password']) < 1 or len(info['username']) < 1:
            error.append("please don't leave anything black")
        if not (info['name']).isalpha():
            error.append('your name should only consists of letters')
        if not EMAIL_REGEX.match(info['email']):
            error.append('please enter a proper email')
        # if len(emails) > 0:
        #     error.append('this email already exists')

        # if info['password'] != info['confirm_password']:
        #     error.append('the passwords are not matching')
            # i am thinking of not needing the user to confirm password, because thats what most apps are like nowaday

        if error:
            print error
            return{"status":False, "errors":error}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(info['password'])
            insert_query = "INSERT INTO `givr`.`users` (`first_name`, `last_name`, `password`, `email`, `username`, `created_at`, `updated_at`) VALUES (%s, %s, %s,%s,%s, NOW(),NOW() )"
            data = (info['first_name'], info['last_name'],hashed_pw, info['email'], info['username'])
            # print insert_query
            self.db.query_db(insert_query, data)
            query = "select * from users where email = %s"
            data2 = (info['email']);
            print query
            user = self.db.query_db(query, data2)
            return {"status":True, "user":user[0]}

    def login(self,info):
        query = "select * from users where email = %s"
        data  =(info['email'])
        check = self.db.query_db(query,data)
        if check and self.bcrypt.check_password_hash(check[0]['password'], info['password']):
            return {'status':True, 'user':check[0]}
        message = "please enter a proper email/password combination"
        return{'status':False,'message':message}




