#import flask - from the package import a module or Class
from flask import Flask

# create a function that creates a web app
# a web server will run this web app
def create_app():
    # this is the name of the module/package that is calling this app
    app = Flask(__name__)
    
    # set a secret key so we can use Flask 'session'
    app.secret_key = 'usuallymoresecretthanthis'

    # Disable this in production
    app.debug = True

    #add the Blueprint
    from . import views
    app.register_blueprint(views.bp)
    
    return app

# This creates the app when using the app factory pattern
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)