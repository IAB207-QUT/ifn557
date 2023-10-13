#import flask - from package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

#create a function that creates a web application
# a web server will run this web application
def create_app():
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123'

    bootstrap = Bootstrap4(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)
    
    @app.errorhandler(404) 
    # Inbuilt function (to Flask) which takes error as parameter
    def not_found(e): 
      return render_template("error.html", error=e)

    # Handles server errors (look-up 'HTTP response status codes')
    @app.errorhandler(500)
    def internal_error(e):
      return render_template("error.html", error=e)   
   
    return app