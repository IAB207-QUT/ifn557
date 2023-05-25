from flask import Blueprint, render_template
from .models import City, Tour, Order

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    cities = City.query.order_by(City.name).all()
    return render_template('index.html', cities=cities)

@main_bp.route('/tours/<int:cityid>')
def citytours(cityid):
    tours = Tour.query.filter(Tour.city_id==cityid)
    return render_template('citytours.html', tours=tours)

# STUBS for routes not implemented yet
# (get_url links in the templates will fail without these routes defined)

@main_bp.route('/order', methods=['POST','GET'])
def order(id):
    #return render_template('order.html', order = order, totalprice = order.total_cost)
    order = Order.query.order_by(id=id).all()
    return render_template('order.html', order = order, totalprice = order.total_cost)

@main_bp.route('/deleteorder')
def deleteorder():
    #return render_template('index.html')
    return 'not implemented yet'

@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    #return render_template('index.html')
    return 'not implemented yet'

@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
    #return render_template('checkout.html', form = form)
    return 'not implemented yet'