from Base import baseclass
from estate import apartment,house
from deal import rent,sell


class apartmentsell(baseclass,apartment,sell):
    def showdeatial(self):
        self.show_description()
        self.showPrice()


class apartmentrent(baseclass,apartment,rent):
    def showdetail(self):
        self.show_description()

class houseSell(baseclass,house,sell):
    def show_detail(self):
        self.show_description()
        self.show_price()


class houseRent(baseclass,house,rent):
    def show_detail(self):
        self.show_description()
        # self.show_price()

