#!/usr/bin/env python3
class Date:
    def __init__(self, year, month, day):

        mon_max = self.days_in_mon(year)
        if (month > 12 or month < 1) :
            print("Error: wrong month entered")
            return False
        elif (day > mon_max[month] or day < 1):
            print("Error: wrong day entered")
        else:  
            self.year = year
            self.month = month
            self.day = day

    def  __repr__(self): 
        return '%.4d-%.2d-%.2d' % (self.year, self.month, self.day)
        #return date object as a string in "yyyy-mm-dd" format

    def __str__(self): 
        return '%.4d/%.2d/%.2d' % (self.year, self.month, self.day)
        #return date object as a string in "yyyy/mm/dd" format

    def days_in_mon(self, year):
        feb_max = 29 if self.leap_year(year) else 28
        return { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
     
    def leap_year(self, year):
        lyear = year % 4
        leapYear = True if lyear == 0 else False
     
        lyear = year % 100
        if lyear == 0:
            leapYear = False

        lyear = year % 400
        if lyear == 0:
            leapYear = True

        return leapYear
        
    def __add__(self, other):
        day = self.day
        month = self.month
        year = self.year
    
        mon_max = self.days_in_mon(year)

        for x in range(int(other)):
            day += 1 # next day
            if day > mon_max[month]:
                day = 1 # if tmp_day > this month's max, reset to 1
                month += 1
           
            if month > 12:
                month = 1
                year += 1
                mon_max = self.days_in_mon(year)
                
        return Date(year, month, day)
              
       
    def  __sub__(self, other):
        if type(other) is not Date:
            day = self.day
            month = self.month
            year = self.year
            
            mon_max = self.days_in_mon(year)

            for x in range(int(other)):
                day -= 1 # previous day
                if day < 1:
                    month -= 1
                    if month < 1:
                        month = 12
                        year -= 1
                    mon_max = self.days_in_mon(year)
                    day = mon_max[month]
                    
            return Date(year, month, day)
              
        else:
            return (self.days_to_time()  - other.days_to_time())

    def tomorrow(self):
        return self + 1

    def yesterday(self):
        return self - 1

    def day_of_week(self):
        day = self.day
        month = self.month
        year = self.year
        # https://en.wikipedia.org/wiki/Zeller%27s_congruence
        if month == 1:
            month = 13
            year -= 1
        elif month == 2:
            month = 14
            year -= 1
        yearC = year % 100
        century = year // 100
        functionCal = (day + int(13*(month + 1)/5.0) + yearC + int(yearC/4.0)) + int(century/4.0) - 2 * century
        dayOfWeek = (functionCal - 1) % 7
        return dayOfWeek

    def days_to_time(self):
        #convert an integer which is n days from epoch (Jan 1, 1970) to a corresponding date object
        day1 = self.day
        month1 = self.month
        year1 = self.year
    
        year2 = 1970
        month2 = 1
        day2 = 1
    
        if (year2 < year1 or year2 == year1 and month2 < month1 or year2 == year1 and month2 == month1 and day2 < day1):
            year2 = year2 + year1
            year1 = year2 - year1
            year2 = year2 - year1
            month2 = month2 + month1
            month1 = month2 - month1
            month2 = month2 - month1
            day2 = day2 + day1
            day1 = day2 - day1
            day2 = day2 - day1
     
        mon_max = self.days_in_mon(year1)
        count = 0

        while not(year2 == year1 and month2 == month1 and day2 == day1):
            day1 = day1 + 1 # next day
            if day1 > mon_max[month1]:
                day1 = 1 # if tmp_day > this month's max, reset to 1
                month1 = month1 + 1
       
            if month1 > 12:
                month1 = 1
                year1 = year1 + 1
                mon_max = self.days_in_mon(year1)

            count = count + 1

        return abs(count)
    


