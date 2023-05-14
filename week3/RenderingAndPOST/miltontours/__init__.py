#import flask - from  package import Class/module
from flask import Flask 


#create a function that creates a web application
# a web server will run this web application
def create_app():
    app = Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug = True
    #add the Blueprint
    from . import views
    app.register_blueprint(views.bp)
    
    return app

