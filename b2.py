import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2000-01-8, format)
print('day ' + str(t1.day))
print('month ' + str(t1.month))
print('minute ' + str(t1.second))
# Define todays date and time
t2 = dt.datetime.now()
diff = t2-t1
print('How many days difference? ' + str(diff.days))
