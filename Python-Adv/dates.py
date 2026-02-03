import datetime
def get_today_date():
    today = datetime.date.today()
    print(today)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("date Components : ",today.day, today.month, today.year)
    print("Today's Weekday is : ", days[today.weekday()])

def get_curr_datetime():
    now = datetime.datetime.now()
    print("Current date and time : ", now)
    print("Time is : ", datetime.datetime.time(now))
    return now

def format_datetime(datetime_obj):
    print(datetime_obj.strftime("The Current Year is :%Y"))
    print(datetime_obj.strftime("The Current Date is :%a %d %B %y"))
    #a : Day of week short form
    #d : Day of Month
    #B : Month Full form
    #y : Year short form    

def format_datetime_locale(datetime_obj):
    print(datetime_obj.strftime("Locale Date & time :%c"))
    print(datetime_obj.strftime("Locale Date  :%x"))
    print(datetime_obj.strftime("Locale time :%X"))

def format_time(datetime_obj):
    print(datetime_obj.strftime("Current Time : %I : %M : %S      %p"))

def main():
    #Call here
    get_today_date()
    nw = get_curr_datetime()
    format_datetime(nw)
    format_datetime_locale(nw)
    format_time(nw)
    return 0

if __name__ == "__main__":
    main()