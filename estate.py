from abc import ABC,abstractmethod
from Base import baseclass

class estateabstract(ABC):
    def __init__(self , user , area , rooms_count ,built_year , region , address , *args , **kwargs):
        self.user = user
        self.area = area
        self.rooms_count = rooms_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args , **kwargs)

    @abstractmethod
    def show_description(self):
        pass



class apartment(estateabstract):
    def __init__(self , has_parking , has_elevator , floor , *args , **kwargs):
        self.has_parking = has_parking
        self.has_elevator = has_elevator
        self.floor = floor
        super().__init__(*args,**kwargs)

    def show_description(self):
        return f"the apartment is {self.area} meters "



class house(estateabstract):
    def __init__(self , has_yard , floors_count , *args , **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count
        super().__init__(*args,**kwargs)

    def show_description(self):
        return f"the house is {self.area} meters"

