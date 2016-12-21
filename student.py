from datetime import datetime
import datetime
class Student:
    def __init__(self,name,hometown,age,height,fav_IC, by, bm, bd):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.fav_IC=fav_IC
        self.by=by
        self.bm=bm
        self.bd=bd
        

    def print_summary(self):
        print(str(self.name) + ' is from ' + str(self.hometown) + ' and is ' + str(self.age) + '. He/she is ' + str(self.height) + 'cm tall and their favorite ice cream flavor ' + str(self.fav_IC) + '.')

    def get_giraffe_gap(self):
        X= 500-(int(self.age))
        return X

    def get_days_to_birthday(self):
        now=datetime.date.today()
        bday=datetime.date(self.by, self.bm, self.bd)
        return str(bday-now)
