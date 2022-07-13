from advertisements import *
from region import region
from user import user


u1 = user(firstname='Ray',lastname='Donavan',phonenumber=253669875)
u2 = user(firstname='Mickey',lastname='Donavan',phonenumber=253666987)


Los_angeles=region(name='calabases')
southy=region(name='Boston')


myapartment = apartmentrent(has_parking=True , has_elevator=False , floor=2,
                            user=u1 , area=250 , rooms_count=3 ,built_year=2009
                            , region=Los_angeles, address=Los_angeles.name ,
                            initial_price=200,monthly_price=20,convertable=False
                            ,discountable=True)



if __name__ == "__main__":
    print(apartmentrent.mro())
    print(apartmentrent.manager.search(floor=2))


