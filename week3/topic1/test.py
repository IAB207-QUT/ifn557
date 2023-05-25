from datetime import datetime
from miltontours.city import City
from miltontours.tour import Tour
from miltontours.order import Order

print('Creating a city Brisbane')
brisbane = City('Brisbane', 'City in Queensland with a good weather', 'brisbane.jpg')
print(brisbane)
print('#################')

print('Creating a new tour for Brisbane')
tour1 = Tour('Kangaroo point walk', 'Gentle stroll but be careful of cliffs', 'kanga.jpg', 99.00, brisbane, datetime(2023,7,23))
print(tour1)
print('#################')

print('Creating another new tour for Brisbane')
tour2 = Tour('West End markets', 'Tour the boutique goods and food', 'wemarket.jpg', 20.00, brisbane, datetime(2023,10,30))
print(tour2)
print('#################')

print('Creating a new order')
order = Order(False, 'Jane', 'Smith', 'jsmith@gmail.com', '0402 111 222', datetime.now(), [tour1, tour2], tour1.price + tour2.price)
print(order)