class Date:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validate(day, month, year):
        my_list = []

        if 1 > day or day > 31:
            my_list.append(f'День введен неверно!')
        if 1 > month or month > 12:
            my_list.append(f'Месяц введен неверно!')
        if year <= 0:
            my_list.append(f'Год введен неверно!')
        if len(my_list) > 0:
            return " ".join(my_list)
        else:
            return f'Данные введены верно.'

    def __str__(self):
        return f'Текущая дата - {Date.extract(self.day_month_year)}'


today = Date('18 - 11 - 2021')
print(today)

print(Date.validate(15, 9, 2008))
print(Date.validate(40, 15, -22))

print(Date.extract('12 - 04 - 1944'))
