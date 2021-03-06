import datetime
import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dayoftheweek = datetime.date(year, month, day).weekday()
        days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return days[dayoftheweek]
        
def dayOfTheWeekAlt(day, month, year):
    date = str(day) + '' + str(month) + '' + str(year)
    day = datetime.strptime(date, '%d %m %Y').weekday()
    return day