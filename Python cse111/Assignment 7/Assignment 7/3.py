class Dates:
    def __init__(self,date):
        self.date=date
    @classmethod
    def toDashDate(cls,db):
        temp=db.replace("/","-")
        return cls(temp)
    def getDate(self):
        return self.date
print('It prints Equal because the value of "date1.getDate()" and the value of "date2.getDate()" is equal. The "date1.getDate()" was created when the object "data1" was created. It is the address of "05-09-2020". On ther other hand "data2.getData()" was created when "Date.toDashDate(dateFromDB)" was called. It created an object which had the address "date2" and an instance variable was created named "date2.getDate()" which is the address of "05-09-2020". This "05-09-2020" was created from "05/09/2020" on that previous class method named "Date.toDashDate(dateFromDB)".')
#===================
date1 = Dates("05-09-2020")
dateFromDB = "05/09/2020"
date2= Dates.toDashDate(dateFromDB)
if(date1.getDate() == date2.getDate() ):
    print("Equal")
else:
    print("Unequal")
