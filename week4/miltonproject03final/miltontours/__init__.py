from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():
    app = Flask(__name__)
    # Don't leave this enabled in production
    app.debug = True
    
    app.secret_key = 'BetterSecretNeeded123'

    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///milton.sqlite'

    # initialise db with flask app - necessary because scope of app
    # is only here in create_app, but db is defined globally
    db.init_app(app)
    
    Bootstrap4(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.main_bp)
    #from . import admin
    #app.register_blueprint(admin.admin_bp)
    
    @app.errorhandler(404) 
    # Inbuilt function (to Flask) which takes error as parameter
    def not_found(e): 
      return render_template("error.html", error=e)

    # Handles server errors (look-up 'HTTP response status codes')
    @app.errorhandler(500)
    def internal_error(e):
      return render_template("error.html", error=e)
   
    return app