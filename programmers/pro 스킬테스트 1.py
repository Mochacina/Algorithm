from datetime import datetime
def solution(a, b):
    wd = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    date = '2016-' + str(a) + '-' + str(b)
    datetime_date = datetime.strptime(date, '%Y-%m-%d')
    print(datetime_date.weekday())
    return wd[datetime_date.weekday()]

a = 5
b = 24
print(solution(a,b))