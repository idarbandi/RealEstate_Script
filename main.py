from sample import samples
from advertisements import *


#TODO:Search_By_Multiple_Values.For_Examle
# : apartmentsell.manager.search(area__min=3,area__max=4)
#We use handler to handle the imported Samples
class Handler:
    """handler Class has a RUN class_Func which
    Initiates The Samples And Updates us About The Data"""

    advertisement_types = {
        1:apartmentrent,2:apartmentsell,
        3:houseSell,4:houseSell

    }

    switches = {
        'r':'get_report',
        's':'show_all'

    }

    def get_report(self):
        for abd in self.advertisement_types.values():
            print(abd,abd.manager.counter())


    def show_all(self):
       for abd in self.advertisement_types.values():
           print(abd,abd.manager.counter())
           for obj in abd.objects_list:
               print(obj.showdetail)

    def run(self):
        print('Wellcome To Our RealEstate')
        for key in self.switches:
            print(f"press {key} for {self.switches[key]}")
            usr_input = input('Enter Your choice ')
            Switch = self.switches.get(usr_input,None)
            if Switch is None:
                print('Wrong Choose')
                self.run()
            choice = getattr(self,Switch,None)
            choice()


if __name__ == "__main__":
    samples()
    print(apartmentsell.manager.search(area__min=500,area__max=600))