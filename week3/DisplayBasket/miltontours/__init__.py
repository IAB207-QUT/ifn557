#import flask - e.g., from 'package' import 'thing' (can be Classes, functions and more)
from flask import Flask, render_template

# create a function that creates a web app
# a WSGI server will run this app
def create_app():
  app = Flask(__name__)

  app.debug = True

  # Why do we need this secret_key?
  app.secret_key = 'BetterSecretNeeded123'
    
  # Importing modules here to avoid circular references
  from . import views
  # Every blueprint must be registered with our app, else it's routes won't 'exist'
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