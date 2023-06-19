from datetime import datetime


WEEKDAYS_LIST = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
users = [{'Вадік Лопата': datetime(1983, 6, 24)}, {'Коля Катлєта': datetime(2001, 6, 25)}, {'Олєжа Кактус': datetime(1995, 6, 22)}, {'Саня Зарядка': datetime(2020, 6, 22)}, {'Вася Васєчкін': datetime(1999, 6, 23)}]
need_to_say_happy_b = {}

def get_birthdays_per_week(user):
    for name, birthday in user.items():
        midl_date = datetime((birthday.year + (datetime.now().year - birthday.year)), birthday.month, birthday.day)
        if 358 <= (datetime.now() - midl_date).days%365 <= 365 or (datetime.now() - midl_date).days%365 == 0:
            weekday = midl_date.strftime('%A')
            return name, weekday

for user in users:
    if get_birthdays_per_week(user):

        try:
            need_to_say_happy_b[get_birthdays_per_week(user)[1]].append(get_birthdays_per_week(user)[0])
        except KeyError:
            need_to_say_happy_b[get_birthdays_per_week(user)[1]] = []
            need_to_say_happy_b[get_birthdays_per_week(user)[1]].append(get_birthdays_per_week(user)[0])


# Days order changing and weekend days replacing
need_to_say_happy_b_edited = {}
for weekend_day in WEEKDAYS_LIST[-2:]:
    for day, names_list in need_to_say_happy_b.items():
        if day == weekend_day:
            for name in names_list:
                try:
                    need_to_say_happy_b_edited[WEEKDAYS_LIST[0]].append(name)
                except KeyError:
                    need_to_say_happy_b_edited[WEEKDAYS_LIST[0]] = []
                    need_to_say_happy_b_edited[WEEKDAYS_LIST[0]].append(name)

for weekday in WEEKDAYS_LIST[:-2]:   
    for day, names_list in need_to_say_happy_b.items():
        if day == weekday:
            need_to_say_happy_b_edited[day] = names_list


# Printing
for day, names_list in need_to_say_happy_b_edited.items():
    result_print_txt = f'{day}: '
    for name in names_list:
        result_print_txt += name + ', '
    print(result_print_txt.removesuffix(', '))