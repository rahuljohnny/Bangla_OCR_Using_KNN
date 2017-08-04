# !/usr/bin/env python

import sys

class Employee:


    def __init__(self ,first ,last ,pay):
        self. first =first
        self. last =last
        self. pay =pay
        self. mail = first + '.' + last +'@company.com'

    def fullname(self):  # get the average of three numbers
        return '{} {}'.format(self.first ,self.last)
    def house_location(self,cottage_location):
        self.cottage_location = cottage_location
        return 'home of {} {} is in {}'.format(self.first,self.last,self.cottage_location)

    def occupation(self,occupation):
        self.occupation = occupation
        return 'occupation of {} {} is in {}'.format(self.first,self.last,self.occupation)


emp_1= Employee('Corey', 'Schafer', 50000)
emp_2= Employee('Bilbo', 'Baggins', 60000)
#emp_3 = Employee.occupation('farmer')

print Employee.fullname(emp_2)
print Employee.house_location(emp_2,'Shire')
print Employee.occupation(emp_2,'farmer')

