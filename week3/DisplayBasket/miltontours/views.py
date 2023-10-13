from flask import Blueprint, render_template, request, session
from .models import City, Tour, Order
from datetime import datetime

# This data will eventually be stored in a database
sydney = City('1', 'Sydney', 'City in New South Wales with largest population', 'sydney.jpg')
brisbane = City('2', 'Brisbane', 'City in Queensland with a good weather', 'brisbane.jpg')
tour1 = Tour('1', 'Kangaroo point walk', 'Gentle stroll but be careful of cliffs. Hand feed the kangaroos', 't_hand.jpg', 99.00, brisbane, datetime(2023,7,23))
tour2 = Tour('2', 'West End markets', 'Tour the boutique goods and food and ride the wheel', 't_ride.jpg', 20.00, brisbane, datetime(2023,10,30))
tour3 = Tour('3', 'Whale spotting', 'Visit Straddy and see the whales migrating', 't_whale.jpg', 129.00, sydney, datetime(2023,10,30))
cities = [brisbane, sydney]
tours = [tour1, tour2, tour3]
order1 = Order('1', False, '', '','', '', datetime.now(), [tour1, tour2], tour1.price + tour2.price) # simulating order not checked out
order2 = Order('2', False, '', '','', '', datetime.now(), [tour3], tour1.price + tour3.price) # simulating order not checked out
orders = [order1, order2]

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', cities=cities)

@bp.route('/tours/<int:city_id>/')
def citytours(city_id):
    # Create an empty list that will hold the Tours for this City
    city_tours = []
    # Loop over the list of tours and add the tours that match this city's ID to the city_tours list
    # HINT: tours comes from the list declared above on line 12
    for tour in tours:
        if int(tour.city.id) == int(city_id): 
            city_tours.append(tour)
    return render_template('citytours.html', tours=city_tours)

@bp.route('/order/', methods=['POST', 'GET'])
def order():
    tour_id = request.args.get('tour_id')
    # is this a new order?
    if 'order_id' not in session:
        session['order_id'] = 1 # arbitrary, we could set either order 1 or order 2
    
    #retrieve correct order object
    for i in orders:
            if int(i.id) == int(session['order_id']): 
                order = i
    # are we adding an item? - will be implemented later with DB
    if tour_id:
        print(f'User requested to add tour id = {tour_id}')

    return render_template('order.html', order=order, totalprice=order.total_cost)

@bp.route('/deleteorder/')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
    return render_template('index.html')

@bp.route('/deleteorderitem/', methods = ['POST'])
def deleteorderitem():
    print(f'User wants to delete tour with id={request.form["id"]}')
    return render_template('index.html')