from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/tours/<int:city_id>')
def citytours(city_id):
    return render_template('citytours.html')

# Stubs for routes not implemented yet
# (url_for links in the templates will fail without these routes defined)
@main_bp.route('/order', methods=['POST','GET'])
def order():
    return 'not implemented yet'

@main_bp.route('/deleteorder')
def deleteorder():
    return 'not implemented yet'

@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    return 'not implemented yet'

@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
    return 'not implemented yet'