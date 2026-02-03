from datetime import timedelta
import datetime

def basic_timedelta_operations():
    print(timedelta(days=365, hours=5, minutes=1))
    now = datetime.datetime.now()
    print("Current date and time : ", now)
    print("An Year from Now is : ", str(now + timedelta(days=365)))
    print("In 2 weeks & 3 days", str(now + timedelta(weeks=2, days=3)))

    t= datetime.datetime.now() - timedelta(weeks=1, days=1)
    s = t.strftime("%a %d %B %Y")
    print("One week ago it was : ", s)

def april_fool_day_cnt():
    today = datetime.date.today()
    afd = datetime.date(today.year, 4,1)
    if afd < today:
        print("April foold day Already went by : ", (today-afd).days, "days ago")
        afd = afd.replace(year = today.year +1)
        time_to_afd = afd-today
        print("Time to April foold day : ", time_to_afd.days, "days")
    else:
        
        time_to_afd = afd-today
        print("Time to April foold day : ", time_to_afd.days, "days")

def main():
    basic_timedelta_operations()
    april_fool_day_cnt()
    return 0

if __name__ == "__main__":
    main()