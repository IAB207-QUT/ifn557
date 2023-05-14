class Order:
    def __init__(self, status, firstname, surname, email, phone, date, tours, total_cost):
        self.status = status
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.date = date
        self.tours = tours
        self.total_cost = total_cost
    
    def get_tour_details(self):
        return str(self)

    def __repr__(self):
        str = "Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Tours: {}, Total Cost: {}\n" 
        str = str.format( self.status,self.firstname,self.surname, self.email, self.phone, self.date, self.tours, self.total_cost)
        return str