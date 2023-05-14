#import flask - from the package import a module
from flask import Flask 


#create a function that creates a web application
# a web server will run this web application
def create_app():
    app = Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug = True

    #secret key so we can use session
    app.secret_key = 'usuallymoresecretthanthis'

    #add the Blueprint
    from . import views
    app.register_blueprint(views.bp)
    
    return app


if __name__ == '__main__':
    napp = create_app()
    napp.run(debug = True)