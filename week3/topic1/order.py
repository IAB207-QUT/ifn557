class Order:

    def __init__(self, status, date, tours, total_cost, firstname, surname, email, phone):
        self.status = status
        self.date = date
        self.tours = tours
        self.total_cost = total_cost
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone

    def __repr__(self):
        str = 'Status: {}, First Name: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Tours: {}, Total Cost: {}\n'
        str = str.format(self.status, self.firstname, self.surname, self.email, self.phone, self.date, self.tours, self.total_cost)
        return str
    
    def get_order_details(self):
        return str(self)