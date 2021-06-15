from app import create_app,db 
from app.models import Pitch,PitchComments,User,Upvotes,Downvotes 
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
# Creating app instance
app = create_app('development')
# app=create_app('development')
# app=create_app('test')

 # create migrate instance
migrate = Migrate(app, db)
 #create manager instance
manager = Manager(app)

manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.command
def test():
    '''
    does unit test
    '''
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Pitch=Pitch,PitchComments=PitchComments)


if __name__ == '__main__':
    manager.run()