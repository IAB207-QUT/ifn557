#import flask - from the package import class
from flask import Flask, render_template

#create a function that creates a web application
# a web server will run this web application
def create_app():
  app = Flask(__name__)
  
  app.debug = True
  
  #importing modules here to avoid circular references, register blueprints of routes
  from . import views
  app.register_blueprint(views.bp)
  
  # Error handler to deal with 404 page not found errors
  @app.errorhandler(404) 
  # Inbuilt function (to Flask) which takes error as parameter
  def not_found(e): 
    return render_template("error.html", error=e)

  # Handles server errors (look-up 'HTTP response status codes')
  @app.errorhandler(500)
  def internal_error(e):
    return render_template("error.html", error=e)
   
  return app