from system.core.model import Model

class Request(Model):
    def __init__(self):
        super(Request, self).__init__()
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
   def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        
        return self.load_view('index.html')