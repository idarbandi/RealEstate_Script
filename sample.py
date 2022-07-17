from advertisements import *
from region import region
from user import user
from estate import apartment,house




def samples():
    u1 = user(firstname='Ray', lastname='Donavan', phonenumber=253669875)
    u2 = user(firstname='Mickey', lastname='Donavan', phonenumber=253666987)
    u3 = user(firstname='Sully',lastname='Sullivan',phonenumber=2536996832)

    Los_angeles = region(name='calabases')
    southy = region(name='Boston')

    myapartment = apartmentrent(has_parking=True, has_elevator=False, floor=2,
                                user=u1, area=250, rooms_count=3, built_year=2009
                                , region=Los_angeles, address=Los_angeles.name,
                                initial_price=600, monthly_price=20, convertable=False
                                , discountable=True)
    mickeys_House = apartmentsell(has_parking=False, has_elevator=True, floor=3,
                                  price_per_meter=3,discountable=False
                                  ,convertable=False,user=u3, area=500
                                  , rooms_count=3
                                  ,built_year=1956,region=southy, address=southy.name)

    house_rent = houseRent(
        has_yard=True, floors_count=1, user=u1, area=400,
        rooms_count=6, built_year=1370, region=Los_angeles, address='Some text ...',
        initial_price=130, monthly_price=5.5, convertable=False, discountable=True
    )

    house_sell = houseSell(
        has_yard=True, floors_count=1, user=u2, area=400,
        rooms_count=6, built_year=1370, region=southy, address='Some text ...',
        price_per_meter=20, discountable=False, convertable=False
    )

    House = house(
        has_yard=True, floors_count=1, user=u2, area=400,
        rooms_count=6, built_year=1370, region=southy, address='Some text ...'
    )

    apt1 = apartment(
        has_elevator=True, has_parking=True, floor=2, user=u1,
        built_year=1393, region=Los_angeles, area=80, rooms_count=2,
        address="Some text..."
    )

    print('#'*20,'samples Succesfully Imported','#'*20)



