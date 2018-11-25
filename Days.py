# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

#define lengths of months and years
long_month = 31
short_month = 30
feb_no_leap = 28
feb_leap = 29
leap_year_days = 366
no_leap_year_days = 365

# Is it a leap year?
def is_leap_year(year):
    year = year+0.0
    if year/4 == round(year/4,0):
        return True
    return False

#Is it in the same year?
def is_same_year(start_year,end_year):
    if start_year==end_year:
        return True
    return False

#How many days left in year 1?
def days_left_start_year(start_year,start_month, start_day):
    days=0
    while start_month!=12:
        if start_month==1 or start_month==3 or start_month==5 or start_month==7 or start_month==8 or start_month==10:
            days = days + long_month
        if start_month== 4 or start_month==6 or start_month==9 or start_month==11:
            days = days + short_month
        if start_month== 2:
            if is_leap_year(start_year):
                days = days + feb_leap
            else:
                days = days + feb_no_leap
        start_month=start_month+1

        
#get to end 1st of Jan of following year
    days = days + (long_month+ 1 - start_day)
    return(days)

#How many days in end_year?
def days_to_end_date_in_end_year(end_year,end_month,end_day):
    days=0
    while end_month!=12:
        if end_month==1 or end_month==3 or end_month==5 or end_month==7 or end_month==8 or end_month==10:
            days = days + long_month
        if end_month== 4 or end_month==6 or end_month==9 or end_month==11:
            days = days + short_month
        if end_month== 2:
            if is_leap_year(end_year):
                days = days + feb_leap
            else:
                days = days + feb_no_leap
        end_month=end_month+1

    days = days + (32-end_day)

    if is_leap_year(end_year):
        days_to_end_date_in_end_year = leap_year_days-days
    else:
        days_to_end_date_in_end_year=no_leap_year_days-days
    return(days_to_end_date_in_end_year)

#How many days are there in whole years between years 1 and 2?
def whole_years(start_year, end_year):
    whole_years = 0
    while start_year < end_year-1:
        if is_leap_year(start_year+1) == True:
            whole_years = whole_years + leap_year_days
        else:
            whole_years = whole_years + no_leap_year_days
        start_year = start_year+1
    return(whole_years)

#The number of days between date 1 and date 2
#If year 1 == year 2, it would be days in year 2 + days in year 1 - either no_leap_year_days or leap_year_days
#Otherwise,
def days_between_dates(start_year, start_month, start_day, end_year, end_month, end_day):
    #is the birthday and end day in same year?
    if start_year==end_year:
        #if so, if it's a leap year, take the daysa from birthday to end of year, the days from beginning of year to end date, and subtract the # of dats in that year
        #This gives you the intersection
        if is_leap_year(start_year)==True:
            return (days_left_start_year(start_year, start_month, start_day) + days_to_end_date_in_end_year(end_year, end_month, end_day)-leap_year_days)
        else:
            return (days_left_start_year(start_year, start_month, start_day) +days_to_end_date_in_end_year(end_year, end_month, end_day)-no_leap_year_days)
    else:
        #if not all in the same year, then the # of days is the # of days remaining in the start_year, the # of days in the whole years between, and the # of days to the end date
        return(days_left_start_year(start_year, start_month, start_day)+days_to_end_date_in_end_year(end_year, end_month, end_day)+whole_years(start_year, end_year))

# Problem Set test routine


def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585),
                  ((1900,1,1,1999,12,31), 36524)]
    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
