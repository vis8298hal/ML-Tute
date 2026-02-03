import calendar

def create_calendar():
    # Text Calendar
    text_cal = calendar.TextCalendar(calendar.SUNDAY)
    str1 = text_cal.formatmonth(2026, 2,1,1)
    print(str1)
    #HTML Calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    str2 = hc.formatmonth(2026, 2, 1)
    print(str2)

def loop_days_mon():
    c = calendar.TextCalendar(calendar.SUNDAY)
    for i in c.itermonthdays(2026, 2):
        print(i)

def locale_loop():
    for name in enumerate(calendar.month_name):
        print(name)
    print("---------Days--------------")
    for day in enumerate(calendar.day_name):
        print(day)

def countdown_to_fri():
    print("Team Meetings will be On : ")
    for m in range(1,13):
        cal = calendar.monthcalendar(2026, m)
        week_1 = cal[0]
        week_2 = cal[1]
        if week_1[calendar.FRIDAY] != 0:
            meet_deay = week_1[calendar.FRIDAY]
        else:
            meeet_day = week_2[calendar.FRIDAY]
        print(calendar.month_name[m], meet_deay)

def main():
    create_calendar()
    loop_days_mon()
    locale_loop()
    countdown_to_fri()
    return 0

if __name__ == "__main__":
    main()