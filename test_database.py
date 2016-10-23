from database import Database as DB

db = DB()

db.insert({'longitude': 50, 'latitude': 100, 'light': 0, 'acc': 5.0, 'tmp': 10.0, 'baro': 999.0})
db.insert({'longitude': 1, 'latitude': 200, 'light': 1, 'acc': 5.0, 'tmp': 10.0, 'baro': 100.0})
print db.retrieve('all')
print

print db.retrieve('range', '2010-10-01', '2016-11-31')
print

print db.retrieve('latest')
