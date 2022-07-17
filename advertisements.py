from Base import baseclass
from estate import apartment,house
from deal import rent,sell


class apartmentsell(baseclass,apartment,sell):
    def showdetail(self):
        self.show_description()
        self.showPrice()

    def __str__(self):
        return f"Following apartmnent is for sale with {self.price_per_meter} million"


class apartmentrent(baseclass,apartment,rent):
    def showdetail(self):
        self.show_description()

    def __str__(self):
        return f"Following apartmnent is for rent with {self.initial_price} million"

class houseSell(baseclass,house,sell):
    def showdetail(self):
        self.show_description()
        self.showPrice()


    def __str__(self):
        return f"Following House is for sale with {self.price_per_meter} million"


class houseRent(baseclass,house,rent):
    def showdetail(self):
        self.show_description()
        # self.show_price()

    def __str__(self):
        return f"Following House is for rent with {self.monthly_price} million"

