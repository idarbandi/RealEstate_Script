from abc import ABC


class sell(ABC):
    def __init__(self,price_per_meter,discountable,convertable=False,*args,**kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args,**kwargs)

    def showPrice(self):
        print(f"the Price is : {self.price_per_meter}/t discount is {self.discountable}")


class rent(ABC):
    def __init__(self,initial_price,monthly_price,convertable,discountable,*args,**kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args,**kwargs)


    def showPrice(self):
        return f"youre looking at a {self.initial_price} property"

