from datetime import datetime


users = [{'Вадік Лопата': datetime(1983, 6, 24)}, {'Коля Катлєта': datetime(2001, 6, 20)}, {'Олєжа Кактус': datetime(1995, 6, 22)}, {'Саня Зарядка': datetime(2020, 6, 23)}, {'Вася Васєчкін': datetime(1999, 6, 22)}]
need_to_say_happy_b = {}
d = {}

def main():
    def get_birthdays_per_week(user):
        for name, birthday in user.items():
            midl_date = datetime((birthday.year + (datetime.now().year - birthday.year)), birthday.month, birthday.day)
            if 358 <= (datetime.now() - midl_date).days%365 <= 365 or (datetime.now() - midl_date).days%365 == 0:
                weekday_word = midl_date.strftime('%A')
                weekday_num = midl_date.weekday()
                if weekday_num in [5,6]:
                    weekday_word = 'Monday'
                    weekday_num = 0
                return name, weekday_word, weekday_num

    for user in users:
        if get_birthdays_per_week(user):

            try:
                need_to_say_happy_b[get_birthdays_per_week(user)[2]].append(get_birthdays_per_week(user)[0])
            except KeyError:
                need_to_say_happy_b[get_birthdays_per_week(user)[2]] = []
                need_to_say_happy_b[get_birthdays_per_week(user)[2]].append(get_birthdays_per_week(user)[0])

            d[get_birthdays_per_week(user)[2]] = get_birthdays_per_week(user)[1]

    need_to_say_happy_b_sorted = dict(sorted(need_to_say_happy_b.items()))

    for num, day in dict(sorted(d.items())).items():
        key_holder = need_to_say_happy_b_sorted[num]
        del need_to_say_happy_b_sorted[num]
        need_to_say_happy_b_sorted[day] = key_holder

    # Printing
    for day, names_list in need_to_say_happy_b_sorted.items():
        result_print_txt = f'{day}: '
        for name in names_list:
            result_print_txt += name + ', '
        print(result_print_txt.removesuffix(', '))

if __name__ == "__main__":
    main()