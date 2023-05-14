'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import City, Tour, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    city1 = City(name='Sydney', image='sydney.jpg', \
        description='''The state capital of New South Wales and the most populous city in Australia and Oceania.Located on Australia's east coast, the metropolis surrounds Port Jackson and extends about 70 km (43.5 mi) on its periphery towards the Blue Mountains to the west, Hawkesbury to the north, the Royal National Park to the south and Macarthur to the south-west. Sydney is famous for
spectacular beaches; beautiful parks; a wealth of diversity; incredibly tasty food; The Harbour; and outdoor experiences''')
    city2 = City(name='Brisbane', image='brisbane.jpg', \
        description='''The state capital of and the most populated city in the Australian state of Queensland, and the third most populous city in Australia. Brisbane's metropolitan area has a population of approximately 2.5 million, and the South East Queensland metropolitan region, centred on Brisbane, encompasses a population of more than 3.6 million. It is known as the gateway to the reef and is famous for
friendly Koalas; dolphin spotting; sand Dunes; being a cosmopolitan city; tremendous beaches within 45 minutes; diversity of eateries; and daily tours to Fraser Island and the Reef''')
    city3 = City(name='Melbourne', image='melbourne.jpg', \
        description='''The capital and most populous city of the Australian state of Victoria, and the second most populous city in Australia and Oceania. The city occupies much of the coastline of Port Phillip bay and spreads into the hinterlands towards the Dandenong and Macedon ranges, Mornington Peninsula and Yarra Valley. Melbourne is famous for
being the world’s most livable city; amazing coffee; being the sports capital of Australia; urban laneways; incredible food; eclectic festivals; and fashion-forward trends''')
      
    try:
        db.session.add(city1)
        db.session.add(city2)
        db.session.add(city3)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    t1 = Tour(city_id=city1.id, image='t_cuddle.jpg', price=59.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Cuddle koalas',\
        description= 'Lone Pine Koala Sanctuary is the world\'s first and largest koala sanctuary and is home to more than 130 koalas. Hand-feed their kangaroos and wild lorikeets, be entertained by a platypus or - best of all - get cuddly with a beautiful koala. Duration 0900-1400 (5hrs), begins at entrance to Koala Plaza') 
    t2 = Tour(city_id=city1.id, image='t_hand.jpg', price=100.50,\
        date=datetime.datetime(2020, 2, 1),\
        name='Hand-feed kangaroo',\
        description= 'Get up close and personal with Australia\'s favourite wildlife and tick two items off your bucket list with a trip to Lone Pine Koala Sanctuary. Lone Pine is only 40 minutes from the CBD by bus and you\'ll be cuddling up to koalas and hand-feeding kangaroos in no time. Don\'t forget the selfie! Duration 0900-1300 (4hrs), begins at entrance to Kanga Plaza.')
    t3 = Tour(city_id=city1.id, image='t_sand.jpg', price=180.50,\
        date=datetime.datetime(2020, 3, 10),\
        name='Sand island adventure',\
        description= 'You don\'t have to travel to the far north to see Australia\'s bustling reef and sea life. Take a short ferry ride from the Port of Brisbane and you\'ll find yourself at Moreton Island, a tropical sand island with crystal-clear coastal water, lakes and incredible snorkelling at the historic Tangalooma Wrecks. You\'ll want your GoPro to take some incredible underwater snaps. Duration 0900-1700 (8hrs), begins at entrance to Transit Centre.')
    t4 = Tour(city_id=city1.id, image='t_whale.jpg', price=99.99,\
        date=datetime.datetime(2020, 8, 1),\
        name='Whale watching',\
        description= 'From June to November, Whale Watching Tours inc. runs daily cruises for those who want to witness the incredible acrobatics of the southern humpback whale. More than 20,000 whales migrate through every winter. Tickets for the five-hour cruise through Moreton Bay are good value and include guaranteed whale sightings. Duration 1300-1800 (5hrs), begins at entrance to Port Street.')                
    t5 = Tour(city_id=city2.id, image='t_trek.jpg', price=49.00,\
        date=datetime.datetime(2020, 4, 20),\
        name='Trek around the national park',\
        description= 'Forget the outback and take in the green scene. While most international visitors picture red dirt when they think of Australia, you\'re more likely to find yourself surrounded by lush greenery than outback desert. Take the opportunity to check out local fauna and flora at the national parks, as close as 20 minutes from the CBD. Did we mention our parks have drop-bears? Must bring sunblock. Duration 1000-1300 (3hrs), begins at entrance to Forrest Car Park.')
    t6 = Tour(city_id=city2.id, image='t_island.jpg', price=250.99,\
        date=datetime.datetime(2021, 1, 2),\
        name='Island adventure',\
        description= 'The world\'s biggest sand island is just a few hours away. Heritage-listed Big Sandy Island has more than 100 freshwater lakes, pristine water and white-sand beaches. There\'s many ways to explore the island but the most fun is by four-wheel-drive. Join a tour such as the Dingos Resort tag-along four-wheel drive tour, where you can drive yourself and make friends along the way. Duration 0600-1600 (11hrs), begins at entrance to Ferry Road.')
    t7 = Tour(city_id=city2.id, image='t_freshwater.jpg', price=120.00,\
        date=datetime.datetime(2020, 11, 1),\
        name='Freshwater swimming holes',\
        description= 'You can\'t come to Australia without enjoying the abundant inland lakes, falls and swimming holes. There\'s almost too many to choose from. Check out Visit our must-swim spots. Duration 0900-1200 (3hrs), begins at entrance to River Park.')
    t8 = Tour(city_id=city2.id, image='t_cruise.jpg', price=60.00,\
        date=datetime.datetime(2020, 4, 1),\
        name='Cruise our wonderful river',\
        description= 'Jump on board a CityCat  or ride our private City Cab to explore the city by ferry. CityCats run between the city and various points of interest all the way around to killer bay. Duration 1000-1200 (2hrs), begins at entrance to CBD Ferry Stop.')
    t9 = Tour(city_id=city3.id, image='t_go.jpg', price=189.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Go chasing waterfalls, waterholes and lakes',\
        description= 'We\'re all about the aquatic life over here in Oz, and you can be too. Take a short trip into the coast and hinterland to discover an abundance of natural waterfalls, waterholes and lakes. You are going to love the diversity we will show you. Duration 0800-1700 (9hrs), begins at entrance Bush Station.')
    t10 = Tour(city_id=city3.id, image='t_climb.jpg', price=89.95,\
        date=datetime.datetime(2020, 6, 19),\
        name='Climb to the top of the City Bridge',\
        description= 'Get your own city skyline pic when you climb the City Bridge, right here in the CBD. The City Bridge Adventure Climb is one of only three bridge climbs in the world and shows off spectacular city and river views. Twilight is the best time to climb. Free use of safety equipment. Duration 1800-2100 (3hrs), begins at bottom of CBD Climb Inc Office.')
    t11 = Tour(city_id=city3.id, image='t_ride.jpg', price=45.99,\
        date=datetime.datetime(2020, 2, 24),\
        name='Ride the City Wheel',\
        description= 'Enjoy city views without the climb in the air-conditioned comfort of the City Wheel. Every city has its vantage point and for ours, this is it! Ride at night to see the city light up. Duration 1800-2100 (3hrs), begins at bottom of CBD Wheel Inc Booth.')
    t12 = Tour(city_id=city3.id, image='t_sunrise.jpg', price=49.99,\
        date=datetime.datetime(2020, 10, 10),\
        name='Sunrise at Mt High-er',\
        description= 'The official city Lookout at Mt High-er is a heritage-listed site boasting panoramic views of the outer region. This is a definite city bucket list item for locals and travellers alike – and yes, it\'s worth the 4am alarm. Duration 0400-0900 (5hrs), begins at High-er visitor centre.')
    t13 = Tour(city_id=city3.id, image='t_streets.jpg', price=45.00,\
        date=datetime.datetime(2020, 7, 7),\
        name='Streets Beach BBQ',\
        description= 'Take a dip and enjoy a BBQ a Australia\'s only inner-city man-made beach. Streets Beach at North Bank holds the equivalent of five Olympic swimming pools of water, so there\'s no shortage of space to cool down. Pack your swimmers, bring your friends and don\'t forget to grab an included ice-cream. Duration 1500-1800 (3hrs), begins at Life Guard Central on Streets Beach.')

    try:
        db.session.add(t1)
        db.session.add(t2)
        db.session.add(t3)
        db.session.add(t4)
        db.session.add(t5)
        db.session.add(t6)
        db.session.add(t7)
        db.session.add(t8)
        db.session.add(t9)
        db.session.add(t10)
        db.session.add(t11)
        db.session.add(t12)
        db.session.add(t13)
        db.session.commit()
    except:
        return 'There was an issue adding a tour in dbseed function'

    return 'DATA LOADED'


