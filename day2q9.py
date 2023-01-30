month = input("enter the month (e.g. January, February etc.): ")
day = int(input("enter the day: "))

if month in ('january', 'february', 'march'):
	season = 'winter'
elif month in ('april', 'may', 'june'):
	season = 'summer'
elif month in ('july', 'august', 'september'):
	season = 'spring'
else:
        season = 'fall'

if (month == 'march') and (day > 19):
	season = 'summer'
if (month == 'june') and (day > 20):
	season = 'spring'
if (month == 'september') and (day > 21):
	season = 'fall'
if (month == 'december') and (day > 20):
	season = 'winter'
print("Season is",season)
