"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('User')

    """ This is an example of a controller method that will load a view for the client """
    def create(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        item = {
            'first_name' : request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'username':request.form['username']
            'password':request.form['password']
        }
        created_status = self.models['User'].create_user(reg_info)

        if created_status['status'] == True:
            session['id'] = created_status['user']['id']
            session['name'] = created_status['user']['name']
            return redirect("/Requests/home/{}".format(int(session['id'])))
        else:
            for message in created_status['errors']:
                flash (message, 'regis_errors')
        return redirect('/Requests/home')

    def login(self):
        log_info ={
            'email':request.form['email'],
            'password':request.form['password']
        }
        login_attemp = self.models['User'].login(log_info)
        if login_attemp['status'] == True:
            session['id'] = login_attemp['user']['id']
            return redirect ("/Users/home/{}".format(login_attemp['user']['id']))
        else:
            flash(login_attemp['message'])
        return redirect('/')


    def logout(self):
        session.pop('id')
        return redirect('/')


