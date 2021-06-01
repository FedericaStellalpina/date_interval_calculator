#From start date --> periods of 4 weeks to current date
# define start date
# define current date
# define period length
# print separate periods



import datetime

date_format = "%d/%m/%Y"

#find the monday from the start date

start_date = datetime.datetime.strptime("30/4/2007", date_format).date()
monday_st_da = start_date - datetime.timedelta(days=start_date.weekday())

# add sunday for week calculation has to be done for

last_da = datetime.datetime.strptime("25/3/2021", date_format).date()
d = monday_st_da

# define period (how many weeks?)

step = datetime.timedelta(days=28)

# define end period (step - 1)
step1 = datetime.timedelta (days =27)
d1a = d + step1

while d < last_da:

    print('from ' + d.strftime(date_format) + ' to ' + d1a.strftime(date_format))
    d += step
    d1a += step

#def
#input start date
#input end date
#input period length
#call def
