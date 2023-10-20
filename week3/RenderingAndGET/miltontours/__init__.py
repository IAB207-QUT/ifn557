#import flask - from the package import a module or Class
from flask import Flask

# create a function that creates a web app
# a web server will run this web app
def create_app():
    # this is the name of the module/package that is calling this app
    app = Flask(__name__)

    # Disable this in production
    app.debug = True

    #add the Blueprint
    from . import views
    app.register_blueprint(views.bp)
    
    return app