'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

runners_minutes = 30
runners_seconds = 30
runners_distance = 10

runners_hours = (runners_minutes/60) + (runners_seconds/60/60)

print(runners_hours)

runners_speed = (runners_distance / runners_hours) * 1.6

print(runners_speed, "KM/H")